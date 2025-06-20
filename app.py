import json
import subprocess
import tempfile
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load questions from JSON file
def load_questions():
    try:
        with open('questions.json', 'r') as f:
            questions_data = json.load(f)
        return questions_data
    except FileNotFoundError:
        print("ERROR: questions.json not found.")
        return []
    except json.JSONDecodeError:
        print("ERROR: Could not decode questions.json. Make sure it's valid JSON.")
        return []

questions = load_questions()

# Timeout for code execution in seconds
CODE_EXECUTION_TIMEOUT = 5

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/question/<int:question_id>')
def question_page(question_id):
    question = next((q for q in questions if q["id"] == question_id), None)
    if question:
        return render_template('question_page.html', question=question)
    return "Question not found", 404

@app.route('/run_code', methods=['POST'])
def run_code():
    data = request.get_json()
    user_code = data.get('code', '')
    question_id = data.get('question_id')

    if not question_id:
        return jsonify({"error": "Missing question_id"}), 400

    question = next((q for q in questions if q["id"] == question_id), None)
    if not question:
        return jsonify({"error": "Question not found"}), 404

    results = []
    overall_success = True

    # Create a temporary file to write the user's code and test harness
    # This helps in managing the execution scope and makes it easier to run with subprocess
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.py', encoding='utf-8') as tmp_file:
        # Start with necessary imports if any (e.g., for type hints if they are used in evaluation)
        # For now, assume standard library is sufficient.
        # If questions require specific imports, this setup would need to be more sophisticated.

        # Write the user's code
        tmp_file.write(user_code + "\n\n")

        # Write test execution logic
        for i, test_case in enumerate(question.get("test_cases", [])):
            input_data = test_case["input"] # This is a dict
            expected_output = test_case["output"]

            # Assuming the function signature in question.json is like "def func_name(arg1, arg2):"
            # We need to extract the function name.
            # This is a simplistic way; a robust parser might be needed for complex signatures.
            try:
                func_name = question["function_signature"].split("def ")[1].split("(")[0].strip()
            except IndexError:
                return jsonify({"error": f"Could not parse function name from signature: {question['function_signature']}"}), 500

            # Construct the function call string
            # Example: if input_data is {"nums": [1,2], "target": 3}, call_str will be "func_name(nums=[1,2], target=3)"
            args_str = ", ".join(f"{k}={repr(v)}" for k, v in input_data.items())
            call_str = f"{func_name}({args_str})"

            # Write the code to call the function and print its output for this test case
            # We'll use a specific marker to find the output later
            tmp_file.write(f"print('---TEST_CASE_OUTPUT_START_{i}---')\n")
            tmp_file.write(f"try:\n")
            tmp_file.write(f"    actual_output = {call_str}\n")
            tmp_file.write(f"    print(repr(actual_output))\n") # repr() helps to get string representation of various types
            tmp_file.write(f"except Exception as e:\n")
            tmp_file.write(f"    print(f'ERROR: {{e.__class__.__name__}}: {{str(e)}}')\n")
            tmp_file.write(f"print('---TEST_CASE_OUTPUT_END_{i}---')\n\n")

        tmp_file_path = tmp_file.name

    # Execute the temporary file using subprocess
    try:
        # Using python executable explicitly. Ensure this is the desired Python environment.
        # On some systems, 'python' might point to Python 2. 'python3' is often safer.
        # For now, assuming 'python' is appropriate for the sandbox.
        process = subprocess.run(
            ['python', tmp_file_path],
            capture_output=True,
            text=True,
            timeout=CODE_EXECUTION_TIMEOUT,
            check=False # Don't raise exception for non-zero exit codes, we'll handle it
        )

        stdout = process.stdout
        stderr = process.stderr

        if process.returncode != 0:
            # General script error (not specific to a test case's try-except)
            # This could be a syntax error in user code before any test case runs,
            # or an unhandled exception in the test harness itself (less likely).
            if not stderr and not stdout: # Sometimes error is not captured if script fails very early
                 stderr = "Script execution failed with return code " + str(process.returncode) + ". Possible syntax error or early crash."

        # Parse stdout to get results for each test case
        current_test_case_idx = 0
        for test_case in question.get("test_cases", []):
            expected_output = test_case["output"]
            output_marker_start = f"---TEST_CASE_OUTPUT_START_{current_test_case_idx}---"
            output_marker_end = f"---TEST_CASE_OUTPUT_END_{current_test_case_idx}---"

            start_idx = stdout.find(output_marker_start)
            end_idx = stdout.find(output_marker_end)

            actual_output_str = "Error: Could not find output markers."
            status = "error"

            if start_idx != -1 and end_idx != -1:
                actual_output_str = stdout[start_idx + len(output_marker_start):end_idx].strip()

                if actual_output_str.startswith("ERROR:"):
                    status = "error"
                else:
                    try:
                        # Attempt to evaluate the captured output string (e.g., 'None', '[1, 2]', 'True')
                        # This is potentially risky if output is not well-formed, but repr() should make it safe.
                        # A safer way would be to use ast.literal_eval if output is guaranteed to be a literal.
                        # For now, direct eval on repr() output is common for simple types.
                        actual_output_val = eval(actual_output_str)
                        if actual_output_val == expected_output:
                            status = "pass"
                        else:
                            status = "fail"
                            overall_success = False
                    except Exception as e:
                        status = "error"
                        actual_output_str += f"\nError evaluating output: {str(e)}"
                        overall_success = False
            else:
                overall_success = False # If markers are missing, something went wrong

            results.append({
                "input": test_case["input"],
                "expected": expected_output,
                "actual": actual_output_str, # Send the string representation
                "status": status
            })
            current_test_case_idx += 1

        if stderr: # Append any stderr not captured by individual test try-except to the last result or as general error
            if results:
                # If stderr seems to be a general error not tied to a specific test case's execution print
                if not any(res["status"] == "error" and stderr in res["actual"] for res in results):
                     results.append({"type": "general_error", "output": stderr.strip()})
            elif not stdout : # If there's only stderr and no stdout at all
                 results.append({"type": "general_error", "output": stderr.strip(), "status": "error"})
                 overall_success = False


    except subprocess.TimeoutExpired:
        results.append({"type": "timeout_error", "output": f"Code execution timed out after {CODE_EXECUTION_TIMEOUT} seconds.", "status": "error"})
        overall_success = False
    except Exception as e:
        results.append({"type": "execution_error", "output": f"An unexpected error occurred: {str(e)}", "status": "error"})
        overall_success = False
    finally:
        # Clean up the temporary file
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)

    return jsonify({
        "overall_success": overall_success,
        "results": results,
        "raw_stdout": process.stdout if 'process' in locals() else "N/A", # For debugging
        "raw_stderr": process.stderr if 'process' in locals() else "N/A"  # For debugging
        })


if __name__ == '__main__':
    # Use Gunicorn or another WSGI server in production
    # For local development, app.run(debug=True) is fine.
    # Setting host='0.0.0.0' makes it accessible on the network if needed for testing from other devices.
    app.run(debug=True, host='0.0.0.0')

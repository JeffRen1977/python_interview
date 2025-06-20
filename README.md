# Python Interview Practice Web App

This project is an AI-powered web application designed to help users practice for technical interviews, covering coding questions, system design, and behavioral questions.

## Running the Application

1.  **Ensure Python is installed:** You'll need Python 3.x (Python 3.7+ recommended).
2.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
3.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    # venv\\Scripts\\activate
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    You should see output indicating the server is running, typically on `http://127.0.0.1:5000/`.

6.  **Access the web app:** Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Features (Phase 1 - Basic)

*   View a list of coding questions.
*   Select a question to see its description, examples, and function signature.
*   Enter Python code in an online editor.
*   Run the code against predefined test cases.
*   View results: pass/fail status for each test case, expected vs. actual output, and any errors.

## Project Structure

```
.
├── app.py                   # Main Flask application
├── questions.json           # Stores coding questions, test cases, etc.
├── requirements.txt         # Python dependencies
├── static/                  # Static files (CSS, JS)
│   └── style.css
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── index.html           # Homepage - lists questions
│   └── question_page.html   # Displays individual question and editor
├── ... (original Python coding problem files)
└── README.md                # This file
```

## Future Development (Next Phases)

*   **AI-Powered Assistance:**
    *   Hints and clarifications for questions.
    *   AI feedback on code style, efficiency, and correctness.
    *   Explanation of reference solutions.
*   **System Design & Behavioral Questions:** Modules for these types of interview questions.
*   **Database Integration:** Store questions, user progress, and solutions.
*   **User Accounts:** Allow users to track their progress.
*   **Enhanced Code Editor:** Syntax highlighting, autocompletion.
*   **Secure Code Execution:** Transition from `subprocess` to a containerized (e.g., Docker) execution environment for security and better resource management.

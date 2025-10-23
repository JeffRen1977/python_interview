class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)  # length of string a
        len_b = len(b)  # length of string b
        max_length = max(len_a, len_b)  # find the maximum length of both strings
        carry = 0  # initialize carry
        new_str = []  # list to store binary result

        # Traverse both strings from right to left
        for i in range(-1, -max_length - 1, -1):
            element_a = int(a[i]) if i >= -len_a else 0  # digit from a or 0 if out of bounds
            element_b = int(b[i]) if i >= -len_b else 0  # digit from b or 0 if out of bounds

            # Calculate sum of current bits and carry
            add = element_a + element_b + carry
            value = add % 2  # current binary digit (remainder)
            carry = add // 2  # update carry (quotient)

            # Add the current binary digit to the front of the result list
            new_str.insert(0, str(value))

        # If there's a carry left, add it to the front of the result list
        if carry != 0:
            new_str.insert(0, str(carry))

        # Join the list into a string and return
        return ''.join(new_str)

def main():
    sol = Solution()

    # Example 1
    a1 = "11"
    b1 = "1"
    output1 = sol.addBinary(a1, b1)
    print(f"Binary addition of {a1} and {b1} is: {output1}")  # Expected output: "100"

    # Additional Test Cases
    # Case 2: Both inputs are the same length with multiple carries
    a2 = "1010"
    b2 = "1011"
    output2 = sol.addBinary(a2, b2)
    print(f"Binary addition of {a2} and {b2} is: {output2}")  # Expected output: "10101"

    # Case 3: Different lengths with carry overflow
    a3 = "111"
    b3 = "10"
    output3 = sol.addBinary(a3, b3)
    print(f"Binary addition of {a3} and {b3} is: {output3}")  # Expected output: "1001"

    # Case 4: No carry
    a4 = "110"
    b4 = "001"
    output4 = sol.addBinary(a4, b4)
    print(f"Binary addition of {a4} and {b4} is: {output4}")  # Expected output: "111"

    # Case 5: Both inputs are zeros
    a5 = "0"
    b5 = "0"
    output5 = sol.addBinary(a5, b5)
    print(f"Binary addition of {a5} and {b5} is: {output5}")  # Expected output: "0"

main()

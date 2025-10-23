class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # Remove leading and trailing whitespace
        if not s:
            return False
        ls = s.split('e')  # Split by 'e' to check if it's exponential notation
        if len(ls) == 1:  # No 'e' in the string
            return self.decide_num(ls[0])
        elif len(ls) == 2:  # Contains 'e', so split into base and exponent
            return self.decide_num(ls[0]) and self.decide_pow(ls[1])
        else:
            return False  # More than one 'e' is invalid

    def decide_num(self, s: str) -> bool:
        if not s:
            return False
        if s[0] in ['+', '-']:  # Skip leading '+' or '-'
            s = s[1:]
        ls = s.split('.')  # Split by '.' to check for decimal numbers
        if len(ls) == 1:  # No '.'
            return ls[0].isnumeric()
        elif len(ls) == 2:  # Contains '.'
            # Check for valid numbers before and after the '.'
            if not ls[0] and ls[1].isnumeric():  # Empty before '.'
                return True
            elif not ls[1] and ls[0].isnumeric():  # Empty after '.'
                return True
            else:
                return ls[0].isnumeric() and ls[1].isnumeric()
        else:
            return False  # More than one '.' is invalid

    def decide_pow(self, s: str) -> bool:
        if not s:
            return False
        if s[0] in ['+', '-']:  # Skip leading '+' or '-'
            s = s[1:]
        return s.isnumeric()  # Exponent must be a valid integer

def main():
    solution = Solution()
    test_cases = [
        ("0", True),
        ("0.1", True),
        ("abc", False),
        ("1 a", False),
        ("2e10", True),
        (" -90e3   ", True),
        (" 1e", False),
        ("e3", False),
        (" 6e-1", True),
        (" 99e2.5 ", False),
        ("53.5e93", True),
        (" --6 ", False),
        ("-+3", False),
        ("95a54e53", False),
    ]

    for s, expected in test_cases:
        result = solution.isNumber(s)
        print(f"Input: '{s}' | Expected: {expected} | Result: {result} | {'Pass' if result == expected else 'Fail'}")

if __name__ == "__main__":
    main()

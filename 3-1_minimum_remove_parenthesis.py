from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = deque()  # Stack to store indices of unmatched parentheses
        for i, ch in enumerate(s):
            if ch == '(':  # If it's an opening parenthesis, push index onto the stack
                stk.append(i)
            elif ch == ')':
                # If there's a matching '(', pop it from the stack
                if stk and s[stk[-1]] == '(':
                    stk.pop()
                else:
                    # If there's no matching '(', push index onto the stack
                    stk.append(i)

        # Now the stack contains indices of unmatched parentheses
        res = ""
        for i in range(len(s)):
            if stk and i == stk[0]:  # If index is in the stack, skip it
                stk.popleft()
            else:
                res += s[i]  # Otherwise, add character to result

        return res

def main():
    solution = Solution()
    test_cases = [
        ("lee(t(c)o)de)", "lee(t(c)o)de"),  # Example 1
        ("a)b(c)d", "ab(c)d"),              # Example 2
        ("))((", ""),                       # Example 3
        ("(a(b(c)d)", "a(b(c)d)"),          # Additional Test Case 1
        ("abc", "abc"),                     # Additional Test Case 2 (no parentheses)
        ("", ""),                           # Additional Test Case 3 (empty string)
    ]

    for s, expected in test_cases:
        result = solution.minRemoveToMakeValid(s)
        print(f"Input: '{s}' | Expected: '{expected}' | Result: '{result}' | {'Pass' if result == expected else 'Fail'}")

if __name__ == "__main__":
    main()

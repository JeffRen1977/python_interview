import collections

# Solution class as provided
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s += "@"  # Append "@" to the end of the string `s`. This acts as a sentinel to prevent out-of-bound errors.

        # Define a dictionary to store the character counts of the target string `t`.
        # This is a Counter object that tracks the frequency of each character in `t`.
        dict_t = collections.Counter(t)

        # Initialize two pointers `l` (left) and `r` (right), which will be used to create a sliding window.
        # Initialize `figures` to the number of distinct characters in `t` that need to be matched in `s`.
        l, r, figures = 0, 0, len(dict_t.keys())

        # Initialize a `res` list to store the starting and ending indices of the smallest window.
        # The result starts with a size larger than the length of `s` to ensure any valid window can replace it.
        res = [0, len(s) + 1]

        # While the right pointer `r` is within bounds of string `s`:
        while r < len(s):
            # If `figures` is 0, it means the current window contains all the required characters.
            if figures == 0:
                # Check if the current window length (r - l) is smaller than the best result found so far.
                if r - l < res[1] - res[0]:
                    # If so, update `res` with the current window's start and end indices.
                    res = [l, r]

                # If the character at the left pointer `l` is part of `dict_t`:
                if s[l] in dict_t:
                    # Increment its count back (since we are shrinking the window from the left).
                    dict_t[s[l]] += 1
                    # If its count becomes positive, it means we are missing this character in the window.
                    if dict_t[s[l]] > 0:
                        # Increase `figures` since we now need to find this character again.
                        figures += 1
                # Move the left pointer to the right, shrinking the window.
                l += 1
            else:
                # If `figures` is not 0, we haven't found all the characters yet.
                # Check if the character at the right pointer `r` is part of `dict_t`:
                if s[r] in dict_t:
                    # Decrement its count since it's now part of the window.
                    dict_t[s[r]] -= 1
                    # If its count becomes 0, it means we have matched this character fully.
                    if dict_t[s[r]] == 0:
                        # Decrease `figures` since this character is now satisfied.
                        figures -= 1
                # Move the right pointer to the right, expanding the window.
                r += 1

        # After the loop, if no valid window was found, return an empty string.
        if res == [0, len(s) + 1]:
            return ""
        # Otherwise, return the smallest window found in `s`.
        else:
            return s[res[0]:res[1]]

# Main function to test the Solution class
def main():
    # Test cases
    test_cases = [
        ("ADOBECODEBANC", "ABC"),  # Expected output: "BANC"
        ("a", "a"),               # Expected output: "a"
        ("a", "aa"),              # Expected output: ""
        ("thisisateststring", "tist"),  # Expected output: "tstri"
    ]

    # Create an instance of Solution
    solution = Solution()

    # Test each case
    for s, t in test_cases:
        result = solution.minWindow(s, t)
        print(f"minWindow('{s}', '{t}') -> '{result}'")

# Run the main function
if __name__ == "__main__":
    main()







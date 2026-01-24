class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # Define a list of length n+1 to store the ways to decode up to each point
        dp = [0] * (n + 1)

        # Base cases
        dp[0] = 1  # One way to decode an empty string
        dp[1] = 0 if s[0] == '0' else 1  # If the first character is '0', no valid decoding

        # Fill in the dp array
        for i in range(2, n + 1):
            # `first` represents the single digit at the current position
            first = int(s[i - 1:i])

            # `second` represents the two digits formed by the current and previous position
            second = int(s[i - 2:i])

            # If the single digit is valid (1-9), add the ways from dp[i-1]
            if 1 <= first <= 9:
                dp[i] += dp[i - 1]

            # If the two-digit number is valid (10-26), add the ways from dp[i-2]
            if 10 <= second <= 26:
                dp[i] += dp[i - 2]

        # The last element of dp will contain the total number of ways to decode the full string
        return dp[n]


def main():
    solution = Solution()

    # Test cases
    print(solution.numDecodings("12"))  # Output: 2
    print(solution.numDecodings("226"))  # Output: 3
    print(solution.numDecodings("06"))  # Output: 0
    print(solution.numDecodings("10"))  # Output: 1
    print(solution.numDecodings("27"))  # Output: 1
    print(solution.numDecodings("11106"))  # Output: 2


if __name__ == "__main__":
    main()

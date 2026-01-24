from typing import List
from sys import maxsize


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize a dp array where dp[i] means the minimum coins needed for amount i.
        # Set all values to a large number initially, as we want to minimize this later.
        dp = [maxsize] * (amount + 1)

        # Base case: 0 coins are needed to make the amount of 0.
        dp[0] = 0

        # Iterate over each coin
        for coin in coins:
            # Update the dp array for all amounts from 1 to 'amount'
            for i in range(1, amount + 1):
                # Only update if the current amount is at least as large as the coin's value
                if i >= coin:
                    # dp[i] is updated to the minimum of its current value or
                    # dp[i - coin] + 1, which represents taking this coin.
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still set to maxsize, it means we can't form this amount
        # Return -1 in that case. Otherwise, return dp[amount].
        return -1 if dp[amount] == maxsize else dp[amount]


def main():
    # Instantiate the Solution class
    solution = Solution()

    # Test cases
    test_cases = [
        # Basic cases
        {"coins": [1, 2, 5], "amount": 11, "expected": 3},  # 11 = 5 + 5 + 1
        {"coins": [2], "amount": 3, "expected": -1},  # Cannot make 3 with only 2s
        {"coins": [1], "amount": 0, "expected": 0},  # Amount is 0, no coins needed
        {"coins": [1], "amount": 2, "expected": 2},  # 2 = 1 + 1

        # Edge cases
        {"coins": [1, 3, 4], "amount": 6, "expected": 2},  # 6 = 3 + 3
        {"coins": [2, 4], "amount": 7, "expected": -1},  # Impossible to make 7 with [2, 4]
        {"coins": [5, 10, 25], "amount": 30, "expected": 2},  # 30 = 25 + 5
        {"coins": [2, 5, 10, 1], "amount": 27, "expected": 4},  # 27 = 10 + 10 + 5 + 2

        # Large case
        {"coins": [186, 419, 83, 408], "amount": 6249, "expected": 20},
    ]

    # Test each case
    for i, test_case in enumerate(test_cases):
        coins = test_case["coins"]
        amount = test_case["amount"]
        expected = test_case["expected"]

        # Get the result from the coinChange function
        result = solution.coinChange(coins, amount)

        # Print the results
        print(f"Test case {i + 1}: coins = {coins}, amount = {amount}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")
        print("------")


# Run the main test function
if __name__ == "__main__":
    main()
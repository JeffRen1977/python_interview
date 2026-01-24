from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        player1_score = self.dfs(nums, 0, len(nums) - 1)
        player2_score = total_sum - player1_score
        return player1_score >= player2_score

    def dfs(self, nums: List[int], s: int, e: int) -> int:
        if s > e:
            return 0
        # If Player 1 chooses the start element
        start = nums[s] + min(self.dfs(nums, s + 1, e - 1), self.dfs(nums, s + 2, e))
        # If Player 1 chooses the end element
        end = nums[e] + min(self.dfs(nums, s + 1, e - 1), self.dfs(nums, s, e - 2))
        # Player 1 maximizes their score
        return max(start, end)


def main():
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 5, 2], False),  # Example 1: Player 1 cannot win
        ([1, 5, 233, 7], True),  # Example 2: Player 1 can win
        ([1, 2, 3, 4], True),  # Player 1 can at least tie
        ([1, 5, 2, 4, 6], True),  # Player 1 can win with optimal strategy
        ([7, 8, 8, 9], True),  # Player 1 can win with an equal number of values
        ([5], True),  # Edge case: Only one element, Player 1 wins by default
        ([2, 2], True),  # Edge case: Two equal elements, Player 1 can at least tie
    ]

    # Run each test case
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.PredictTheWinner(nums)
        print(f"Test Case {i + 1}: Input: {nums}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")
        print("")


# Run the main function
if __name__ == "__main__":
    main()

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, profit = float('inf'), 0
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit


# Main function to test the code
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    prices = [7, 1, 5, 3, 6, 4]
    print("Test Case 1")
    print("Prices:", prices)
    print("Maximum Profit:", solution.maxProfit(prices))  # Expected Output: 5

    # Test case 2
    prices = [7, 6, 4, 3, 1]
    print("\nTest Case 2")
    print("Prices:", prices)
    print("Maximum Profit:", solution.maxProfit(prices))  # Expected Output: 0 (no profit possible)

    # Test case 3
    prices = [1, 2, 3, 4, 5]
    print("\nTest Case 3")
    print("Prices:", prices)
    print("Maximum Profit:", solution.maxProfit(prices))  # Expected Output: 4

    # Test case 4
    prices = [3, 2, 6, 1, 4]
    print("\nTest Case 4")
    print("Prices:", prices)
    print("Maximum Profit:", solution.maxProfit(prices))  # Expected Output: 3

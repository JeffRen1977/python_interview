from typing import List
from collections import deque


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # Initialize a deque to store indices and their respective prefix sums
        q = deque()
        q.append((-1, 0))  # Start with (-1, 0) for easier subarray calculations
        min_size = float("inf")  # Initialize minimum size to infinity
        cumsum = 0  # Cumulative sum for the current prefix

        # Iterate through each element in the array
        for j in range(len(A)):
            cumsum += A[j]  # Update cumulative sum with the current element

            # Check if there's any valid subarray by comparing cumsum and deque's front
            while q and cumsum - q[0][1] >= K:
                min_size = min(min_size, j - q[0][0])  # Update minimum subarray length
                q.popleft()  # Remove the element from the front of the deque

            # Maintain monotonicity by removing elements from the back
            while q and q[-1][1] >= cumsum:
                q.pop()

            # Add the current index and cumulative sum to the deque
            q.append((j, cumsum))

        # If min_size is still infinity, it means no valid subarray was found
        return -1 if min_size == float("inf") else min_size


def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    test_cases = [
        ([84, -37, 32, 40, 95], 167, 3),  # Expected output: 3
        ([2, -1, 2], 3, 3),  # Expected output: 3
        ([1, 2], 4, -1),  # Expected output: -1
        ([1], 1, 1),  # Expected output: 1
        ([1, 2, 3, 4, 5], 15, 5),  # Expected output: 5
        ([1, -1, 6, -1, 2, 5], 7, 2),  # Expected output: 2
        ([84, 10, -10, 70, 20], 100, 2)  # Expected output: 2
    ]

    # Run test cases
    all_passed = True
    for i, (A, K, expected) in enumerate(test_cases):
        result = solution.shortestSubarray(A, K)
        if result != expected:
            print(f"Test case {i + 1} failed: Input (A={A}, K={K}) - Expected {expected}, got {result}")
            all_passed = False
        else:
            print(f"Test case {i + 1} passed.")

    if all_passed:
        print("All test cases passed!")


if __name__ == "__main__":
    main()

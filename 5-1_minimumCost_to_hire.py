from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        # Step 1: Calculate the wage-to-quality ratio and pair it with each worker's quality.
        wq = sorted([(w / q, q) for w, q in zip(wage, quality)])  # Sort by ratio

        # Initialize the result with infinity (as we want the minimum).
        res = float('inf')

        # Initialize a max-heap to keep track of the highest quality workers in the group.
        heap = []
        qSum = 0  # Sum of qualities of current K workers

        # Step 2: Iterate over the sorted list and form groups of size K
        for ratio, q in wq:
            # Add the current worker's quality to the sum and push it to the heap (negated to simulate max-heap)
            qSum += q
            heapq.heappush(heap, -q)

            # If we exceed the number of K workers, remove the worker with the highest quality
            if len(heap) > K:
                qSum += heapq.heappop(
                    heap)  # `heapq.heappop(heap)` returns the smallest (negative) quality, so we add it to `qSum`

            # If we have exactly K workers, calculate the minimum cost for this configuration
            if len(heap) == K:
                res = min(res, ratio * qSum)

        # Return the minimum cost found
        return res


def main():
    # Create a Solution object
    sol = Solution()

    # Example 1
    quality1 = [10, 20, 5]
    wage1 = [70, 50, 30]
    K1 = 2
    output1 = sol.mincostToHireWorkers(quality1, wage1, K1)
    print(f"Minimum cost for example 1: {output1:.5f}")  # Expected output: 105.00000

    # Example 2
    quality2 = [3, 1, 10, 1, 1]
    wage2 = [4, 8, 2, 2, 7]
    K2 = 3
    output2 = sol.mincostToHireWorkers(quality2, wage2, K2)
    print(f"Minimum cost for example 2: {output2:.5f}")  # Expected output: 30.66667


main()

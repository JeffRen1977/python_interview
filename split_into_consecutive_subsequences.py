from typing import List
import heapq


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Step 1: Initialize the hash table for min-heaps.
        heaps = {}

        # Step 2: Populate the heaps dictionary with empty lists for all elements in nums.
        # This will store min-heaps for sequences ending at each integer.
        for n in range(nums[0] - 1, nums[-1] + 1):
            heaps[n] = []

        # Step 3: Process each number in the array.
        for n in nums:
            if heaps[n - 1]:
                # If there is a subsequence ending at n-1, extend it by adding n.
                length = heapq.heappop(heaps[n - 1]) + 1
            else:
                # Otherwise, start a new subsequence of length 1.
                length = 1
            # Push the updated subsequence length into the min-heap for subsequences ending at n.
            heapq.heappush(heaps[n], length)

        # Step 4: Check if all subsequences have a length of at least 3.
        for n in nums:
            if heaps[n] and heaps[n][0] < 3:
                return False
        return True


def main():
    # Create a Solution object
    sol = Solution()

    # Example 1
    nums1 = [1, 2, 3, 3, 4, 5]
    output1 = sol.isPossible(nums1)
    print(f"Is it possible to split array {nums1} into consecutive subsequences? {output1}")  # Expected output: True

    # Additional Example 2
    nums2 = [1, 2, 3, 4, 4, 5, 6]
    output2 = sol.isPossible(nums2)
    print(f"Is it possible to split array {nums2} into consecutive subsequences? {output2}")  # Expected output: False

    # Additional Example 3
    nums3 = [1, 2, 3, 4, 5, 6]
    output3 = sol.isPossible(nums3)
    print(f"Is it possible to split array {nums3} into consecutive subsequences? {output3}")  # Expected output: True


main()

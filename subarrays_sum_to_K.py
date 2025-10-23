from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to store the frequency of each prefix sum
        table = defaultdict(int)
        # Initialize result and prefix sum
        res = 0
        presum = 0
        # Initialize with a prefix sum of zero
        table[0] = 1

        # Traverse each element in nums
        for num in nums:
            # Update prefix sum
            presum += num
            # If (presum - k) is in the table, add its count to the result
            if presum - k in table:
                res += table[presum - k]
            # Update the frequency of the current prefix sum
            table[presum] += 1

        return res


def main():
    # Test Case 1
    nums1 = [1, 1, 1]
    k1 = 2
    solution = Solution()
    result1 = solution.subarraySum(nums1, k1)
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {result1}")
    print(f"Expected Output: 2\n")

    # Test Case 2: Mixed positive and negative numbers
    nums2 = [1, 2, 3, -2, 1, 4]
    k2 = 5
    result2 = solution.subarraySum(nums2, k2)
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {result2}")
    print(f"Expected Output: 3\n")

    # Test Case 3: All elements are zeros
    nums3 = [0, 0, 0, 0]
    k3 = 0
    result3 = solution.subarraySum(nums3, k3)
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {result3}")
    print(f"Expected Output: 10\n")

    # Test Case 4: Array with both positive and negative numbers
    nums4 = [-1, -1, 1]
    k4 = 0
    result4 = solution.subarraySum(nums4, k4)
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Output: {result4}")
    print(f"Expected Output: 1\n")

    # Test Case 5: No subarrays with sum k
    nums5 = [1, 2, 3]
    k5 = 7
    result5 = solution.subarraySum(nums5, k5)
    print(f"Input: nums = {nums5}, k = {k5}")
    print(f"Output: {result5}")
    print(f"Expected Output: 0\n")


main()

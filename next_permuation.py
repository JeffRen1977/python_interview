from typing import List

def find_pivot(nums: List[int]) -> int:
    m = nums[-1]
    i = len(nums) - 2
    while i >= 0 and nums[i] >= m:
        m = nums[i]
        i -= 1
    return i

def find_successor(nums: List[int], pivot: int) -> int:
    j = len(nums) - 1
    while nums[pivot] >= nums[j]:
        j -= 1
    assert j > pivot
    return j

def reverse(arr: List[int], start: int, end: int) -> None:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return
        # Locate the first index that fell
        i = find_pivot(nums)
        if i < 0:
            nums.sort()
        else:
            # Find the index j where the value is larger than nums[i] after index i
            j = find_successor(nums, i)
            # Swap the numbers at index positions i and j
            nums[i], nums[j] = nums[j], nums[i]
            # Array sorting after index position i
            reverse(nums, i + 1, len(nums) - 1)

# Main function to test the code
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 3],
        [3, 2, 1],
        [1, 1, 5],
        [1, 5, 8, 4, 7, 6, 5, 3, 1],
        [1, 3, 2]
    ]

    solution = Solution()
    for nums in test_cases:
        print("Original array:", nums)
        solution.nextPermutation(nums)
        print("Next permutation:", nums)

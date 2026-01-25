from typing import List

"""
Next Permutation Algorithm (LeetCode 31)

Problem: Find the next lexicographically greater permutation of an array.
If no greater permutation exists, rearrange to the smallest permutation (ascending order).

Algorithm Approach:
1. Find the pivot: rightmost index where nums[i] < nums[i+1]
   - This is the rightmost position we can increase
   - Everything to the right is in descending order
2. If no pivot found: array is descending → reverse to ascending
3. If pivot found:
   a. Find successor: smallest element to the right of pivot that's > nums[pivot]
   b. Swap pivot and successor
   c. Reverse suffix after pivot to get lexicographically smallest arrangement

Time Complexity: O(N) where N = array length
Space Complexity: O(1) - in-place modification
"""


def find_pivot(nums: List[int]) -> int:
    """
    Find the rightmost index where nums[i] < nums[i+1].
    This is the pivot point - the rightmost position we can increase.
    
    Args:
        nums: Input array
    
    Returns:
        Index of pivot, or -1 if array is in descending order (no pivot found)
    
    Algorithm:
        - Start from the second-to-last element
        - Move left while elements are in descending order (nums[i] >= nums[i+1])
        - Return the first index where we find an increase (nums[i] < nums[i+1])
    
    Example:
        [1, 5, 8, 4, 7, 6, 5, 3, 1]
        Pivot at index 3 (value 4), because 4 < 7
        Everything after index 3 is descending: [7, 6, 5, 3, 1]
    """
    # Start with the last element as the reference
    m = nums[-1]
    # Start checking from the second-to-last element
    i = len(nums) - 2
    
    # Move left while elements are in descending order
    # We're looking for the first position where nums[i] < nums[i+1]
    while i >= 0 and nums[i] >= m:
        # Update reference to current element
        m = nums[i]
        # Move to previous position
        i -= 1
    
    # Return pivot index, or -1 if no pivot found (array is descending)
    return i


def find_successor(nums: List[int], pivot: int) -> int:
    """
    Find the smallest element to the right of pivot that's larger than nums[pivot].
    This element will be swapped with the pivot to get the next permutation.
    
    Args:
        nums: Input array
        pivot: Index of the pivot element
    
    Returns:
        Index of the successor element
    
    Algorithm:
        - Start from the rightmost element
        - Move left while elements are <= nums[pivot]
        - The first element > nums[pivot] is the successor
        - This is the smallest element larger than pivot (since we scan from right)
    
    Example:
        nums = [1, 5, 8, 4, 7, 6, 5, 3, 1], pivot = 3 (value 4)
        Elements to the right: [7, 6, 5, 3, 1]
        Elements > 4: [7, 6, 5]
        Smallest: 5 at index 6
    """
    # Start from the rightmost element
    j = len(nums) - 1
    
    # Move left while elements are <= nums[pivot]
    # We want the smallest element that's > nums[pivot]
    # Since we scan from right, the first element > nums[pivot] is the smallest
    while nums[pivot] >= nums[j]:
        j -= 1
    
    # Assertion: successor must be to the right of pivot
    assert j > pivot
    
    return j


def reverse(arr: List[int], start: int, end: int) -> None:
    """
    Reverse a subarray in-place from index start to end (inclusive).
    
    Args:
        arr: Array to modify
        start: Starting index (inclusive)
        end: Ending index (inclusive)
    
    Algorithm:
        - Swap elements from both ends moving towards center
        - Continue until start >= end
    
    Example:
        arr = [1, 2, 3, 4, 5], start = 1, end = 3
        After reverse: [1, 4, 3, 2, 5]
    """
    # Swap elements from both ends, moving towards center
    while start < end:
        # Swap elements at start and end positions
        arr[start], arr[end] = arr[end], arr[start]
        # Move pointers towards center
        start += 1
        end -= 1


class Solution:
    """
    Solution class for Next Permutation problem.
    
    The algorithm modifies the array in-place to get the next lexicographically
    greater permutation, or the smallest permutation if no greater one exists.
    """
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Rearrange numbers into the lexicographically next greater permutation.
        Modifies the array in-place.
        
        Args:
            nums: List of integers to rearrange (modified in-place)
        
        Algorithm Steps:
            1. Find pivot: rightmost index where we can increase value
            2. If no pivot: array is descending → reverse to ascending
            3. If pivot found:
               a. Find successor: smallest element > pivot to the right
               b. Swap pivot and successor
               c. Reverse suffix after pivot to get smallest arrangement
        
        Example:
            Input:  [1, 2, 3]
            Output: [1, 3, 2]  (next lexicographically greater)
            
            Input:  [3, 2, 1]
            Output: [1, 2, 3]  (no greater permutation, return smallest)
        """
        # Edge case: arrays with 0 or 1 element don't need processing
        if len(nums) < 2:
            return
        
        # Step 1: Find the pivot point
        # Pivot is the rightmost index where nums[i] < nums[i+1]
        # This is the rightmost position we can increase
        i = find_pivot(nums)
        
        if i < 0:
            # No pivot found: array is in descending order
            # No greater permutation exists, so return the smallest permutation
            # Sort (or reverse) to get ascending order
            nums.sort()  # Could also use nums.reverse() since it's already descending
        else:
            # Step 2: Find the successor
            # Successor is the smallest element to the right of pivot that's > nums[i]
            # This ensures we get the next permutation, not a later one
            j = find_successor(nums, i)
            
            # Step 3: Swap pivot and successor
            # This increases the value at position i to the smallest possible larger value
            nums[i], nums[j] = nums[j], nums[i]
            
            # Step 4: Reverse the suffix after pivot
            # After swapping, the suffix is still in descending order
            # Reversing it gives us the lexicographically smallest arrangement
            # This completes the next permutation
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

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Initialize the left (l) and right (r) boundaries of the array
        l, r = 0, len(nums) - 1
        
        # Continue searching as long as the left boundary is less than or equal to the right boundary
        while l <= r:
            # Find the middle index of the current search space
            mid = (l + r) // 2
            
            # If the target is at the mid index, return the index
            if target == nums[mid]:
                return mid
            
            # Check if the left side (from l to mid) is sorted
            if nums[l] <= nums[mid]:
                # If the target is greater than mid or less than the value at l, the target is not on the left side
                if target > nums[mid] or target < nums[l]:
                    # Move the left boundary to mid + 1 to search the right side
                    l = mid + 1
                else:
                    # Otherwise, continue searching on the left by moving the right boundary to mid - 1
                    r = mid - 1
            # If the right side (from mid to r) is sorted
            else:
                # If the target is less than mid or greater than the value at r, the target is not on the right side
                if target < nums[mid] or target > nums[r]:
                    # Move the right boundary to mid - 1 to search the left side
                    r = mid - 1
                else:
                    # Otherwise, continue searching on the right by moving the left boundary to mid + 1
                    l = mid + 1
        
        # If the target is not found in the array, return -1
        return -1


def main():
    sol = Solution()

    # Example 1: Standard rotated array
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    result1 = sol.search(nums1, target1)
    print(f"Array: {nums1}, Target: {target1}")
    print(f"Result: {result1}")  # Expected: 4
    print()

    # Example 2: Target at rotation point
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    result2 = sol.search(nums2, target2)
    print(f"Array: {nums2}, Target: {target2}")
    print(f"Result: {result2}")  # Expected: -1 (not found)
    print()

    # Example 3: Single element array
    nums3 = [1]
    target3 = 0
    result3 = sol.search(nums3, target3)
    print(f"Array: {nums3}, Target: {target3}")
    print(f"Result: {result3}")  # Expected: -1
    print()

    # Example 4: Target in left sorted portion
    nums4 = [4, 5, 6, 7, 0, 1, 2]
    target4 = 5
    result4 = sol.search(nums4, target4)
    print(f"Array: {nums4}, Target: {target4}")
    print(f"Result: {result4}")  # Expected: 1
    print()

    # Example 5: Non-rotated array (edge case)
    nums5 = [1, 2, 3, 4, 5]
    target5 = 4
    result5 = sol.search(nums5, target5)
    print(f"Array: {nums5}, Target: {target5}")
    print(f"Result: {result5}")  # Expected: 3


if __name__ == "__main__":
    main()

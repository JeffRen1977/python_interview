class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

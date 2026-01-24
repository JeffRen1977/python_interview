class SolutionDemo:
    def search(self, nums: list[int], target: int) -> int:
        print(f"\n{'='*60}")
        print(f"Searching for target {target} in array: {nums}")
        print(f"{'='*60}")
        
        # Visualize the rotated array
        self.visualize_array(nums, target)
        
        l, r = 0, len(nums) - 1
        iteration = 0
        
        print(f"\nInitial: l={l}, r={r}")
        print(f"{'─'*60}")
        
        while l <= r:
            iteration += 1
            mid = (l + r) // 2
            
            print(f"\n📍 Iteration {iteration}:")
            print(f"   l={l}, r={r}, mid={mid}")
            print(f"   nums[l]={nums[l]}, nums[mid]={nums[mid]}, nums[r]={nums[r]}")
            self.visualize_pointers(nums, l, mid, r, target)
            
            if target == nums[mid]:
                print(f"\n   ✅ FOUND! target {target} == nums[mid] {nums[mid]}")
                print(f"   Return index: {mid}")
                return mid
            
            # Check if left side is sorted
            if nums[l] <= nums[mid]:
                print(f"\n   📊 Left side is SORTED (nums[l]={nums[l]} <= nums[mid]={nums[mid]})")
                print(f"      Left portion: {nums[l:mid+1]}")
                
                if target > nums[mid] or target < nums[l]:
                    print(f"   🔍 Target {target} is NOT in left sorted portion")
                    print(f"      (target > nums[mid] OR target < nums[l])")
                    print(f"      → Search RIGHT: l = mid + 1 = {mid + 1}")
                    l = mid + 1
                else:
                    print(f"   🔍 Target {target} IS in left sorted portion")
                    print(f"      (nums[l] <= target <= nums[mid])")
                    print(f"      → Search LEFT: r = mid - 1 = {mid - 1}")
                    r = mid - 1
            else:
                print(f"\n   📊 Right side is SORTED (nums[mid]={nums[mid]} < nums[l]={nums[l]})")
                print(f"      Right portion: {nums[mid:r+1]}")
                
                if target < nums[mid] or target > nums[r]:
                    print(f"   🔍 Target {target} is NOT in right sorted portion")
                    print(f"      (target < nums[mid] OR target > nums[r])")
                    print(f"      → Search LEFT: r = mid - 1 = {mid - 1}")
                    r = mid - 1
                else:
                    print(f"   🔍 Target {target} IS in right sorted portion")
                    print(f"      (nums[mid] <= target <= nums[r])")
                    print(f"      → Search RIGHT: l = mid + 1 = {mid + 1}")
                    l = mid + 1
        
        print(f"\n   ❌ NOT FOUND! l={l} > r={r}, search space exhausted")
        print(f"   Return: -1")
        return -1
    
    def visualize_array(self, nums: list[int], target: int):
        """Visualize the rotated array structure"""
        print(f"\nArray Visualization:")
        print(f"Index:  {' '.join(f'{i:3}' for i in range(len(nums)))}")
        print(f"Value:  {' '.join(f'{v:3}' for v in nums)}")
        
        # Find rotation point
        rotation_idx = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                rotation_idx = i
                break
        
        if rotation_idx > 0:
            print(f"\n🔄 Rotation point at index {rotation_idx}")
            print(f"   Left sorted:  {nums[:rotation_idx]} (indices 0-{rotation_idx-1})")
            print(f"   Right sorted: {nums[rotation_idx:]} (indices {rotation_idx}-{len(nums)-1})")
        else:
            print(f"\n📋 Array is NOT rotated (fully sorted)")
    
    def visualize_pointers(self, nums: list[int], l: int, mid: int, r: int, target: int):
        """Visualize current pointer positions"""
        print(f"\n   Pointer visualization:")
        
        # Index row
        idx_str = "   Index:  "
        for i in range(len(nums)):
            idx_str += f"{i:4}"
        print(idx_str)
        
        # Value row
        val_str = "   Value:  "
        for v in nums:
            val_str += f"{v:4}"
        print(val_str)
        
        # Pointer row
        ptr_str = "   Ptr:    "
        for i in range(len(nums)):
            if i == l and i == mid and i == r:
                ptr_str += " LMR"
            elif i == l and i == mid:
                ptr_str += " L,M"
            elif i == mid and i == r:
                ptr_str += " M,R"
            elif i == l and i == r:
                ptr_str += " L,R"
            elif i == l:
                ptr_str += "   L"
            elif i == mid:
                ptr_str += "   M"
            elif i == r:
                ptr_str += "   R"
            else:
                ptr_str += "    "
        print(ptr_str)


def main():
    print("╔" + "═" * 58 + "╗")
    print("║" + " SEARCH IN ROTATED SORTED ARRAY - DEMO ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")
    
    sol = SolutionDemo()
    
    # Example 1: Target in right portion (after rotation point)
    print("\n" + "█" * 60)
    print("█ EXAMPLE 1: Target in right portion after rotation")
    print("█" * 60)
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    result1 = sol.search(nums1, target1)
    print(f"\n🎯 Final Result: Index {result1}")
    
    # Example 2: Target not in array
    print("\n" + "█" * 60)
    print("█ EXAMPLE 2: Target NOT in array")
    print("█" * 60)
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    result2 = sol.search(nums2, target2)
    print(f"\n🎯 Final Result: {result2} (not found)")
    
    # Example 3: Target in left sorted portion
    print("\n" + "█" * 60)
    print("█ EXAMPLE 3: Target in left sorted portion")
    print("█" * 60)
    nums3 = [4, 5, 6, 7, 0, 1, 2]
    target3 = 6
    result3 = sol.search(nums3, target3)
    print(f"\n🎯 Final Result: Index {result3}")
    
    # Example 4: Single element (found)
    print("\n" + "█" * 60)
    print("█ EXAMPLE 4: Single element array (found)")
    print("█" * 60)
    nums4 = [1]
    target4 = 1
    result4 = sol.search(nums4, target4)
    print(f"\n🎯 Final Result: Index {result4}")
    
    # Example 5: Non-rotated array
    print("\n" + "█" * 60)
    print("█ EXAMPLE 5: Non-rotated (fully sorted) array")
    print("█" * 60)
    nums5 = [1, 2, 3, 4, 5, 6, 7]
    target5 = 5
    result5 = sol.search(nums5, target5)
    print(f"\n🎯 Final Result: Index {result5}")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY OF ALL RESULTS")
    print("=" * 60)
    print(f"Example 1: nums={[4,5,6,7,0,1,2]}, target=0 → Index {result1} ✓")
    print(f"Example 2: nums={[4,5,6,7,0,1,2]}, target=3 → {result2} (not found) ✓")
    print(f"Example 3: nums={[4,5,6,7,0,1,2]}, target=6 → Index {result3} ✓")
    print(f"Example 4: nums={[1]}, target=1 → Index {result4} ✓")
    print(f"Example 5: nums={[1,2,3,4,5,6,7]}, target=5 → Index {result5} ✓")


if __name__ == "__main__":
    main()

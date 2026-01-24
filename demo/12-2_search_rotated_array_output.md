# Search in Rotated Sorted Array

> **LeetCode 33**: Given a rotated sorted array (no duplicates), search for a target value in O(log n) time.

## Problem Description

A sorted array is rotated at some pivot point. For example:
- Original: `[0, 1, 2, 4, 5, 6, 7]`
- Rotated at pivot 4: `[4, 5, 6, 7, 0, 1, 2]`

Given the rotated array and a target, return the index of the target or -1 if not found.

---

## Key Insight

Even though the array is rotated, **at least one half is always sorted**:

```
Array: [4, 5, 6, 7, 0, 1, 2]
        ├───────┤ ├──────┤
        sorted    sorted
        (left)    (right)

When mid = 3 (value 7):
- Left half [4,5,6,7] is sorted (nums[l] <= nums[mid])
- Right half [0,1,2] is also sorted but contains the rotation point
```

---

## Algorithm Logic

```
1. Find mid point
2. Check if target == nums[mid] → found!
3. Determine which half is sorted:
   - If nums[l] <= nums[mid] → LEFT is sorted
   - Otherwise → RIGHT is sorted
4. Check if target is in the sorted half:
   - If yes → search that half
   - If no → search the other half
5. Repeat until found or search space exhausted
```

---

## Example 1: Target in Right Portion (after rotation)

**Input**: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`

### Array Structure
```
Index:   0   1   2   3   4   5   6
Value:   4   5   6   7   0   1   2
         ├───────────┤ ├─────────┤
         Left sorted   Right sorted
         
🔄 Rotation point at index 4
```

### Step-by-Step Execution

| Iter | l | r | mid | nums[mid] | Sorted Half | Target Location | Action |
|------|---|---|-----|-----------|-------------|-----------------|--------|
| 1 | 0 | 6 | 3 | 7 | Left `[4,5,6,7]` | NOT in left (0 < 4) | `l = 4` |
| 2 | 4 | 6 | 5 | 1 | Left `[0,1]` | IN left (0 ≤ 0 ≤ 1) | `r = 4` |
| 3 | 4 | 4 | 4 | 0 | — | **FOUND!** | return 4 |

### Iteration 1 Detail
```
   Index:   0   1   2   3   4   5   6
   Value:   4   5   6   7   0   1   2
   Ptr:     L           M           R

   nums[l]=4 <= nums[mid]=7 → Left side is SORTED
   Is target 0 in [4,5,6,7]? 
     - 0 < 4 (less than left boundary) → NO
   → Search RIGHT: l = mid + 1 = 4
```

### Iteration 2 Detail
```
   Index:   0   1   2   3   4   5   6
   Value:   4   5   6   7   0   1   2
   Ptr:                     L   M   R

   nums[l]=0 <= nums[mid]=1 → Left side is SORTED
   Is target 0 in [0,1]?
     - 0 <= 0 <= 1 → YES
   → Search LEFT: r = mid - 1 = 4
```

### Iteration 3 Detail
```
   Index:   0   1   2   3   4   5   6
   Value:   4   5   6   7   0   1   2
   Ptr:                    LMR

   nums[mid] = 0 = target → FOUND!
   Return index: 4
```

**Result**: `4` ✅

---

## Example 2: Target NOT in Array

**Input**: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 3`

| Iter | l | r | mid | nums[mid] | Sorted Half | Target Location | Action |
|------|---|---|-----|-----------|-------------|-----------------|--------|
| 1 | 0 | 6 | 3 | 7 | Left `[4,5,6,7]` | NOT in left (3 < 4) | `l = 4` |
| 2 | 4 | 6 | 5 | 1 | Left `[0,1]` | NOT in left (3 > 1) | `l = 6` |
| 3 | 6 | 6 | 6 | 2 | Left `[2]` | NOT in left (3 > 2) | `l = 7` |
| — | 7 | 6 | — | — | l > r | Search exhausted | return -1 |

**Result**: `-1` ✅ (not found)

---

## Example 3: Target in Left Sorted Portion

**Input**: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 6`

| Iter | l | r | mid | nums[mid] | Sorted Half | Target Location | Action |
|------|---|---|-----|-----------|-------------|-----------------|--------|
| 1 | 0 | 6 | 3 | 7 | Left `[4,5,6,7]` | IN left (4 ≤ 6 ≤ 7) | `r = 2` |
| 2 | 0 | 2 | 1 | 5 | Left `[4,5]` | NOT in left (6 > 5) | `l = 2` |
| 3 | 2 | 2 | 2 | 6 | — | **FOUND!** | return 2 |

**Result**: `2` ✅

---

## Example 4: Single Element Array

**Input**: `nums = [1]`, `target = 1`

| Iter | l | r | mid | nums[mid] | Result |
|------|---|---|-----|-----------|--------|
| 1 | 0 | 0 | 0 | 1 | **FOUND!** |

**Result**: `0` ✅

---

## Example 5: Non-Rotated Array (Edge Case)

**Input**: `nums = [1, 2, 3, 4, 5, 6, 7]`, `target = 5`

```
Array is fully sorted (no rotation)
The algorithm still works because left half is always "sorted"
```

| Iter | l | r | mid | nums[mid] | Sorted Half | Target Location | Action |
|------|---|---|-----|-----------|-------------|-----------------|--------|
| 1 | 0 | 6 | 3 | 4 | Left `[1,2,3,4]` | NOT in left (5 > 4) | `l = 4` |
| 2 | 4 | 6 | 5 | 6 | Left `[5,6]` | IN left (5 ≤ 5 ≤ 6) | `r = 4` |
| 3 | 4 | 4 | 4 | 5 | — | **FOUND!** | return 4 |

**Result**: `4` ✅

---

## Decision Tree

```
                    ┌─────────────────┐
                    │ target == nums[mid]? │
                    └─────────┬───────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                   YES                  NO
                    │                   │
                    ▼                   ▼
               ┌────────┐     ┌─────────────────────┐
               │ FOUND! │     │ nums[l] <= nums[mid]? │
               │return mid│   └──────────┬──────────┘
               └────────┘              │
                              ┌────────┴────────┐
                              │                 │
                             YES               NO
                        (Left sorted)     (Right sorted)
                              │                 │
                              ▼                 ▼
                    ┌──────────────┐   ┌──────────────┐
                    │target in left?│  │target in right?│
                    │nums[l]<=t<=mid│  │mid<=t<=nums[r]│
                    └──────┬───────┘   └──────┬───────┘
                           │                  │
                    ┌──────┴──────┐    ┌──────┴──────┐
                   YES           NO   YES           NO
                    │             │    │             │
                    ▼             ▼    ▼             ▼
                r = mid-1    l = mid+1  l = mid+1   r = mid-1
               (go left)    (go right) (go right)  (go left)
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(log n) | Binary search halves the search space each iteration |
| **Space** | O(1) | Only uses a few pointer variables |

---

## Summary Table

| Example | Array | Target | Result | Iterations |
|---------|-------|--------|--------|------------|
| 1 | `[4,5,6,7,0,1,2]` | 0 | 4 ✅ | 3 |
| 2 | `[4,5,6,7,0,1,2]` | 3 | -1 ✅ | 3 |
| 3 | `[4,5,6,7,0,1,2]` | 6 | 2 ✅ | 3 |
| 4 | `[1]` | 1 | 0 ✅ | 1 |
| 5 | `[1,2,3,4,5,6,7]` | 5 | 4 ✅ | 3 |

---

## Source Code

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # Found target
            if target == nums[mid]:
                return mid
            
            # Check if left side is sorted
            if nums[l] <= nums[mid]:
                # Target in left sorted portion?
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1  # Search right
                else:
                    r = mid - 1  # Search left
            # Right side is sorted
            else:
                # Target in right sorted portion?
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1  # Search left
                else:
                    l = mid + 1  # Search right
        
        return -1  # Not found
```

---

## Common Mistakes to Avoid

1. **Forgetting `=` in `nums[l] <= nums[mid]`**
   - Without `=`, fails when `l == mid` (e.g., two-element arrays)

2. **Wrong boundary check for target**
   - Must check BOTH boundaries: `target >= nums[l]` AND `target <= nums[mid]`

3. **Infinite loop**
   - Always move `l` or `r` by at least 1 (`mid + 1` or `mid - 1`)

---

## Related Problems

- **LeetCode 81**: Search in Rotated Sorted Array II (with duplicates)
- **LeetCode 153**: Find Minimum in Rotated Sorted Array
- **LeetCode 154**: Find Minimum in Rotated Sorted Array II

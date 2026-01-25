# Next Permutation

> **LeetCode 31**: Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. If such arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

## Problem Description

Find the next lexicographically greater permutation of an array of integers.

**Rules:**
- If a next greater permutation exists, rearrange in-place to that permutation
- If no greater permutation exists (array is in descending order), rearrange to the smallest permutation (ascending order)
- Must modify the array in-place and use only constant extra memory

**Example:**
- Input: `[1, 2, 3]`
- Output: `[1, 3, 2]` (next lexicographically greater permutation)

**Lexicographic Order:**
- Similar to dictionary order
- Compare elements from left to right
- First differing element determines order

---

## Key Insight

**Algorithm Steps:**
1. **Find Pivot**: Find the rightmost index `i` where `nums[i] < nums[i+1]`
   - This is the first position from right where we can make a larger permutation
2. **Find Successor**: If pivot exists, find the smallest element to the right of pivot that's larger than `nums[i]`
3. **Swap**: Swap pivot with successor
4. **Reverse Suffix**: Reverse the suffix after pivot to get the lexicographically smallest arrangement

**Why This Works:**
- To get the next permutation, we need to increase the value at the rightmost position possible
- The pivot is the rightmost position we can increase
- After swapping, the suffix is in descending order, so reversing it gives the smallest arrangement

---

## Algorithm Logic

```
1. Find pivot (rightmost index where nums[i] < nums[i+1]):
   - Start from end, find first decreasing element
   - If no pivot found → array is descending → reverse entire array

2. If pivot found:
   a. Find successor (smallest element > nums[pivot] to the right)
   b. Swap pivot and successor
   c. Reverse suffix after pivot

3. Result: Next lexicographically greater permutation
```

---

## Detailed Example 1: Step-by-Step

**Input**: `nums = [1, 2, 3]`

### Visual Representation

```
Current: [1, 2, 3]
Next:    [1, 3, 2]

Lexicographic order:
  1. [1, 2, 3]
  2. [1, 3, 2]  ← Next
  3. [2, 1, 3]
  4. [2, 3, 1]
  5. [3, 1, 2]
  6. [3, 2, 1]
```

### Step-by-Step Execution

#### Step 1: Find Pivot

```
Call: find_pivot([1, 2, 3])

Initialize:
  m = nums[-1] = nums[2] = 3
  i = len(nums) - 2 = 3 - 2 = 1

Iteration 1 (i = 1):
  Check: nums[1] >= m?
    nums[1] = 2
    m = 3
    2 >= 3? NO ❌
  
  Exit loop
  Return i = 1
```

**Pivot found at index 1** (value = 2)

#### Step 2: Find Successor

```
Call: find_successor([1, 2, 3], pivot=1)

Initialize:
  j = len(nums) - 1 = 2

Iteration 1 (j = 2):
  Check: nums[pivot] >= nums[j]?
    nums[1] = 2
    nums[2] = 3
    2 >= 3? NO ❌
  
  Exit loop
  Return j = 2
```

**Successor found at index 2** (value = 3)

#### Step 3: Swap Pivot and Successor

```
nums[1], nums[2] = nums[2], nums[1]
nums = [1, 3, 2]
```

#### Step 4: Reverse Suffix

```
Call: reverse([1, 3, 2], start=2, end=2)

Suffix after pivot (index 1) is from index 2 to 2
  start = 2, end = 2
  start < end? 2 < 2? NO
  
  No reversal needed (single element)
```

**Result**: `[1, 3, 2]` ✅

---

## Detailed Example 2: Complex Case

**Input**: `nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]`

### Step-by-Step Execution

#### Step 1: Find Pivot

```
Call: find_pivot([1, 5, 8, 4, 7, 6, 5, 3, 1])

Initialize:
  m = nums[-1] = 1
  i = len(nums) - 2 = 7

Iteration 1 (i = 7):
  nums[7] = 3, m = 1
  3 >= 1? YES ✅
    m = 3
    i = 6

Iteration 2 (i = 6):
  nums[6] = 5, m = 3
  5 >= 3? YES ✅
    m = 5
    i = 5

Iteration 3 (i = 5):
  nums[5] = 6, m = 5
  6 >= 5? YES ✅
    m = 6
    i = 4

Iteration 4 (i = 4):
  nums[4] = 7, m = 6
  7 >= 6? YES ✅
    m = 7
    i = 3

Iteration 5 (i = 3):
  nums[3] = 4, m = 7
  4 >= 7? NO ❌
  
  Exit loop
  Return i = 3
```

**Pivot found at index 3** (value = 4)

**Visual:**
```
Index:  0  1  2  3  4  5  6  7  8
Array: [1, 5, 8, 4, 7, 6, 5, 3, 1]
                ↑
              Pivot
```

#### Step 2: Find Successor

```
Call: find_successor([1, 5, 8, 4, 7, 6, 5, 3, 1], pivot=3)

Initialize:
  j = len(nums) - 1 = 8

Iteration 1 (j = 8):
  nums[3] = 4, nums[8] = 1
  4 >= 1? YES ✅
    j = 7

Iteration 2 (j = 7):
  nums[3] = 4, nums[7] = 3
  4 >= 3? YES ✅
    j = 6

Iteration 3 (j = 6):
  nums[3] = 4, nums[6] = 5
  4 >= 5? NO ❌
  
  Exit loop
  Return j = 6
```

**Successor found at index 6** (value = 5)

**Visual:**
```
Index:  0  1  2  3  4  5  6  7  8
Array: [1, 5, 8, 4, 7, 6, 5, 3, 1]
                ↑           ↑
              Pivot      Successor
```

#### Step 3: Swap Pivot and Successor

```
nums[3], nums[6] = nums[6], nums[3]
nums = [1, 5, 8, 5, 7, 6, 4, 3, 1]
```

**After swap:**
```
Index:  0  1  2  3  4  5  6  7  8
Array: [1, 5, 8, 5, 7, 6, 4, 3, 1]
                ↑
              Swapped
```

#### Step 4: Reverse Suffix

```
Call: reverse([1, 5, 8, 5, 7, 6, 4, 3, 1], start=4, end=8)

Suffix after pivot (index 3) is from index 4 to 8
  Original suffix: [7, 6, 4, 3, 1]  (descending)
  Need to reverse to: [1, 3, 4, 6, 7]  (ascending)

Iteration 1:
  start=4, end=8
  start < end? 4 < 8? YES
    Swap nums[4] and nums[8]
    nums = [1, 5, 8, 5, 1, 6, 4, 3, 7]
    start=5, end=7

Iteration 2:
  start=5, end=7
  start < end? 5 < 7? YES
    Swap nums[5] and nums[7]
    nums = [1, 5, 8, 5, 1, 3, 4, 6, 7]
    start=6, end=6

Iteration 3:
  start=6, end=6
  start < end? 6 < 6? NO
    Exit loop
```

**Result**: `[1, 5, 8, 5, 1, 3, 4, 6, 7]` ✅

**Verification:**
- Original: `[1, 5, 8, 4, 7, 6, 5, 3, 1]`
- Next: `[1, 5, 8, 5, 1, 3, 4, 6, 7]`
- This is the lexicographically next greater permutation!

---

## Detailed Example 3: Descending Order (No Next Permutation)

**Input**: `nums = [3, 2, 1]`

### Step-by-Step Execution

#### Step 1: Find Pivot

```
Call: find_pivot([3, 2, 1])

Initialize:
  m = nums[-1] = 1
  i = len(nums) - 2 = 1

Iteration 1 (i = 1):
  nums[1] = 2, m = 1
  2 >= 1? YES ✅
    m = 2
    i = 0

Iteration 2 (i = 0):
  nums[0] = 3, m = 2
  3 >= 2? YES ✅
    m = 3
    i = -1

i = -1
Return i = -1
```

**No pivot found** (i < 0)

#### Step 2: Sort Array (Reverse)

```
Since i < 0, array is in descending order
Call: nums.sort()
nums = [1, 2, 3]
```

**Result**: `[1, 2, 3]` ✅ (smallest permutation)

---

## Detailed Example 4: With Duplicates

**Input**: `nums = [1, 1, 5]`

### Step-by-Step Execution

#### Step 1: Find Pivot

```
Call: find_pivot([1, 1, 5])

Initialize:
  m = nums[-1] = 5
  i = len(nums) - 2 = 1

Iteration 1 (i = 1):
  nums[1] = 1, m = 5
  1 >= 5? NO ❌
  
  Exit loop
  Return i = 1
```

**Pivot found at index 1** (value = 1)

#### Step 2: Find Successor

```
Call: find_successor([1, 1, 5], pivot=1)

Initialize:
  j = len(nums) - 1 = 2

Iteration 1 (j = 2):
  nums[1] = 1, nums[2] = 5
  1 >= 5? NO ❌
  
  Exit loop
  Return j = 2
```

**Successor found at index 2** (value = 5)

#### Step 3: Swap and Reverse

```
Swap: nums[1], nums[2] = nums[2], nums[1]
nums = [1, 5, 1]

Reverse suffix (index 2 to 2): No change
```

**Result**: `[1, 5, 1]` ✅

---

## Key Concepts

### 1. Lexicographic Order

**Definition**: Dictionary-like ordering
- Compare elements from left to right
- First differing element determines order
- Shorter sequences come before longer ones (if prefix matches)

**Example:**
```
[1, 2, 3] < [1, 3, 2] < [2, 1, 3] < [2, 3, 1] < [3, 1, 2] < [3, 2, 1]
```

### 2. Pivot Point

**Definition**: Rightmost index where `nums[i] < nums[i+1]`

**Why it matters:**
- Everything to the right of pivot is in descending order
- This is the rightmost position we can increase
- Increasing any position to the left would give a smaller permutation

**Visual:**
```
[1, 5, 8, 4, 7, 6, 5, 3, 1]
        ↑
      Pivot (4 < 7)
      Everything after is descending: [7, 6, 5, 3, 1]
```

### 3. Successor

**Definition**: Smallest element to the right of pivot that's larger than `nums[pivot]`

**Why smallest?**
- We want the next permutation, not just any larger one
- The smallest larger element ensures we get the lexicographically next permutation

**Example:**
```
Pivot = 4 at index 3
Elements to the right: [7, 6, 5, 3, 1]
Elements > 4: [7, 6, 5]
Smallest: 5
```

### 4. Why Reverse Suffix?

**After swapping pivot and successor:**
- The suffix is still in descending order
- To get the lexicographically smallest arrangement, we reverse it
- This gives us the next permutation

**Example:**
```
After swap: [1, 5, 8, 5, 7, 6, 4, 3, 1]
Suffix: [7, 6, 4, 3, 1]  (descending)
Reverse: [1, 3, 4, 6, 7]  (ascending - smallest)
Result: [1, 5, 8, 5, 1, 3, 4, 6, 7]
```

### 5. Edge Case: Descending Order

**When array is in descending order:**
- No pivot found (i < 0)
- This means no greater permutation exists
- Reverse entire array to get smallest permutation

**Example:**
```
[3, 2, 1] → No pivot → Reverse → [1, 2, 3]
```

---

## Algorithm Pseudocode

```python
def nextPermutation(nums):
    if len(nums) < 2:
        return
    
    # Step 1: Find pivot
    pivot = find_pivot(nums)
    
    if pivot < 0:
        # Array is descending, reverse to ascending
        nums.reverse()
    else:
        # Step 2: Find successor
        successor = find_successor(nums, pivot)
        
        # Step 3: Swap
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        
        # Step 4: Reverse suffix
        reverse(nums, pivot + 1, len(nums) - 1)

def find_pivot(nums):
    m = nums[-1]
    i = len(nums) - 2
    while i >= 0 and nums[i] >= m:
        m = nums[i]
        i -= 1
    return i

def find_successor(nums, pivot):
    j = len(nums) - 1
    while nums[pivot] >= nums[j]:
        j -= 1
    return j

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(N) | N = array length. Find pivot O(N), find successor O(N), reverse O(N) |
| **Space** | O(1) | Only constant extra space used (in-place modification) |

**Where:**
- N = length of array

**Time Complexity Breakdown:**
- `find_pivot`: O(N) - scans from right to left
- `find_successor`: O(N) - scans from right to left
- `reverse`: O(N) - reverses suffix
- Total: O(N)

**Space Complexity:**
- No additional arrays
- Only a few variables (i, j, m, start, end)
- O(1) space

---

## Edge Cases

### Case 1: Single Element
```
nums = [1]
Result: [1] (no change)
```

### Case 2: Two Elements
```
nums = [1, 2]
Result: [2, 1] (swap)
```

### Case 3: Descending Order
```
nums = [3, 2, 1]
Result: [1, 2, 3] (reverse)
```

### Case 4: Ascending Order
```
nums = [1, 2, 3]
Result: [1, 3, 2] (next permutation)
```

### Case 5: With Duplicates
```
nums = [1, 1, 5]
Result: [1, 5, 1] (handles duplicates correctly)
```

### Case 6: All Same Elements
```
nums = [1, 1, 1]
Result: [1, 1, 1] (no change, already largest)
```

---

## Why This Algorithm Works

### Correctness

1. **Pivot is Correct:**
   - Rightmost position where we can increase value
   - Everything to the right is in descending order
   - This is the optimal position to modify

2. **Successor is Correct:**
   - Smallest element larger than pivot
   - Ensures we get the next permutation, not a later one

3. **Reverse is Correct:**
   - After swap, suffix is still descending
   - Reversing gives the lexicographically smallest arrangement
   - This completes the next permutation

### Why Right-to-Left?

**We scan from right to left because:**
- We want to change the rightmost position possible
- This gives us the smallest increase
- Changing left positions would give larger permutations (not next)

### Why Reverse, Not Sort?

**After swapping:**
- The suffix is in descending order
- Reversing is O(N) and gives ascending order
- Sorting would also work but is O(N log N)
- Reverse is more efficient and sufficient

---

## Alternative Approaches

### 1. Generate All Permutations

**Idea**: Generate all permutations, find current, return next

**Pros:** Simple conceptually
**Cons:** O(N!) time, O(N!) space - very inefficient

### 2. Use Built-in Functions

**Python:**
```python
from itertools import permutations
# Generate all permutations, find next
```

**Pros:** Simple
**Cons:** O(N!) time and space

### 3. Recursive Approach

**Idea**: Recursively find next permutation

**Pros:** More intuitive
**Cons:** O(N!) worst case, more complex

---

## Visual Timeline

### Example: `[1, 5, 8, 4, 7, 6, 5, 3, 1]`

```
Step | Action                    | Array State
-----|---------------------------|------------------------------------------
0    | Original                 | [1, 5, 8, 4, 7, 6, 5, 3, 1]
1    | Find pivot (i=3, val=4)  | [1, 5, 8, 4, 7, 6, 5, 3, 1]
2    | Find successor (j=6)     | [1, 5, 8, 4, 7, 6, 5, 3, 1]
3    | Swap pivot & successor   | [1, 5, 8, 5, 7, 6, 4, 3, 1]
4    | Reverse suffix [4:8]     | [1, 5, 8, 5, 1, 3, 4, 6, 7]
5    | Result                   | [1, 5, 8, 5, 1, 3, 4, 6, 7] ✅
```

---

## Real-World Applications

1. **Combinatorics:**
   - Generating permutations in order
   - Combinatorial algorithms

2. **Password Generation:**
   - Systematic password generation
   - Brute force attacks

3. **Game Development:**
   - Puzzle games
   - Arrangement problems

4. **Data Analysis:**
   - Exploring all arrangements
   - Optimization problems

---

## Common Mistakes

### Mistake 1: Wrong Pivot Condition

```python
# WRONG: Using > instead of >=
while i >= 0 and nums[i] > m:  # Misses equal elements!
```

**Fix:** Use `>=` to handle duplicates correctly

### Mistake 2: Not Reversing Suffix

```python
# WRONG: Forgetting to reverse
nums[i], nums[j] = nums[j], nums[i]
# Missing: reverse(nums, i+1, len(nums)-1)
```

**Fix:** Always reverse suffix after swap

### Mistake 3: Wrong Successor Search

```python
# WRONG: Finding largest instead of smallest
j = max(range(i+1, len(nums)), key=lambda x: nums[x])
```

**Fix:** Find smallest element > pivot (rightmost that's larger)

### Mistake 4: Not Handling Descending Case

```python
# WRONG: Not checking if pivot < 0
if pivot >= 0:  # Should handle descending case!
```

**Fix:** Check `if pivot < 0` and reverse entire array

---

## Summary

The next permutation algorithm:
- Finds the **pivot** (rightmost decreasing position)
- Finds the **successor** (smallest larger element to the right)
- **Swaps** pivot and successor
- **Reverses** suffix to get lexicographically smallest arrangement
- Time complexity: **O(N)**
- Space complexity: **O(1)**

**Key Insight**: To get the next permutation, increase the value at the rightmost position possible, then arrange the suffix in the smallest possible way (ascending order).

---

## Related Problems

- **LeetCode 31**: Next Permutation (this problem)
- **LeetCode 46**: Permutations (generate all permutations)
- **LeetCode 47**: Permutations II (with duplicates)
- **LeetCode 60**: Permutation Sequence (kth permutation)
- **LeetCode 556**: Next Greater Element III (similar concept)

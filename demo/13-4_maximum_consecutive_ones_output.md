# Maximum Consecutive Ones (with K Flips)

> **LeetCode 1004**: Given a binary array `A` and an integer `K`, return the maximum number of consecutive 1's in the array if you can flip at most `K` zeros.

## Problem Description

Find the longest subarray containing only 1's after flipping at most `K` zeros to 1's.

**Example:**
- `A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]`, `K = 2`
- Answer: `6` (flip two zeros in the middle to get `[1, 1, 1, 1, 1, 1]`)

---

## Key Insight

This is a **sliding window** problem where:
- We want the **longest subarray with at most K zeros**
- Zeros can be "flipped" to ones (counted as flips)
- Use two pointers to maintain a valid window

**Strategy**: Expand window (move right), shrink window (move left) when zeros exceed K.

---

## Algorithm Logic

```
1. Initialize:
   - left, right = 0, 0 (window boundaries)
   - flip = 0 (count of zeros in current window)
   - max_len = -1 (maximum valid window length)

2. For each right pointer position:
   a. If A[right] == 0:
      * Increment flip count
   b. While flip > K:
      * Shrink window from left
      * If A[left] == 0: decrement flip count
      * Move left pointer
   c. Update max_len = max(max_len, window_length)

3. Return max_len
```

---

## Detailed Example: Step-by-Step

**Input**: `A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]`, `K = 2`

### Visual Representation

```
Array:  1  1  1  0  0  0  1  1  1  1  0
Index:  0  1  2  3  4  5  6  7  8  9  10

Goal: Find longest subarray with at most 2 zeros
```

### Step-by-Step Execution

| Step | right | A[right] | flip | Window | Action | max_len |
|------|-------|----------|------|--------|--------|---------|
| 0 | 0 | 1 | 0 | `[1]` | Expand | 1 |
| 1 | 1 | 1 | 0 | `[1,1]` | Expand | 2 |
| 2 | 2 | 1 | 0 | `[1,1,1]` | Expand | 3 |
| 3 | 3 | 0 | 1 | `[1,1,1,0]` | Expand | 4 |
| 4 | 4 | 0 | 2 | `[1,1,1,0,0]` | Expand | 5 |
| 5 | 5 | 0 | 3 | `[1,1,1,0,0,0]` | Shrink (flip>K) | 5 |
| 5a | 5 | 0 | 2 | `[1,1,0,0,0]` | Shrink (flip>K) | 5 |
| 5b | 5 | 0 | 1 | `[1,0,0,0]` | Shrink (flip>K) | 5 |
| 5c | 5 | 0 | 0 | `[0,0,0]` | Continue | 5 |
| 6 | 6 | 1 | 0 | `[0,0,0,1]` | Expand | 5 |
| 7 | 7 | 1 | 0 | `[0,0,0,1,1]` | Expand | 5 |
| 8 | 8 | 1 | 0 | `[0,0,0,1,1,1]` | Expand | 6 |
| 9 | 9 | 1 | 0 | `[0,0,0,1,1,1,1]` | Expand | 7 |
| 10 | 10 | 0 | 1 | `[0,0,0,1,1,1,1,0]` | Shrink (flip>K) | 7 |
| 10a | 10 | 0 | 0 | `[0,1,1,1,1,0]` | Continue | 7 |

**Final Result**: `max_len = 6` ✅

---

## Detailed Step Breakdown

### Initialization
```
A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 2

left = 0, right = 0
flip = 0
max_len = -1
```

### Steps 0-2: Expanding Window (All Ones)

**Step 0**: `right = 0`, `A[0] = 1`
```
A[right] = 1 (not zero)
flip = 0 (no change)
Window: [1] (indices 0-0)
Window length = 1
max_len = max(-1, 1) = 1
left = 0, right = 1
```

**Step 1**: `right = 1`, `A[1] = 1`
```
A[right] = 1 (not zero)
flip = 0 (no change)
Window: [1, 1] (indices 0-1)
Window length = 2
max_len = max(1, 2) = 2
left = 0, right = 2
```

**Step 2**: `right = 2`, `A[2] = 1`
```
A[right] = 1 (not zero)
flip = 0 (no change)
Window: [1, 1, 1] (indices 0-2)
Window length = 3
max_len = max(2, 3) = 3
left = 0, right = 3
```

### Steps 3-4: Adding Zeros (Still Valid)

**Step 3**: `right = 3`, `A[3] = 0`
```
A[right] = 0 → flip = 0 + 1 = 1
flip (1) <= K (2) → window is valid
Window: [1, 1, 1, 0] (indices 0-3)
Window length = 4
max_len = max(3, 4) = 4
left = 0, right = 4
```

**Step 4**: `right = 4`, `A[4] = 0`
```
A[right] = 0 → flip = 1 + 1 = 2
flip (2) <= K (2) → window is valid
Window: [1, 1, 1, 0, 0] (indices 0-4)
Window length = 5
max_len = max(4, 5) = 5
left = 0, right = 5
```

### Step 5: Exceeding K - Shrinking Window

**Step 5**: `right = 5`, `A[5] = 0`
```
A[right] = 0 → flip = 2 + 1 = 3
flip (3) > K (2) → window is INVALID, need to shrink!

Enter while loop (flip > K):
```

**Step 5a**: Shrink from left
```
A[left] = A[0] = 1 (not zero)
flip = 3 (no change)
left = 0 + 1 = 1
Window: [1, 1, 0, 0, 0] (indices 1-5)
flip (3) > K (2) → continue shrinking
```

**Step 5b**: Continue shrinking
```
A[left] = A[1] = 1 (not zero)
flip = 3 (no change)
left = 1 + 1 = 2
Window: [1, 0, 0, 0] (indices 2-5)
flip (3) > K (2) → continue shrinking
```

**Step 5c**: Remove a zero
```
A[left] = A[2] = 1 (not zero)
flip = 3 (no change)
left = 2 + 1 = 3
Window: [0, 0, 0] (indices 3-5)
flip (3) > K (2) → continue shrinking
```

**Step 5d**: Remove first zero
```
A[left] = A[3] = 0 → flip = 3 - 1 = 2
left = 3 + 1 = 4
Window: [0, 0] (indices 4-5)
flip (2) <= K (2) → exit while loop
```

**After Step 5**:
```
Window: [0, 0] (indices 4-5)
Window length = 5 - 4 + 1 = 2
max_len = max(5, 2) = 5
left = 4, right = 6
```

### Steps 6-9: Expanding Again

**Step 6**: `right = 6`, `A[6] = 1`
```
A[right] = 1 (not zero)
flip = 2 (no change)
Window: [0, 0, 1] (indices 4-6)
Window length = 3
max_len = max(5, 3) = 5
left = 4, right = 7
```

**Step 7**: `right = 7`, `A[7] = 1`
```
A[right] = 1 (not zero)
flip = 2 (no change)
Window: [0, 0, 1, 1] (indices 4-7)
Window length = 4
max_len = max(5, 4) = 5
left = 4, right = 8
```

**Step 8**: `right = 8`, `A[8] = 1`
```
A[right] = 1 (not zero)
flip = 2 (no change)
Window: [0, 0, 1, 1, 1] (indices 4-8)
Window length = 5
max_len = max(5, 5) = 5
left = 4, right = 9
```

**Step 9**: `right = 9`, `A[9] = 1`
```
A[right] = 1 (not zero)
flip = 2 (no change)
Window: [0, 0, 1, 1, 1, 1] (indices 4-9)
Window length = 6
max_len = max(5, 6) = 6  ← NEW MAXIMUM!
left = 4, right = 10
```

### Step 10: Final Zero - Shrinking Again

**Step 10**: `right = 10`, `A[10] = 0`
```
A[right] = 0 → flip = 2 + 1 = 3
flip (3) > K (2) → window is INVALID, need to shrink!

Enter while loop (flip > K):
```

**Step 10a**: Shrink from left
```
A[left] = A[4] = 0 → flip = 3 - 1 = 2
left = 4 + 1 = 5
Window: [0, 1, 1, 1, 1, 0] (indices 5-10)
flip (2) <= K (2) → exit while loop
```

**After Step 10**:
```
Window: [0, 1, 1, 1, 1, 0] (indices 5-10)
Window length = 10 - 5 + 1 = 6
max_len = max(6, 6) = 6
left = 5, right = 11 (end of array)
```

### Final Result
```
max_len = 6
Best window: indices 4-9 → [0, 0, 1, 1, 1, 1]
After flipping 2 zeros: [1, 1, 1, 1, 1, 1] ✅
```

---

## Key Concepts

### 1. Sliding Window Technique

The algorithm maintains a window `[left, right]` that always contains **at most K zeros**.

- **Expand**: Move `right` pointer to include new elements
- **Shrink**: Move `left` pointer when zeros exceed K

### 2. Why Shrink When flip > K?

When `flip > K`, the current window is invalid. We need to remove elements from the left until `flip <= K`.

**Key insight**: We remove from the left because:
- We want the **longest** valid window
- Removing from left allows us to potentially extend the window further right
- We've already considered all windows ending before the current `right`

### 3. Window Validity

A window is **valid** if `flip <= K`:
- `flip` = number of zeros in the window
- These zeros can be "flipped" to ones
- After flipping, the window contains only 1's

### 4. Why Update max_len After Shrinking?

After the while loop, the window is guaranteed to be valid (`flip <= K`). We update `max_len` to track the longest valid window we've seen so far.

---

## Visual Timeline

```
Array:  1  1  1  0  0  0  1  1  1  1  0
Index:  0  1  2  3  4  5  6  7  8  9  10

Step 4: [==========]                    Window: [1,1,1,0,0], length=5, flip=2 ✓
        l         r

Step 5: [============]                  Window: [1,1,1,0,0,0], flip=3 ✗
        l           r
        Need to shrink...

Step 5d:      [====]                    Window: [0,0], length=2, flip=2 ✓
              l    r

Step 9:      [==========]               Window: [0,0,1,1,1,1], length=6, flip=2 ✓
              l         r                ← BEST SO FAR!

Step 10:     [===========]              Window: [0,0,1,1,1,1,0], flip=3 ✗
              l          r               Need to shrink...

Step 10a:        [========]              Window: [0,1,1,1,1,0], length=6, flip=2 ✓
                  l       r
```

---

## Algorithm Pseudocode

```python
def longestOnes(A, K):
    max_len = -1
    left = 0
    flip = 0  # Count of zeros in current window
    
    for right in range(len(A)):
        # Expand window: include A[right]
        if A[right] == 0:
            flip += 1
        
        # Shrink window if invalid
        while flip > K:
            if A[left] == 0:
                flip -= 1
            left += 1
        
        # Update maximum length
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(n) | Each element is visited at most twice (by left and right pointers) |
| **Space** | O(1) | Only uses a few variables |

**Why O(n) and not O(n²)?**
- The `while` loop doesn't cause O(n²) because:
  - `left` pointer only moves forward (never backward)
  - Each element is processed at most once by `left` and once by `right`
  - Total operations: O(2n) = O(n)

---

## Edge Cases

### Case 1: All Ones
```
A = [1, 1, 1, 1, 1], K = 0
Result: 5 (no flips needed)
```

### Case 2: All Zeros
```
A = [0, 0, 0, 0], K = 2
Result: 2 (can flip 2 zeros)
```

### Case 3: K Larger Than Zeros
```
A = [0, 0, 1, 1, 0], K = 5
Result: 5 (can flip all zeros)
```

### Case 4: Single Element
```
A = [0], K = 1
Result: 1 (flip the zero)
```

### Case 5: K = 0
```
A = [1, 0, 1, 1], K = 0
Result: 2 (longest consecutive 1's without flipping)
```

---

## Why This Algorithm Works

1. **Greedy Approach**: Always try to extend the window as far right as possible
2. **Maintain Invariant**: Window always has `flip <= K` after the while loop
3. **Optimal Substructure**: The longest valid window ending at `right` is found by shrinking from left
4. **No Backtracking**: Once we move `right`, we never need to go back

---

## Alternative Interpretation

Think of it as: **"Find the longest subarray with at most K zeros"**

- Zeros in the subarray can be "flipped" to ones
- After flipping, we get consecutive 1's
- The problem is equivalent to finding the longest subarray with at most K zeros

---

## Summary

The maximum consecutive ones algorithm:
- Uses **sliding window** technique
- Maintains window with **at most K zeros**
- **Expands** window by moving right pointer
- **Shrinks** window by moving left pointer when invalid
- Time complexity: **O(n)**
- Space complexity: **O(1)**

**Key Insight**: This is equivalent to finding the longest subarray containing at most K zeros, which can be flipped to create consecutive 1's.

---

## Related Problems

- **LeetCode 424**: Longest Repeating Character Replacement
- **LeetCode 3**: Longest Substring Without Repeating Characters
- **LeetCode 209**: Minimum Size Subarray Sum
- **LeetCode 904**: Fruit Into Baskets

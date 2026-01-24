# Integer Square Root (Binary Search)

> **LeetCode 69**: Given a non-negative integer `x`, compute and return the square root of `x` rounded down to the nearest integer.

## Problem Description

Find the integer square root of a number without using built-in functions.

**Examples:**
- `sqrt(4) = 2` (perfect square)
- `sqrt(8) = 2` (since 2² = 4 ≤ 8 < 3² = 9)
- `sqrt(15) = 3` (since 3² = 9 ≤ 15 < 4² = 16)

---

## Key Insight

Since we're looking for the **largest integer n such that n² ≤ x**, we can use binary search:
- The answer must be in the range `[0, x]`
- If `mid² > x`, then `mid` is too large → search left
- If `mid² ≤ x`, then `mid` might be the answer or too small → search right

**Important**: We store `mid` as a candidate when `mid² > x`, then adjust at the end if needed.

---

## Algorithm Logic

```
1. Handle edge cases (x == 0 or x == 1)
2. Binary search in range [0, x]:
   - Calculate mid²
   - If mid² > x:
     * Store mid as candidate
     * Search left (right = mid - 1)
   - If mid² <= x:
     * Search right (left = mid + 1)
3. After loop ends:
   - If candidate² > x: return candidate - 1
   - Otherwise: return candidate
```

---

## Example 1: Perfect Square (4)

**Input**: `x = 4`

**Goal**: Find largest integer `n` such that `n² ≤ 4`

### Step-by-Step Execution

| Iter | left | right | mid | mid² | Comparison | Action | Candidate |
|------|------|-------|-----|------|------------|--------|------------|
| 1 | 0 | 4 | 2 | 4 | 4 ≤ 4 | Search right: `left = 3` | — |
| 2 | 3 | 4 | 3 | 9 | 9 > 4 | Search left: `right = 2`, store 3 | 3 |
| — | 3 | 2 | — | — | `left > right` | Loop ends | 3 |

**Final Check**: `3² = 9 > 4` → Return `3 - 1 = 2` ✅

### Detailed Iteration 1
```
   left=0, right=4, mid=2
   mid² = 2² = 4
   
   Compare: 4 vs 4
   4 <= 4 → mid might be answer or too small
   → Search RIGHT: left = mid + 1 = 3
```

### Detailed Iteration 2
```
   left=3, right=4, mid=3
   mid² = 3² = 9
   
   Compare: 9 vs 4
   9 > 4 → mid is TOO LARGE
   → Store mid=3 as candidate
   → Search LEFT: right = mid - 1 = 2
```

**Result**: `2` ✅ (since 2² = 4)

---

## Example 2: Non-Perfect Square (8)

**Input**: `x = 8`**

**Goal**: Find largest integer `n` such that `n² ≤ 8`

### Step-by-Step Execution

| Iter | left | right | mid | mid² | Comparison | Action | Candidate |
|------|------|-------|-----|------|------------|--------|------------|
| 1 | 0 | 8 | 4 | 16 | 16 > 8 | Search left: `right = 3`, store 4 | 4 |
| 2 | 0 | 3 | 1 | 1 | 1 ≤ 8 | Search right: `left = 2` | 4 |
| 3 | 2 | 3 | 2 | 4 | 4 ≤ 8 | Search right: `left = 3` | 4 |
| 4 | 3 | 3 | 3 | 9 | 9 > 8 | Search left: `right = 2`, store 3 | 3 |
| — | 3 | 2 | — | — | `left > right` | Loop ends | 3 |

**Final Check**: `3² = 9 > 8` → Return `3 - 1 = 2` ✅

### Why This Works

- We find that `3² = 9 > 8`, so 3 is too large
- The algorithm stores 3 as candidate
- After the loop, we check: `3² > 8` → return `3 - 1 = 2`
- Verification: `2² = 4 ≤ 8 < 3² = 9` ✓

**Result**: `2` ✅

---

## Example 3: Perfect Square (16)

**Input**: `x = 16`

| Iter | left | right | mid | mid² | Comparison | Action | Candidate |
|------|------|-------|-----|------|------------|--------|------------|
| 1 | 0 | 16 | 8 | 64 | 64 > 16 | Search left: `right = 7`, store 8 | 8 |
| 2 | 0 | 7 | 3 | 9 | 9 ≤ 16 | Search right: `left = 4` | 8 |
| 3 | 4 | 7 | 5 | 25 | 25 > 16 | Search left: `right = 4`, store 5 | 5 |
| 4 | 4 | 4 | 4 | 16 | 16 ≤ 16 | Search right: `left = 5` | 5 |
| — | 5 | 4 | — | — | `left > right` | Loop ends | 5 |

**Final Check**: `5² = 25 > 16` → Return `5 - 1 = 4` ✅

**Result**: `4` ✅ (since 4² = 16)

---

## Example 4: Non-Perfect Square (15)

**Input**: `x = 15`

| Iter | left | right | mid | mid² | Comparison | Action | Candidate |
|------|------|-------|-----|------|------------|--------|------------|
| 1 | 0 | 15 | 7 | 49 | 49 > 15 | Search left: `right = 6`, store 7 | 7 |
| 2 | 0 | 6 | 3 | 9 | 9 ≤ 15 | Search right: `left = 4` | 7 |
| 3 | 4 | 6 | 5 | 25 | 25 > 15 | Search left: `right = 4`, store 5 | 5 |
| 4 | 4 | 4 | 4 | 16 | 16 > 15 | Search left: `right = 3`, store 4 | 4 |
| — | 4 | 3 | — | — | `left > right` | Loop ends | 4 |

**Final Check**: `4² = 16 > 15` → Return `4 - 1 = 3` ✅

**Result**: `3` ✅ (since 3² = 9 ≤ 15 < 4² = 16)

---

## Example 5: Large Number (100)

**Input**: `x = 100`

| Iter | left | right | mid | mid² | Comparison | Action | Candidate |
|------|------|-------|-----|------|------------|--------|------------|
| 1 | 0 | 100 | 50 | 2500 | 2500 > 100 | Search left: `right = 49`, store 50 | 50 |
| 2 | 0 | 49 | 24 | 576 | 576 > 100 | Search left: `right = 23`, store 24 | 24 |
| 3 | 0 | 23 | 11 | 121 | 121 > 100 | Search left: `right = 10`, store 11 | 11 |
| 4 | 0 | 10 | 5 | 25 | 25 ≤ 100 | Search right: `left = 6` | 11 |
| 5 | 6 | 10 | 8 | 64 | 64 ≤ 100 | Search right: `left = 9` | 11 |
| 6 | 9 | 10 | 9 | 81 | 81 ≤ 100 | Search right: `left = 10` | 11 |
| 7 | 10 | 10 | 10 | 100 | 100 ≤ 100 | Search right: `left = 11` | 11 |
| — | 11 | 10 | — | — | `left > right` | Loop ends | 11 |

**Final Check**: `11² = 121 > 100` → Return `11 - 1 = 10` ✅

**Result**: `10` ✅ (since 10² = 100)

---

## Edge Cases

### Case 1: x = 0
```
if x == 0:
    return 0
```
**Result**: `0` ✅

### Case 2: x = 1
```
if x == 1:
    return 1
```
**Result**: `1` ✅

---

## Why Store Candidate When mid² > x?

The algorithm stores `mid` as a candidate when `mid² > x` because:

1. **We're looking for the largest n where n² ≤ x**
2. When `mid² > x`, we know `mid` is too large
3. But `mid - 1` might be the answer (we don't know yet)
4. By storing `mid`, we track the "first value that's too large"
5. After the loop, if `candidate² > x`, we return `candidate - 1`

**Example with x = 8:**
- We find `3² = 9 > 8` → store 3 as candidate
- After loop: `3² > 8` → return `3 - 1 = 2` ✓

---

## Decision Tree

```
                    ┌─────────────────┐
                    │   x == 0 or 1?   │
                    └─────────┬───────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                   YES                  NO
                    │                   │
                    ▼                   ▼
               ┌────────┐     ┌─────────────────┐
               │return x│     │ Binary Search   │
               └────────┘     │  in [0, x]      │
                              └────────┬────────┘
                                       │
                              ┌────────┴────────┐
                              │                 │
                              ▼                 ▼
                    ┌─────────────────┐  ┌─────────────────┐
                    │   mid² > x?     │  │   mid² <= x?     │
                    └────────┬────────┘  └────────┬────────┘
                             │                    │
                    ┌────────┴────────┐   ┌───────┴───────┐
                   YES               NO  YES              NO
                    │                 │   │               │
                    ▼                 ▼   ▼               ▼
            Store mid as      Continue   Search right   Continue
            candidate         search     (left=mid+1)    search
            Search left
            (right=mid-1)
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(log x) | Binary search halves the search space each iteration |
| **Space** | O(1) | Only uses a few variables (left, right, mid, value) |

---

## Summary Table

| Input | Result | Verification | Iterations |
|-------|--------|--------------|------------|
| 0 | 0 | Edge case | 0 |
| 1 | 1 | Edge case | 0 |
| 4 | 2 | 2² = 4 | 2 |
| 8 | 2 | 2² = 4 ≤ 8 < 3² = 9 | 4 |
| 15 | 3 | 3² = 9 ≤ 15 < 4² = 16 | 4 |
| 16 | 4 | 4² = 16 | 4 |
| 100 | 10 | 10² = 100 | 7 |

---

## Source Code

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        # Edge cases
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        left = 0
        right = x
        value = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid > x:
                # mid is too large, store as candidate
                value = mid
                right = mid - 1
            else:
                # mid might be answer or too small
                left = mid + 1
        
        # Adjust if candidate is too large
        if value * value > x:
            return value - 1
        
        return value
```

---

## Common Mistakes to Avoid

1. **Forgetting edge cases**
   - Must handle `x == 0` and `x == 1` separately

2. **Not storing candidate when mid² > x**
   - Need to track the "first value that's too large"

3. **Wrong final adjustment**
   - Must check `value² > x` before returning `value - 1`

4. **Integer overflow**
   - For very large `x`, `mid * mid` might overflow
   - Solution: Use `mid > x // mid` instead of `mid * mid > x`

---

## Alternative Implementation (Avoid Overflow)

```python
def mySqrt(self, x: int) -> int:
    if x < 2:
        return x
    
    left, right = 0, x
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        # Avoid overflow: compare mid with x // mid
        if mid <= x // mid:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

This version avoids potential integer overflow by comparing `mid` with `x // mid` instead of computing `mid * mid`.

---

## Related Problems

- **LeetCode 367**: Valid Perfect Square
- **LeetCode 50**: Pow(x, n)
- **LeetCode 441**: Arranging Coins

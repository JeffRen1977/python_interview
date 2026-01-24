# Interval Intersection

> **LeetCode 986**: Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order. Return the intersection of these two interval lists.

## Problem Description

Find all intervals that are common to both lists. The intersection of two intervals `[a, b]` and `[c, d]` is:
- Empty if `b < c` or `d < a`
- `[max(a, c), min(b, d)]` if they overlap

**Example:**
- `A = [[0, 2], [5, 10], [13, 23], [24, 25]]`
- `B = [[1, 5], [8, 12], [15, 24], [25, 26]]`
- Intersection: `[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]`

---

## Key Insight

Use **two pointers** to traverse both lists simultaneously:
- Compare intervals `A[i]` and `B[j]`
- Calculate intersection: `[max(start1, start2), min(end1, end2)]`
- If `lo <= hi`, there's an intersection
- Move the pointer of the interval with the **smaller endpoint**

**Why move the smaller endpoint?** Because that interval can't intersect with any future intervals from the other list.

---

## Algorithm Logic

```
1. Initialize two pointers i=0, j=0
2. While both pointers are in bounds:
   a. Calculate intersection:
      lo = max(A[i][0], B[j][0])
      hi = min(A[i][1], B[j][1])
   b. If lo <= hi:
      * Add [lo, hi] to result
   c. Move pointer:
      * If A[i][1] < B[j][1]: move i (A[i] ends first)
      * Else: move j (B[j] ends first or equal)
3. Return result
```

---

## Detailed Example: Step-by-Step

**Input**: 
- `A = [[0, 2], [5, 10], [13, 23], [24, 25]]`
- `B = [[1, 5], [8, 12], [15, 24], [25, 26]]`

### Visual Representation

```
Timeline:  0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26
           ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
A[0]:      [────────]
A[1]:                              [──────────────────]
A[2]:                                                                    [──────────────────────────]
A[3]:                                                                                                                      [────]

B[0]:           [──────────]
B[1]:                                    [──────────────]
B[2]:                                                                              [──────────────────────────]
B[3]:                                                                                                                         [────]

Intersections:
  A[0] ∩ B[0]:  [──]        → [1, 2]
  A[1] ∩ B[0]:         [─]  → [5, 5]
  A[1] ∩ B[1]:              [──────]  → [8, 10]
  A[2] ∩ B[2]:                              [──────────────────]  → [15, 23]
  A[3] ∩ B[2]:                                                      [─]  → [24, 24]
  A[3] ∩ B[3]:                                                         [─]  → [25, 25]
```

### Step-by-Step Execution

| Step | i | j | A[i] | B[j] | lo | hi | Intersection? | Action | Result |
|------|---|---|------|------|-----|-----|---------------|--------|--------|
| 0 | 0 | 0 | `[0, 2]` | `[1, 5]` | max(0,1)=1 | min(2,5)=2 | Yes: 1≤2 | Move i (2<5) | `[[1, 2]]` |
| 1 | 1 | 0 | `[5, 10]` | `[1, 5]` | max(5,1)=5 | min(10,5)=5 | Yes: 5≤5 | Move j (5=5) | `[[1, 2], [5, 5]]` |
| 2 | 1 | 1 | `[5, 10]` | `[8, 12]` | max(5,8)=8 | min(10,12)=10 | Yes: 8≤10 | Move i (10<12) | `[[1, 2], [5, 5], [8, 10]]` |
| 3 | 2 | 1 | `[13, 23]` | `[8, 12]` | max(13,8)=13 | min(23,12)=12 | No: 13>12 | Move j (12<23) | `[[1, 2], [5, 5], [8, 10]]` |
| 4 | 2 | 2 | `[13, 23]` | `[15, 24]` | max(13,15)=15 | min(23,24)=23 | Yes: 15≤23 | Move i (23<24) | `[[1, 2], [5, 5], [8, 10], [15, 23]]` |
| 5 | 3 | 2 | `[24, 25]` | `[15, 24]` | max(24,15)=24 | min(25,24)=24 | Yes: 24≤24 | Move j (24<25) | `[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24]]` |
| 6 | 3 | 3 | `[24, 25]` | `[25, 26]` | max(24,25)=25 | min(25,26)=25 | Yes: 25≤25 | Move i (25=25) | `[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]` |
| 7 | 4 | 3 | — | `[25, 26]` | — | — | Loop ends (i out of bounds) | — | Final result |

---

## Detailed Step Breakdown

### Step 0: Initialization
```
A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]

i = 0, j = 0
ans = []
```

### Step 1: Compare A[0] and B[0]

**A[0] = [0, 2]**, **B[0] = [1, 5]**

```
Calculate intersection:
  lo = max(A[0][0], B[0][0]) = max(0, 1) = 1
  hi = min(A[0][1], B[0][1]) = min(2, 5) = 2

Check: lo (1) <= hi (2) → YES, intersection exists!
  Intersection: [1, 2]
  Add to result: ans = [[1, 2]]

Which pointer to move?
  A[0][1] = 2
  B[0][1] = 5
  2 < 5 → Move i (A[0] ends first)
  i = 1
```

**Visualization:**
```
A[0]: [────────]
B[0]:      [──────────]
         [──] ← Intersection [1, 2]
```

### Step 2: Compare A[1] and B[0]

**A[1] = [5, 10]**, **B[0] = [1, 5]**

```
Calculate intersection:
  lo = max(A[1][0], B[0][0]) = max(5, 1) = 5
  hi = min(A[1][1], B[0][1]) = min(10, 5) = 5

Check: lo (5) <= hi (5) → YES, intersection exists!
  Intersection: [5, 5] (single point)
  Add to result: ans = [[1, 2], [5, 5]]

Which pointer to move?
  A[1][1] = 10
  B[0][1] = 5
  10 > 5 → Move j (B[0] ends first)
  j = 1
```

**Visualization:**
```
A[1]:              [──────────────────]
B[0]:      [──────────]
                    [─] ← Intersection [5, 5]
```

### Step 3: Compare A[1] and B[1]

**A[1] = [5, 10]**, **B[1] = [8, 12]**

```
Calculate intersection:
  lo = max(A[1][0], B[1][0]) = max(5, 8) = 8
  hi = min(A[1][1], B[1][1]) = min(10, 12) = 10

Check: lo (8) <= hi (10) → YES, intersection exists!
  Intersection: [8, 10]
  Add to result: ans = [[1, 2], [5, 5], [8, 10]]

Which pointer to move?
  A[1][1] = 10
  B[1][1] = 12
  10 < 12 → Move i (A[1] ends first)
  i = 2
```

**Visualization:**
```
A[1]:              [──────────────────]
B[1]:                           [──────────────]
                    [──────] ← Intersection [8, 10]
```

### Step 4: Compare A[2] and B[1]

**A[2] = [13, 23]**, **B[1] = [8, 12]**

```
Calculate intersection:
  lo = max(A[2][0], B[1][0]) = max(13, 8) = 13
  hi = min(A[2][1], B[1][1]) = min(23, 12) = 12

Check: lo (13) <= hi (12) → NO, no intersection!
  (A[2] starts after B[1] ends)

Which pointer to move?
  A[2][1] = 23
  B[1][1] = 12
  23 > 12 → Move j (B[1] ends first)
  j = 2
```

**Visualization:**
```
A[2]:                                    [──────────────────────────]
B[1]:                           [──────────────]
         No overlap - A[2] starts after B[1] ends
```

### Step 5: Compare A[2] and B[2]

**A[2] = [13, 23]**, **B[2] = [15, 24]**

```
Calculate intersection:
  lo = max(A[2][0], B[2][0]) = max(13, 15) = 15
  hi = min(A[2][1], B[2][1]) = min(23, 24) = 23

Check: lo (15) <= hi (23) → YES, intersection exists!
  Intersection: [15, 23]
  Add to result: ans = [[1, 2], [5, 5], [8, 10], [15, 23]]

Which pointer to move?
  A[2][1] = 23
  B[2][1] = 24
  23 < 24 → Move i (A[2] ends first)
  i = 3
```

**Visualization:**
```
A[2]:                                    [──────────────────────────]
B[2]:                                               [──────────────────────────]
                                         [──────────────────] ← Intersection [15, 23]
```

### Step 6: Compare A[3] and B[2]

**A[3] = [24, 25]**, **B[2] = [15, 24]**

```
Calculate intersection:
  lo = max(A[3][0], B[2][0]) = max(24, 15) = 24
  hi = min(A[3][1], B[2][1]) = min(25, 24) = 24

Check: lo (24) <= hi (24) → YES, intersection exists!
  Intersection: [24, 24] (single point)
  Add to result: ans = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24]]

Which pointer to move?
  A[3][1] = 25
  B[2][1] = 24
  25 > 24 → Move j (B[2] ends first)
  j = 3
```

**Visualization:**
```
A[3]:                                                                                                                      [────]
B[2]:                                               [──────────────────────────]
                                                                              [─] ← Intersection [24, 24]
```

### Step 7: Compare A[3] and B[3]

**A[3] = [24, 25]**, **B[3] = [25, 26]**

```
Calculate intersection:
  lo = max(A[3][0], B[3][0]) = max(24, 25) = 25
  hi = min(A[3][1], B[3][1]) = min(25, 26) = 25

Check: lo (25) <= hi (25) → YES, intersection exists!
  Intersection: [25, 25] (single point)
  Add to result: ans = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

Which pointer to move?
  A[3][1] = 25
  B[3][1] = 26
  25 < 26 → Move i (A[3] ends first)
  i = 4
```

**Visualization:**
```
A[3]:                                                                                                                      [────]
B[3]:                                                                                                                         [────]
                                                                                                                         [─] ← Intersection [25, 25]
```

### Step 8: Loop Ends

```
i = 4 >= len(A) = 4
Loop condition fails: i < len(A) is False
Exit loop

Final result: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
```

---

## Key Concepts

### 1. Intersection Calculation

For two intervals `[a, b]` and `[c, d]`:
- **Start of intersection**: `max(a, c)` (the later start)
- **End of intersection**: `min(b, d)` (the earlier end)
- **Valid intersection**: `max(a, c) <= min(b, d)`

**Why?**
- If `max(a, c) > min(b, d)`, the intervals don't overlap
- Example: `[1, 3]` and `[5, 7]` → `max(1,5)=5`, `min(3,7)=3` → `5 > 3` → No overlap

### 2. Pointer Movement Strategy

**Always move the pointer of the interval with the smaller endpoint.**

**Why?**
- If `A[i][1] < B[j][1]`, then `A[i]` ends before `B[j]`
- `A[i]` can't intersect with any future intervals in `B` (they all start after `B[j]` starts, which is after `A[i]` ends)
- So we can safely discard `A[i]` and move to `A[i+1]`

**Example:**
```
A[i] = [5, 10]
B[j] = [8, 12]
B[j+1] = [15, 20]  (starts at 15, which is > 10)

A[i] ends at 10, so it can't intersect with B[j+1] which starts at 15.
Move i to check A[i+1] with B[j].
```

### 3. Single Point Intersections

When `lo == hi`, the intersection is a single point:
- `[5, 5]` means the intervals touch at point 5
- This is still a valid intersection (closed intervals)

---

## Algorithm Pseudocode

```python
def intervalIntersection(A, B):
    ans = []
    i = j = 0
    
    while i < len(A) and j < len(B):
        # Calculate intersection
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
        
        # Check if intersection exists
        if lo <= hi:
            ans.append([lo, hi])
        
        # Move pointer with smaller endpoint
        if A[i][1] < B[j][1]:
            i += 1  # A[i] ends first
        else:
            j += 1  # B[j] ends first or equal
    
    return ans
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(n + m) | Each interval is visited at most once |
| **Space** | O(k) | Where k is the number of intersections (output size) |

---

## Edge Cases

### Case 1: No Intersections
```
A = [[1, 3], [5, 9]]
B = [[4, 4], [10, 11]]
Result: []
```

### Case 2: Single Point Intersection
```
A = [[1, 2], [5, 6]]
B = [[2, 3], [4, 5]]
Result: [[2, 2], [5, 5]]
```

### Case 3: Complete Overlap
```
A = [[1, 7]]
B = [[3, 10]]
Result: [[3, 7]]  (the overlapping portion)
```

### Case 4: One List is Empty
```
A = [[1, 2], [3, 4]]
B = []
Result: []
```

### Case 5: Adjacent Intervals
```
A = [[1, 2], [3, 4]]
B = [[2, 3]]
Result: [[2, 2], [3, 3]]  (touching at points 2 and 3)
```

---

## Visual Summary

```
Algorithm Flow:

A: [──] [──────] [──────────] [──]
B:    [──] [────] [────────────] [──]
      ↓    ↓      ↓            ↓
      [─] [─]    [────]       [─] [─]
      
Result: All intersections found by comparing in order
```

---

## Why This Algorithm Works

1. **Sorted Input**: Both lists are sorted, so we can use two pointers
2. **Greedy Approach**: Always process the interval that ends first
3. **No Backtracking**: Once we move a pointer, we never need to go back
4. **Complete Coverage**: Every possible intersection is checked exactly once

---

## Summary

The interval intersection algorithm:
- Uses **two pointers** to traverse both lists
- Calculates intersection as `[max(start1, start2), min(end1, end2)]`
- Moves the pointer of the interval with the **smaller endpoint**
- Time complexity: **O(n + m)** where n, m are list lengths
- Space complexity: **O(k)** where k is the number of intersections

**Key Insight**: Moving the pointer with the smaller endpoint ensures we never miss an intersection and never check the same pair twice.

---

## Related Problems

- **LeetCode 56**: Merge Intervals
- **LeetCode 57**: Insert Interval
- **LeetCode 435**: Non-overlapping Intervals
- **LeetCode 452**: Minimum Number of Arrows to Burst Balloons

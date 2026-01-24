# Sparse Vector Dot Product

> **LeetCode 1570**: Given two sparse vectors, compute their dot product efficiently.

## Problem Description

A sparse vector is a vector that has mostly zero values. Instead of storing all values, we only store non-zero elements as `(index, value)` pairs.

**Example:**
- Original vector: `[1, 0, 0, 2, 3]` (5 elements)
- Sparse representation: `[(0, 1), (3, 2), (4, 3)]` (3 elements)

**Dot Product**: `vec1 · vec2 = Σ(vec1[i] × vec2[i])` for all indices `i`

---

## Key Insight

For sparse vectors, we can:
1. **Store only non-zero elements** → saves space
2. **Use two pointers** to traverse both sparse vectors → O(n + m) time instead of O(n × m)

**Algorithm**: Compare indices, only multiply when they match!

---

## Algorithm Logic

```
1. Convert vectors to sparse representation (index, value) pairs
2. Use two pointers (p1, p2) to traverse both sparse vectors
3. For each iteration:
   - If index1 == index2:
     * Multiply values and add to result
     * Move BOTH pointers forward
   - If index1 < index2:
     * Skip index1 (no match possible)
     * Move pointer 1 forward
   - If index2 < index1:
     * Skip index2 (no match possible)
     * Move pointer 2 forward
4. Return accumulated result
```

---

## Example 1: Basic Sparse Vectors

**Input**: 
- `vec1 = [1, 0, 0, 2, 3]` → sparse: `[(0, 1), (3, 2), (4, 3)]`
- `vec2 = [0, 3, 0, 4, 0]` → sparse: `[(1, 3), (3, 4)]`

### Step-by-Step Execution

| Iter | p1 | p2 | index1 | value1 | index2 | value2 | Action | Result |
|------|----|----|--------|--------|--------|--------|---------|--------|
| 1 | 0 | 0 | 0 | 1 | 1 | 3 | `0 < 1` → move p1 | 0 |
| 2 | 1 | 0 | 3 | 2 | 1 | 3 | `1 < 3` → move p2 | 0 |
| 3 | 1 | 1 | 3 | 2 | 3 | 4 | `3 == 3` → multiply: 2×4=8 | 8 |

### Detailed Iteration 1
```
   p1=0, p2=0
   elements1[0] = (0, 1)
   elements2[0] = (1, 3)
   
   Vector 1: [0:1]←p1 [3:2] [4:3]
   Vector 2: [1:3]←p2 [3:4]
   
   index1=0 < index2=1
   → No match, skip index1
   → Move pointer 1: p1 = 1
```

### Detailed Iteration 2
```
   p1=1, p2=0
   elements1[1] = (3, 2)
   elements2[0] = (1, 3)
   
   Vector 1: [0:1] [3:2]←p1 [4:3]
   Vector 2: [1:3]←p2 [3:4]
   
   index2=1 < index1=3
   → No match, skip index2
   → Move pointer 2: p2 = 1
```

### Detailed Iteration 3
```
   p1=1, p2=1
   elements1[1] = (3, 2)
   elements2[1] = (3, 4)
   
   Vector 1: [0:1] [3:2]←p1 [4:3]
   Vector 2: [1:3] [3:4]←p2
   
   index1=3 == index2=3 ✅ MATCH!
   → Multiply: 2 × 4 = 8
   → Add to result: result = 0 + 8 = 8
   → Move BOTH pointers: p1 = 2, p2 = 2
```

**Result**: `8` ✅

**Verification**: 
```
vec1 = [1, 0, 0, 2, 3]
vec2 = [0, 3, 0, 4, 0]
Dot product = 1×0 + 0×3 + 0×0 + 2×4 + 3×0
            = 0 + 0 + 0 + 8 + 0 = 8 ✓
```

---

## Example 2: No Matching Indices

**Input**:
- `vec1 = [1, 0, 0, 0, 0]` → sparse: `[(0, 1)]`
- `vec2 = [0, 0, 0, 0, 5]` → sparse: `[(4, 5)]`

| Iter | p1 | p2 | index1 | index2 | Action | Result |
|------|----|----|--------|--------|--------|--------|
| 1 | 0 | 0 | 0 | 4 | `0 < 4` → move p1 | 0 |
| — | 1 | 0 | — | — | Loop ends (p1 out of bounds) | 0 |

**Result**: `0` ✅ (no matching indices)

---

## Example 3: All Matching Indices

**Input**:
- `vec1 = [1, 0, 3, 0, 5]` → sparse: `[(0, 1), (2, 3), (4, 5)]`
- `vec2 = [2, 0, 4, 0, 6]` → sparse: `[(0, 2), (2, 4), (4, 6)]`

| Iter | p1 | p2 | index1 | value1 | index2 | value2 | Action | Result |
|------|----|----|--------|--------|--------|--------|---------|--------|
| 1 | 0 | 0 | 0 | 1 | 0 | 2 | Match: 1×2=2 | 2 |
| 2 | 1 | 1 | 2 | 3 | 2 | 4 | Match: 3×4=12 | 14 |
| 3 | 2 | 2 | 4 | 5 | 4 | 6 | Match: 5×6=30 | 44 |

**Result**: `44` ✅

**Verification**:
```
vec1 = [1, 0, 3, 0, 5]
vec2 = [2, 0, 4, 0, 6]
Dot product = 1×2 + 0×0 + 3×4 + 0×0 + 5×6
            = 2 + 0 + 12 + 0 + 30 = 44 ✓
```

---

## Example 4: One Vector is All Zeros

**Input**:
- `vec1 = [1, 2, 3]` → sparse: `[(0, 1), (1, 2), (2, 3)]`
- `vec2 = [0, 0, 0]` → sparse: `[]` (empty)

**Result**: `0` ✅ (one vector has no non-zero elements)

---

## Example 5: Large Sparse Vectors

**Input**:
- `vec1 = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0]` → sparse: `[(2, 1), (5, 2), (8, 3)]`
- `vec2 = [0, 1, 0, 0, 2, 0, 0, 3, 0, 0]` → sparse: `[(1, 1), (4, 2), (7, 3)]`

| Iter | p1 | p2 | index1 | index2 | Action |
|------|----|----|--------|--------|--------|
| 1 | 0 | 0 | 2 | 1 | `1 < 2` → move p2 |
| 2 | 0 | 1 | 2 | 4 | `2 < 4` → move p1 |
| 3 | 1 | 1 | 5 | 4 | `4 < 5` → move p2 |
| 4 | 1 | 2 | 5 | 7 | `5 < 7` → move p1 |
| 5 | 2 | 2 | 8 | 7 | `7 < 8` → move p2 |
| — | 2 | 3 | — | — | Loop ends |

**Result**: `0` ✅ (no matching indices)

---

## Visual Comparison: Dense vs Sparse

### Dense Vector Approach
```
vec1 = [1, 0, 0, 2, 3]
vec2 = [0, 3, 0, 4, 0]

Dot product = 1×0 + 0×3 + 0×0 + 2×4 + 3×0
            = 0 + 0 + 0 + 8 + 0 = 8

Time: O(n) where n = vector length
Space: O(n) for each vector
```

### Sparse Vector Approach
```
vec1 sparse: [(0, 1), (3, 2), (4, 3)]  (3 elements)
vec2 sparse: [(1, 3), (3, 4)]          (2 elements)

Only compare matching indices:
- Index 3 matches: 2 × 4 = 8

Time: O(n + m) where n, m = non-zero counts
Space: O(n + m) for sparse storage
```

**Advantage**: For very sparse vectors (many zeros), sparse approach is much faster!

---

## Decision Tree

```
                    ┌─────────────────┐
                    │ p1 < len(vec1)  │
                    │ AND             │
                    │ p2 < len(vec2)? │
                    └─────────┬───────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                   YES                  NO
                    │                   │
                    ▼                   ▼
            ┌───────────────┐      ┌──────────┐
            │ Get indices  │      │ Return   │
            │ index1,      │      │ result   │
            │ index2       │      └──────────┘
            └───────┬───────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
        ▼           ▼           ▼
   index1 ==    index1 <    index2 <
   index2?      index2?     index1?
        │           │           │
    ┌───┴───┐   ┌───┴───┐   ┌───┴───┐
   YES      NO  YES      NO YES      NO
    │        │   │        │   │       │
    ▼        ▼   ▼        ▼   ▼       ▼
 Multiply  Skip Skip    Skip Skip   Skip
 & add     p1   p2      p1   p2      p1
 Move both
 pointers
```

---

## Complexity Analysis

| Aspect | Dense Approach | Sparse Approach |
|--------|----------------|-----------------|
| **Time** | O(n) | O(n + m) where n, m = non-zero counts |
| **Space** | O(n) per vector | O(k) per vector where k = non-zero count |

**When sparse is better**: When vectors have many zeros (k << n)

**Example**: Vector of length 1,000,000 with only 10 non-zero elements
- Dense: O(1,000,000) operations
- Sparse: O(20) operations (10 + 10) → **50,000x faster!**

---

## Summary Table

| Example | vec1 | vec2 | Matching Indices | Result | Iterations |
|---------|------|------|-------------------|---------|-------------|
| 1 | `[1,0,0,2,3]` | `[0,3,0,4,0]` | Index 3 | 8 | 3 |
| 2 | `[1,0,0,0,0]` | `[0,0,0,0,5]` | None | 0 | 1 |
| 3 | `[1,0,3,0,5]` | `[2,0,4,0,6]` | 0, 2, 4 | 44 | 3 |
| 4 | `[1,2,3]` | `[0,0,0]` | None | 0 | 0 |
| 5 | Large sparse | Large sparse | None | 0 | 5 |

---

## Source Code

```python
class SparseVector:
    def __init__(self, nums: List[int]):
        # Store only non-zero elements as (index, value)
        self.elements = [(i, num) for i, num in enumerate(nums) if num != 0]

    def dotProduct(self, vec: 'SparseVector') -> int:
        # Use two pointers to traverse both sparse vectors
        p1 = p2 = 0
        result = 0
        elements1, elements2 = self.elements, vec.elements

        while p1 < len(elements1) and p2 < len(elements2):
            index1, value1 = elements1[p1]
            index2, value2 = elements2[p2]

            if index1 == index2:
                # Indices match: multiply and add
                result += value1 * value2
                p1 += 1
                p2 += 1
            elif index1 < index2:
                # Skip index1 (no match possible)
                p1 += 1
            else:
                # Skip index2 (no match possible)
                p2 += 1

        return result
```

---

## Common Mistakes to Avoid

1. **Not handling empty sparse vectors**
   - Check if `elements` list is empty before looping

2. **Moving both pointers when indices don't match**
   - Only move the pointer with the smaller index

3. **Not storing sparse representation efficiently**
   - Use list of tuples `(index, value)` instead of dictionary for ordered traversal

4. **Forgetting to increment pointers after match**
   - Must move both pointers forward after multiplying

---

## Real-World Applications

1. **Machine Learning**: Feature vectors in NLP (most words don't appear in each document)
2. **Scientific Computing**: Large matrices with mostly zeros
3. **Database Systems**: Sparse data storage and querying
4. **Graph Algorithms**: Adjacency lists for sparse graphs
5. **Image Processing**: Sparse representations of images

---

## Related Problems

- **LeetCode 311**: Sparse Matrix Multiplication
- **LeetCode 1429**: First Unique Number
- **LeetCode 1472**: Design Browser History

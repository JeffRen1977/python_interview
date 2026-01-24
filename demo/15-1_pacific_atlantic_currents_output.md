# Pacific Atlantic Water Flow

> **LeetCode 417**: There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges. Water can only flow in four directions (up, down, left, right) to cells with a height less than or equal to the current cell's height. Find all cells where water can flow to both oceans.

## Problem Description

Find all cells in a matrix where water can flow to both the Pacific Ocean (top/left edges) and Atlantic Ocean (bottom/right edges).

**Flow Rule**: Water flows from a cell to adjacent cells with height ≤ current cell height.

**Example:**
```
Matrix:
  1  2  2  3  5
  3  2  3  4  4
  2  4  5  3  1
  6  7  1  4  5
  5  1  1  2  4

Result: [[0,4], [1,3], [1,4], [2,2], [3,0], [3,1], [4,0]]
```

---

## Key Insight

Use **reverse thinking** with DFS:
- Instead of checking if each cell can reach oceans, start from oceans and find all reachable cells
- Use two DFS traversals:
  1. From Pacific edges (top + left) → find all cells reachable from Pacific
  2. From Atlantic edges (bottom + right) → find all cells reachable from Atlantic
- Return intersection: cells reachable from both oceans

**Strategy**: Start from ocean edges and flow "upstream" (to higher or equal heights).

---

## Algorithm Logic

```
1. Initialize:
   - pacific = set()  (cells reachable from Pacific)
   - atlantic = set() (cells reachable from Atlantic)

2. DFS from Pacific edges:
   - Start DFS from all cells in top row (row 0)
   - Start DFS from all cells in left column (col 0)
   - Mark all reachable cells in pacific set

3. DFS from Atlantic edges:
   - Start DFS from all cells in bottom row (row R-1)
   - Start DFS from all cells in right column (col C-1)
   - Mark all reachable cells in atlantic set

4. Return intersection:
   - Return cells in both pacific and atlantic sets
```

---

## Detailed Example: Step-by-Step

**Input**: 
```
matrix = [
  [1, 2, 2, 3, 5],
  [3, 2, 3, 4, 4],
  [2, 4, 5, 3, 1],
  [6, 7, 1, 4, 5],
  [5, 1, 1, 2, 4]
]
```

### Visual Representation

```
Matrix (row, col):
        Col: 0  1  2  3  4
Row 0:      [1, 2, 2, 3, 5]  ← Pacific (top edge)
Row 1:      [3, 2, 3, 4, 4]
Row 2:      [2, 4, 5, 3, 1]
Row 3:      [6, 7, 1, 4, 5]
Row 4:      [5, 1, 1, 2, 4]  ← Atlantic (bottom edge)
             ↑              ↑
         Pacific        Atlantic
         (left edge)    (right edge)
```

### Phase 1: DFS from Pacific Ocean

**Starting Points**: Top row (row 0) and left column (col 0)

#### DFS from Top Row (Pacific - Top Edge)

**Starting from (0, 0):**
```
Cell (0, 0): height = 1
  Add to pacific: {(0, 0)}
  Check neighbors:
    (0, 1): height 2 >= 1? YES → DFS(0, 1)
    (1, 0): height 3 >= 1? YES → DFS(1, 0)
```

**DFS(0, 1):**
```
Cell (0, 1): height = 2
  Add to pacific: {(0, 0), (0, 1)}
  Check neighbors:
    (0, 0): already in pacific → skip
    (0, 2): height 2 >= 2? YES → DFS(0, 2)
    (1, 1): height 2 >= 2? YES → DFS(1, 1)
```

**DFS(0, 2):**
```
Cell (0, 2): height = 2
  Add to pacific: {(0, 0), (0, 1), (0, 2)}
  Check neighbors:
    (0, 1): already in pacific → skip
    (0, 3): height 3 >= 2? YES → DFS(0, 3)
    (1, 2): height 3 >= 2? YES → DFS(1, 2)
```

**DFS(0, 3):**
```
Cell (0, 3): height = 3
  Add to pacific: {(0, 0), (0, 1), (0, 2), (0, 3)}
  Check neighbors:
    (0, 2): already in pacific → skip
    (0, 4): height 5 >= 3? YES → DFS(0, 4)
    (1, 3): height 4 >= 3? YES → DFS(1, 3)
```

**DFS(0, 4):**
```
Cell (0, 4): height = 5
  Add to pacific: {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)}
  Check neighbors:
    (0, 3): already in pacific → skip
    (1, 4): height 4 >= 5? NO → skip
```

**DFS(1, 0):**
```
Cell (1, 0): height = 3
  Add to pacific: {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0)}
  Check neighbors:
    (0, 0): already in pacific → skip
    (1, 1): height 2 >= 3? NO → skip
    (2, 0): height 2 >= 3? NO → skip
```

**DFS(1, 1):**
```
Cell (1, 1): height = 2
  Add to pacific: {(..., (1, 1))}
  Check neighbors:
    (0, 1): already in pacific → skip
    (1, 0): already in pacific → skip
    (1, 2): height 3 >= 2? YES → DFS(1, 2)
    (2, 1): height 4 >= 2? YES → DFS(2, 1)
```

**DFS(1, 2):**
```
Cell (1, 2): height = 3
  Add to pacific: {(..., (1, 2))}
  Check neighbors:
    (0, 2): already in pacific → skip
    (1, 1): already in pacific → skip
    (1, 3): height 4 >= 3? YES → DFS(1, 3)
    (2, 2): height 5 >= 3? YES → DFS(2, 2)
```

**DFS(1, 3):**
```
Cell (1, 3): height = 4
  Add to pacific: {(..., (1, 3))}
  Check neighbors:
    (0, 3): already in pacific → skip
    (1, 2): already in pacific → skip
    (1, 4): height 4 >= 4? YES → DFS(1, 4)
    (2, 3): height 3 >= 4? NO → skip
```

**DFS(1, 4):**
```
Cell (1, 4): height = 4
  Add to pacific: {(..., (1, 4))}
  Check neighbors:
    (0, 4): already in pacific → skip
    (1, 3): already in pacific → skip
    (2, 4): height 1 >= 4? NO → skip
```

**DFS(2, 1):**
```
Cell (2, 1): height = 4
  Add to pacific: {(..., (2, 1))}
  Check neighbors:
    (1, 1): already in pacific → skip
    (2, 0): height 2 >= 4? NO → skip
    (2, 2): height 5 >= 4? YES → DFS(2, 2)
    (3, 1): height 7 >= 4? YES → DFS(3, 1)
```

**DFS(2, 2):**
```
Cell (2, 2): height = 5
  Add to pacific: {(..., (2, 2))}
  Check neighbors:
    (1, 2): already in pacific → skip
    (2, 1): already in pacific → skip
    (2, 3): height 3 >= 5? NO → skip
    (3, 2): height 1 >= 5? NO → skip
```

**DFS(3, 1):**
```
Cell (3, 1): height = 7
  Add to pacific: {(..., (3, 1))}
  Check neighbors:
    (2, 1): already in pacific → skip
    (3, 0): height 6 >= 7? NO → skip
    (3, 2): height 1 >= 7? NO → skip
    (4, 1): height 1 >= 7? NO → skip
```

**DFS from Left Column (Pacific - Left Edge):**

**Starting from (2, 0):**
```
Cell (2, 0): height = 2
  Already in pacific? Check... (not yet)
  Add to pacific: {(..., (2, 0))}
  Check neighbors:
    (1, 0): already in pacific → skip
    (2, 1): already in pacific → skip
    (3, 0): height 6 >= 2? YES → DFS(3, 0)
```

**DFS(3, 0):**
```
Cell (3, 0): height = 6
  Add to pacific: {(..., (3, 0))}
  Check neighbors:
    (2, 0): already in pacific → skip
    (3, 1): already in pacific → skip
    (4, 0): height 5 >= 6? NO → skip
```

**Starting from (4, 0):**
```
Cell (4, 0): height = 5
  Add to pacific: {(..., (4, 0))}
  Check neighbors:
    (3, 0): already in pacific → skip
    (4, 1): height 1 >= 5? NO → skip
```

**Pacific Set (after Phase 1):**
```
pacific = {
  (0,0), (0,1), (0,2), (0,3), (0,4),  # Top row
  (1,0), (1,1), (1,2), (1,3), (1,4),  # Row 1
  (2,0), (2,1), (2,2),                 # Row 2
  (3,0), (3,1),                        # Row 3
  (4,0)                                # Row 4
}
```

### Phase 2: DFS from Atlantic Ocean

**Starting Points**: Bottom row (row 4) and right column (col 4)

#### DFS from Bottom Row (Atlantic - Bottom Edge)

**Starting from (4, 0):**
```
Cell (4, 0): height = 5
  Add to atlantic: {(4, 0)}
  Check neighbors:
    (3, 0): height 6 >= 5? YES → DFS(3, 0)
    (4, 1): height 1 >= 5? NO → skip
```

**DFS(3, 0):**
```
Cell (3, 0): height = 6
  Add to atlantic: {(4, 0), (3, 0)}
  Check neighbors:
    (4, 0): already in atlantic → skip
    (2, 0): height 2 >= 6? NO → skip
    (3, 1): height 7 >= 6? YES → DFS(3, 1)
```

**DFS(3, 1):**
```
Cell (3, 1): height = 7
  Add to atlantic: {(4, 0), (3, 0), (3, 1)}
  Check neighbors:
    (3, 0): already in atlantic → skip
    (2, 1): height 4 >= 7? NO → skip
    (3, 2): height 1 >= 7? NO → skip
    (4, 1): height 1 >= 7? NO → skip
```

**Starting from (4, 1):**
```
Cell (4, 1): height = 1
  Add to atlantic: {(4, 0), (3, 0), (3, 1), (4, 1)}
  Check neighbors:
    (4, 0): already in atlantic → skip
    (4, 2): height 1 >= 1? YES → DFS(4, 2)
    (3, 1): already in atlantic → skip
```

**DFS(4, 2):**
```
Cell (4, 2): height = 1
  Add to atlantic: {(..., (4, 2))}
  Check neighbors:
    (4, 1): already in atlantic → skip
    (4, 3): height 2 >= 1? YES → DFS(4, 3)
    (3, 2): height 1 >= 1? YES → DFS(3, 2)
```

**DFS(4, 3):**
```
Cell (4, 3): height = 2
  Add to atlantic: {(..., (4, 3))}
  Check neighbors:
    (4, 2): already in atlantic → skip
    (4, 4): height 4 >= 2? YES → DFS(4, 4)
    (3, 3): height 4 >= 2? YES → DFS(3, 3)
```

**DFS(4, 4):**
```
Cell (4, 4): height = 4
  Add to atlantic: {(..., (4, 4))}
  Check neighbors:
    (4, 3): already in atlantic → skip
    (3, 4): height 5 >= 4? YES → DFS(3, 4)
```

**DFS(3, 4):**
```
Cell (3, 4): height = 5
  Add to atlantic: {(..., (3, 4))}
  Check neighbors:
    (4, 4): already in atlantic → skip
    (2, 4): height 1 >= 5? NO → skip
    (3, 3): height 4 >= 5? NO → skip
```

**DFS(3, 2):**
```
Cell (3, 2): height = 1
  Add to atlantic: {(..., (3, 2))}
  Check neighbors:
    (4, 2): already in atlantic → skip
    (3, 1): already in atlantic → skip
    (3, 3): height 4 >= 1? YES → DFS(3, 3)
    (2, 2): height 5 >= 1? YES → DFS(2, 2)
```

**DFS(3, 3):**
```
Cell (3, 3): height = 4
  Add to atlantic: {(..., (3, 3))}
  Check neighbors:
    (4, 3): already in atlantic → skip
    (3, 2): already in atlantic → skip
    (3, 4): already in atlantic → skip
    (2, 3): height 3 >= 4? NO → skip
```

**DFS(2, 2):**
```
Cell (2, 2): height = 5
  Add to atlantic: {(..., (2, 2))}
  Check neighbors:
    (3, 2): already in atlantic → skip
    (2, 1): height 4 >= 5? NO → skip
    (2, 3): height 3 >= 5? NO → skip
    (1, 2): height 3 >= 5? NO → skip
```

#### DFS from Right Column (Atlantic - Right Edge)

**Starting from (0, 4):**
```
Cell (0, 4): height = 5
  Add to atlantic: {(..., (0, 4))}
  Check neighbors:
    (0, 3): height 3 >= 5? NO → skip
    (1, 4): height 4 >= 5? NO → skip
```

**Starting from (1, 4):**
```
Cell (1, 4): height = 4
  Already in atlantic? Check... (not yet)
  Add to atlantic: {(..., (1, 4))}
  Check neighbors:
    (0, 4): already in atlantic → skip
    (1, 3): height 4 >= 4? YES → DFS(1, 3)
    (2, 4): height 1 >= 4? NO → skip
```

**DFS(1, 3):**
```
Cell (1, 3): height = 4
  Add to atlantic: {(..., (1, 3))}
  Check neighbors:
    (1, 4): already in atlantic → skip
    (0, 3): height 3 >= 4? NO → skip
    (1, 2): height 3 >= 4? NO → skip
    (2, 3): height 3 >= 4? NO → skip
```

**Starting from (2, 4):**
```
Cell (2, 4): height = 1
  Add to atlantic: {(..., (2, 4))}
  Check neighbors:
    (1, 4): already in atlantic → skip
    (2, 3): height 3 >= 1? YES → DFS(2, 3)
    (3, 4): already in atlantic → skip
```

**DFS(2, 3):**
```
Cell (2, 3): height = 3
  Add to atlantic: {(..., (2, 3))}
  Check neighbors:
    (2, 4): already in atlantic → skip
    (2, 2): already in atlantic → skip
    (1, 3): already in atlantic → skip
    (3, 3): already in atlantic → skip
```

**Atlantic Set (after Phase 2):**
```
atlantic = {
  (0,4),                    # Top right
  (1,3), (1,4),             # Row 1
  (2,2), (2,3), (2,4),      # Row 2
  (3,0), (3,1), (3,2), (3,3), (3,4),  # Row 3
  (4,0), (4,1), (4,2), (4,3), (4,4)   # Bottom row
}
```

### Phase 3: Find Intersection

```
pacific = {
  (0,0), (0,1), (0,2), (0,3), (0,4),
  (1,0), (1,1), (1,2), (1,3), (1,4),
  (2,0), (2,1), (2,2),
  (3,0), (3,1),
  (4,0)
}

atlantic = {
  (0,4),
  (1,3), (1,4),
  (2,2), (2,3), (2,4),
  (3,0), (3,1), (3,2), (3,3), (3,4),
  (4,0), (4,1), (4,2), (4,3), (4,4)
}

Intersection (cells in both sets):
  (0,4)  ✓
  (1,3)  ✓
  (1,4)  ✓
  (2,2)  ✓
  (3,0)  ✓
  (3,1)  ✓
  (4,0)  ✓

Result: [[0,4], [1,3], [1,4], [2,2], [3,0], [3,1], [4,0]]
```

---

## Key Concepts

### 1. Reverse Thinking

Instead of checking if each cell can reach oceans (expensive), we:
- Start from ocean edges
- Flow "upstream" to find all reachable cells
- Much more efficient!

### 2. Flow Direction

Water flows from higher to lower (or equal) heights:
- If `matrix[nr][nc] >= matrix[r][c]`, water can flow from `(r,c)` to `(nr,nc)`
- In reverse: if we're at `(nr,nc)` and `matrix[nr][nc] >= matrix[r][c]`, we can reach `(r,c)` from `(nr,nc)`

### 3. DFS Traversal

Use DFS to explore all reachable cells:
- Mark visited cells to avoid cycles
- Recursively explore valid neighbors
- Valid neighbor: within bounds AND height >= current height

### 4. Set Intersection

After finding cells reachable from both oceans:
- `pacific & atlantic` gives cells in both sets
- These are cells where water can flow to both oceans

---

## Visual Flow Diagram

```
Pacific DFS (from top and left):
        Col: 0  1  2  3  4
Row 0:  [P, P, P, P, P]  ← Start
Row 1:  [P, P, P, P, P]
Row 2:  [P, P, P,  ,  ]
Row 3:  [P, P,  ,  ,  ]
Row 4:  [P,  ,  ,  ,  ]

Atlantic DFS (from bottom and right):
        Col: 0  1  2  3  4
Row 0:  [ ,  ,  ,  , A]  ← Start
Row 1:  [ ,  ,  , A, A]
Row 2:  [ ,  , A, A, A]
Row 3:  [A, A, A, A, A]
Row 4:  [A, A, A, A, A]  ← Start

Intersection (both P and A):
        Col: 0  1  2  3  4
Row 0:  [ ,  ,  ,  , X]  X = (0,4)
Row 1:  [ ,  ,  , X, X]  X = (1,3), (1,4)
Row 2:  [ ,  , X,  ,  ]  X = (2,2)
Row 3:  [X, X,  ,  ,  ]  X = (3,0), (3,1)
Row 4:  [X,  ,  ,  ,  ]  X = (4,0)
```

---

## Algorithm Pseudocode

```python
def pacificAtlantic(matrix):
    if not matrix or not matrix[0]:
        return []
    
    R, C = len(matrix), len(matrix[0])
    pacific, atlantic = set(), set()
    
    def dfs(r, c, seen):
        if (r, c) in seen:
            return
        seen.add((r, c))
        
        # Explore neighbors
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            # Check bounds and flow condition
            if 0 <= nr < R and 0 <= nc < C:
                if matrix[nr][nc] >= matrix[r][c]:
                    dfs(nr, nc, seen)
    
    # DFS from Pacific edges
    for r in range(R):
        dfs(r, 0, pacific)  # Left edge
    for c in range(C):
        dfs(0, c, pacific)  # Top edge
    
    # DFS from Atlantic edges
    for r in range(R):
        dfs(r, C-1, atlantic)  # Right edge
    for c in range(C):
        dfs(R-1, c, atlantic)  # Bottom edge
    
    # Return intersection
    return list(pacific & atlantic)
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(m × n) | Each cell visited at most twice (once per ocean) |
| **Space** | O(m × n) | Sets store all reachable cells, recursion stack O(m×n) worst case |

---

## Edge Cases

### Case 1: Single Cell
```
matrix = [[1]]
Result: [[0, 0]]
(Touches both oceans)
```

### Case 2: Single Row
```
matrix = [[1, 2, 3]]
Result: [[0, 0], [0, 1], [0, 2]]
(All cells touch both top and bottom edges)
```

### Case 3: Single Column
```
matrix = [[1], [2], [3]]
Result: [[0, 0], [1, 0], [2, 0]]
(All cells touch both left and right edges)
```

### Case 4: All Same Height
```
matrix = [
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1]
]
Result: All cells (water can flow everywhere)
```

### Case 5: No Valid Paths
```
matrix = [
  [9, 9, 9],
  [9, 1, 9],
  [9, 9, 9]
]
Result: Only edge cells (can't flow from center)
```

---

## Why This Algorithm Works

### Correctness

1. **Pacific Reachability**: Starting from Pacific edges and flowing upstream, we find all cells that can reach Pacific
2. **Atlantic Reachability**: Starting from Atlantic edges and flowing upstream, we find all cells that can reach Atlantic
3. **Intersection**: Cells in both sets can reach both oceans

### Efficiency

- **Naive approach**: For each cell, check if it can reach both oceans → O((m×n)²)
- **This approach**: Two DFS traversals → O(m×n)
- Much more efficient!

---

## Summary

The Pacific Atlantic Water Flow algorithm:
- Uses **reverse thinking** with DFS
- Starts from ocean edges and flows upstream
- Finds cells reachable from Pacific and Atlantic separately
- Returns intersection of both sets
- Time complexity: **O(m × n)**
- Space complexity: **O(m × n)**

**Key Insight**: Instead of checking if each cell can reach oceans, start from oceans and find all reachable cells. Much more efficient!

---

## Related Problems

- **LeetCode 200**: Number of Islands
- **LeetCode 130**: Surrounded Regions
- **LeetCode 79**: Word Search
- **LeetCode 695**: Max Area of Island

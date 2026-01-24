# Walls and Gates - Farthest Positions from Cats

> **Problem**: Given a 2D board with cats (1), empty spaces (0), and walls (-1), find the positions that are farthest from all cats.

## Problem Description

Find empty cells that have the maximum shortest distance from any cat position.

**Board Representation:**
- `0`: Empty space (can be traversed)
- `1`: Cat position (source for distance calculation)
- `-1`: Wall/obstacle (cannot be traversed)

**Example:**
```
Board:
  0  -1   1   0
  0   0   0  -1
  0  -1   0  -1
  1  -1   0   0

Cats at: (0, 2) and (3, 0)
Farthest position: (3, 3) with distance 4
```

---

## Key Insight

Use **Multi-Source BFS (Breadth-First Search)**:
- Start BFS from ALL cat positions simultaneously
- BFS naturally finds shortest paths (minimum steps)
- Distance from a cell = minimum distance from any cat
- Find cells with maximum such distance

**Strategy**: Flood fill from all sources at once, tracking distances. The cell with maximum distance is farthest from all cats.

---

## Algorithm Logic

```
1. Initialize:
   - distance[i][j] = infinity (unreachable)
   - queue = all cat positions
   - Set distance[cat] = 0 for each cat

2. Multi-Source BFS:
   While queue not empty:
     Pop position (x, y)
     For each neighbor (nx, ny):
       If empty space (0) and not visited:
         distance[nx][ny] = distance[x][y] + 1
         Add (nx, ny) to queue

3. Find Maximum:
   Scan all empty cells
   Find cells with maximum distance
   Return all such cells
```

---

## Detailed Example: Step-by-Step

**Input Board:**
```
    0  1  2  3
0   0 -1  1  0
1   0  0  0 -1
2   0 -1  0 -1
3   1 -1  0  0

Cats at: (0, 2) and (3, 0)
Walls at: (0,1), (1,3), (2,1), (2,3), (3,1)
```

### Initial Setup

```
rows = 4, cols = 4
directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right

distance matrix (initialized to infinity):
    0    1    2    3
0  ∞    ∞    ∞    ∞
1  ∞    ∞    ∞    ∞
2  ∞    ∞    ∞    ∞
3  ∞    ∞    ∞    ∞

queue = deque()
```

### Step 1: Initialize with Cat Positions

**Find all cats and add to queue:**

```
Scan board:
  (0, 2): board[0][2] = 1 → Cat found!
    queue.append((0, 2))
    distance[0][2] = 0
    
  (3, 0): board[3][0] = 1 → Cat found!
    queue.append((3, 0))
    distance[3][0] = 0
```

**After Step 1:**
```
distance matrix:
    0    1    2    3
0  ∞    ∞    0    ∞
1  ∞    ∞    ∞    ∞
2  ∞    ∞    ∞    ∞
3  0    ∞    ∞    ∞

queue = [(0, 2), (3, 0)]
```

### Step 2: Multi-Source BFS - Iteration 1

**Process (0, 2) - Cat at top:**

```
Pop: (0, 2) from queue
Current distance: distance[0][2] = 0

Explore neighbors:
```

**Neighbor 1: Up (-1, 0)**
```
nx, ny = 0 + (-1), 2 + 0 = (-1, 2)
Check: -1 < 0 → Out of bounds ❌
Skip
```

**Neighbor 2: Down (1, 0)**
```
nx, ny = 0 + 1, 2 + 0 = (1, 2)
Check: 0 <= 1 < 4 and 0 <= 2 < 4 → Valid ✅
Check: board[1][2] = 0 (empty) ✅
Check: distance[1][2] = ∞ (not visited) ✅
  distance[1][2] = distance[0][2] + 1 = 0 + 1 = 1
  queue.append((1, 2))
```

**Neighbor 3: Left (0, -1)**
```
nx, ny = 0 + 0, 2 + (-1) = (0, 1)
Check: Valid ✅
Check: board[0][1] = -1 (wall) ❌
Skip
```

**Neighbor 4: Right (0, 1)**
```
nx, ny = 0 + 0, 2 + 1 = (0, 3)
Check: Valid ✅
Check: board[0][3] = 0 (empty) ✅
Check: distance[0][3] = ∞ (not visited) ✅
  distance[0][3] = distance[0][2] + 1 = 0 + 1 = 1
  queue.append((0, 3))
```

**After processing (0, 2):**
```
distance matrix:
    0    1    2    3
0  ∞    ∞    0    1
1  ∞    ∞    1    ∞
2  ∞    ∞    ∞    ∞
3  0    ∞    ∞    ∞

queue = [(3, 0), (1, 2), (0, 3)]
```

### Step 3: Multi-Source BFS - Iteration 2

**Process (3, 0) - Cat at bottom:**

```
Pop: (3, 0) from queue
Current distance: distance[3][0] = 0

Explore neighbors:
```

**Neighbor 1: Up (-1, 0)**
```
nx, ny = 3 + (-1), 0 + 0 = (2, 0)
Check: Valid ✅
Check: board[2][0] = 0 (empty) ✅
Check: distance[2][0] = ∞ (not visited) ✅
  distance[2][0] = distance[3][0] + 1 = 0 + 1 = 1
  queue.append((2, 0))
```

**Neighbor 2: Down (1, 0)**
```
nx, ny = 3 + 1, 0 + 0 = (4, 0)
Check: 4 >= 4 → Out of bounds ❌
Skip
```

**Neighbor 3: Left (0, -1)**
```
nx, ny = 3 + 0, 0 + (-1) = (3, -1)
Check: -1 < 0 → Out of bounds ❌
Skip
```

**Neighbor 4: Right (0, 1)**
```
nx, ny = 3 + 0, 0 + 1 = (3, 1)
Check: Valid ✅
Check: board[3][1] = -1 (wall) ❌
Skip
```

**After processing (3, 0):**
```
distance matrix:
    0    1    2    3
0  ∞    ∞    0    1
1  ∞    ∞    1    ∞
2  1    ∞    ∞    ∞
3  0    ∞    ∞    ∞

queue = [(1, 2), (0, 3), (2, 0)]
```

### Step 4: Continue BFS - Process (1, 2)

```
Pop: (1, 2) from queue
Current distance: distance[1][2] = 1

Explore neighbors:
  Up (0, 2): Already visited (distance = 0) → Skip
  Down (2, 2): 
    board[2][2] = 0, distance[2][2] = ∞
    distance[2][2] = 1 + 1 = 2
    queue.append((2, 2))
  Left (1, 1):
    board[1][1] = 0, distance[1][1] = ∞
    distance[1][1] = 1 + 1 = 2
    queue.append((1, 1))
  Right (1, 3):
    board[1][3] = -1 (wall) → Skip
```

**After processing (1, 2):**
```
distance matrix:
    0    1    2    3
0  ∞    ∞    0    1
1  ∞    2    1    ∞
2  1    ∞    2    ∞
3  0    ∞    ∞    ∞

queue = [(0, 3), (2, 0), (2, 2), (1, 1)]
```

### Step 5: Continue BFS - Process (0, 3)

```
Pop: (0, 3) from queue
Current distance: distance[0][3] = 1

Explore neighbors:
  Up (-1, 3): Out of bounds → Skip
  Down (1, 3): Wall → Skip
  Left (0, 2): Already visited → Skip
  Right (0, 4): Out of bounds → Skip
```

**No new cells added.**

### Step 6: Continue BFS - Process (2, 0)

```
Pop: (2, 0) from queue
Current distance: distance[2][0] = 1

Explore neighbors:
  Up (1, 0):
    board[1][0] = 0, distance[1][0] = ∞
    distance[1][0] = 1 + 1 = 2
    queue.append((1, 0))
  Down (3, 0): Already visited → Skip
  Left (2, -1): Out of bounds → Skip
  Right (2, 1): Wall → Skip
```

**After processing (2, 0):**
```
distance matrix:
    0    1    2    3
0  ∞    ∞    0    1
1  2    ∞    1    ∞
2  1    ∞    2    ∞
3  0    ∞    ∞    ∞

queue = [(2, 2), (1, 1), (1, 0)]
```

### Step 7: Continue BFS - Process Remaining Cells

**Process (2, 2):**
```
distance[2][2] = 2
Neighbors:
  Up (1, 2): Already visited
  Down (3, 2):
    board[3][2] = 0, distance[3][2] = ∞
    distance[3][2] = 2 + 1 = 3
    queue.append((3, 2))
  Left (2, 1): Wall
  Right (2, 3): Wall
```

**Process (1, 1):**
```
distance[1][1] = 2
Neighbors:
  Up (0, 1): Wall
  Down (2, 1): Wall
  Left (1, 0): Already visited (distance = 2)
  Right (1, 2): Already visited
```

**Process (1, 0):**
```
distance[1][0] = 2
Neighbors:
  Up (0, 0):
    board[0][0] = 0, distance[0][0] = ∞
    distance[0][0] = 2 + 1 = 3
    queue.append((0, 0))
  Down (2, 0): Already visited
  Left (1, -1): Out of bounds
  Right (1, 1): Already visited
```

**Process (3, 2):**
```
distance[3][2] = 3
Neighbors:
  Up (2, 2): Already visited
  Down (4, 2): Out of bounds
  Left (3, 1): Wall
  Right (3, 3):
    board[3][3] = 0, distance[3][3] = ∞
    distance[3][3] = 3 + 1 = 4
    queue.append((3, 3))
```

**Process (0, 0):**
```
distance[0][0] = 3
Neighbors:
  Up (-1, 0): Out of bounds
  Down (1, 0): Already visited
  Left (0, -1): Out of bounds
  Right (0, 1): Wall
```

**Process (3, 3):**
```
distance[3][3] = 4
Neighbors:
  Up (2, 3): Wall
  Down (4, 3): Out of bounds
  Left (3, 2): Already visited
  Right (3, 4): Out of bounds
```

### Final Distance Matrix

```
distance matrix (after BFS completes):
    0    1    2    3
0   3    ∞    0    1
1   2    ∞    1    ∞
2   1    ∞    2    ∞
3   0    ∞    3    4

Interpretation:
  - distance[0][0] = 3: 3 steps from nearest cat
  - distance[3][3] = 4: 4 steps from nearest cat (FARTHEST!)
  - ∞ means unreachable (walls)
```

### Step 8: Find Maximum Distance

```
Scan all empty cells (board[r][c] == 0):

(0, 0): distance = 3
  max_distance = -1 → 3 > -1
  max_distance = 3
  result = [(0, 0)]

(0, 3): distance = 1
  1 < 3 → Skip

(1, 0): distance = 2
  2 < 3 → Skip

(1, 1): distance = 2
  2 < 3 → Skip

(1, 2): distance = 1
  1 < 3 → Skip

(2, 0): distance = 1
  1 < 3 → Skip

(2, 2): distance = 2
  2 < 3 → Skip

(3, 0): distance = 0 (cat position, but board[3][0] = 1, not 0)
  Skip (not empty space)

(3, 2): distance = 3
  3 == 3 → Add to result
  result = [(0, 0), (3, 2)]

(3, 3): distance = 4
  4 > 3 → Update
  max_distance = 4
  result = [(3, 3)]
```

**Final Result:**
```
result = [(3, 3)]
max_distance = 4

Position (3, 3) is farthest from all cats with distance 4.
```

---

## Visual BFS Expansion

```
Initial state (C = cat, W = wall, . = empty):
    0  1  2  3
0   .  W  C  .
1   .  .  .  W
2   .  W  .  W
3   C  W  .  .

After BFS (numbers = distance from nearest cat):
    0  1  2  3
0   3  W  0  1
1   2  .  1  W
2   1  W  2  W
3   0  W  3  4

Expansion visualization:
Level 0: C  (cats at distance 0)
Level 1: 1  (1 step from cats)
Level 2: 2  (2 steps from cats)
Level 3: 3  (3 steps from cats)
Level 4: 4  (4 steps from cats) ← Farthest!
```

---

## Key Concepts

### 1. Multi-Source BFS

**Traditional BFS**: Starts from one source
**Multi-Source BFS**: Starts from multiple sources simultaneously

**Why use Multi-Source BFS?**
- We want distance from ANY cat (not a specific cat)
- Starting from all cats ensures we find minimum distance
- More efficient than running BFS from each cat separately

### 2. Distance Calculation

**`distance[i][j]`** = shortest distance from ANY cat to cell (i, j)

**How it works:**
- BFS explores level by level (distance 0, 1, 2, ...)
- First time a cell is reached = shortest path
- `distance[nx][ny] = distance[x][y] + 1` adds one step

### 3. Why Check `distance[nx][ny] == float('inf')`?

This ensures we only update unvisited cells:
- If a cell is already visited, we've found a shorter path
- BFS guarantees first visit = shortest path
- Revisiting would give longer (incorrect) distance

### 4. Why Skip Walls?

Walls cannot be traversed:
- `board[nx][ny] == -1` means blocked
- Don't add to queue
- Don't update distance

### 5. Finding Maximum Distance

After BFS completes:
- `distance[i][j]` contains shortest distance from any cat
- Scan all empty cells
- Find maximum distance
- Return all cells with that maximum

---

## Algorithm Pseudocode

```python
def farthest_positions(board):
    # Initialize
    rows, cols = len(board), len(board[0])
    distance = [[infinity] * cols for _ in range(rows)]
    queue = deque()
    
    # Step 1: Add all cats to queue
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:  # Cat
                queue.append((r, c))
                distance[r][c] = 0
    
    # Step 2: Multi-Source BFS
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if valid(nx, ny) and board[nx][ny] == 0:
                if distance[nx][ny] == infinity:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
    
    # Step 3: Find maximum distance
    max_dist = -1
    result = []
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 0:
                if distance[r][c] > max_dist:
                    max_dist = distance[r][c]
                    result = [(r, c)]
                elif distance[r][c] == max_dist:
                    result.append((r, c))
    
    return result
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(m × n) | Each cell visited at most once in BFS, then scan all cells |
| **Space** | O(m × n) | Distance matrix (m×n), queue stores at most O(m×n) cells |

---

## Edge Cases

### Case 1: No Cats
```
board = [[0, 0], [0, 0]]
Result: [] (no cats, no farthest positions)
```

### Case 2: All Walls
```
board = [[-1, -1], [-1, -1]]
Result: [] (no empty spaces)
```

### Case 3: Single Cat, Single Empty Cell
```
board = [[1, 0]]
Result: [(0, 1)] (only one empty cell)
```

### Case 4: Multiple Equally Far Positions
```
board = [
  [1, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
Result: [(2, 2)] (or other corner positions with same distance)
```

### Case 5: Unreachable Cells
```
board = [
  [1, -1, 0],
  [-1, -1, 0]
]
Result: [] (empty cells are unreachable due to walls)
```

---

## Why This Algorithm Works

### Correctness

1. **Multi-Source BFS**: Finds shortest distance from ANY cat to each cell
2. **BFS Property**: First visit = shortest path (guaranteed by BFS)
3. **Maximum Finding**: After BFS, finding max distance gives farthest cells

### Completeness

- All reachable empty cells are visited
- Distance from each cell to nearest cat is calculated
- Maximum distance is found correctly

### Efficiency

- Each cell visited once in BFS: O(m×n)
- Final scan: O(m×n)
- Total: O(m×n) - optimal!

---

## Comparison: Single-Source vs Multi-Source BFS

### Single-Source BFS (from each cat separately):
```
For each cat:
  Run BFS from that cat
  Update distances (take minimum)

Time: O(k × m × n) where k = number of cats
```

### Multi-Source BFS (from all cats at once):
```
Add all cats to queue
Run BFS once
Distances automatically minimum

Time: O(m × n) - much better!
```

**Multi-Source BFS is more efficient!**

---

## Summary

The walls and gates algorithm:
- Uses **Multi-Source BFS** starting from all cat positions
- Calculates shortest distance from ANY cat to each empty cell
- Finds cells with maximum such distance
- Time complexity: **O(m × n)**
- Space complexity: **O(m × n)**

**Key Insight**: Multi-Source BFS efficiently finds minimum distances from multiple sources simultaneously. The cell with maximum minimum distance is farthest from all cats.

---

## Related Problems

- **LeetCode 286**: Walls and Gates (similar problem)
- **LeetCode 542**: 01 Matrix (multi-source BFS)
- **LeetCode 994**: Rotting Oranges (multi-source BFS)
- **LeetCode 1162**: As Far from Land as Possible

# Traffic Light - Earliest Arrival Time

> **Problem**: Given a city map where each cell has a traffic light that turns green at a specific time, find the earliest time to reach the bottom-right corner starting from the top-left corner. You can only move right or down, and you must wait at each cell until its traffic light turns green.

## Problem Description

Find the earliest arrival time at the destination in a grid with traffic lights.

**Rules:**
- Start at top-left corner (0, 0)
- Goal: Reach bottom-right corner
- Can only move right or down
- Each cell `(r, c)` has a traffic light that turns green at time `city_map[r][c]`
- When you reach a cell, you must wait until the light turns green
- Movement takes 1 time unit (implicit in the algorithm)

**Example:**
```
city_map = [
    [1, 2, 0, 3],
    [4, 6, 5, 1],
    [9, 2, 5, 7],
    [5, 4, 2, 2]
]
```

---

## Key Insight

**Dijkstra's Algorithm Variant:**
- Use priority queue (min-heap) to always process the cell with earliest arrival time
- Track minimum time to reach each cell
- When moving to a new cell, arrival time = `max(current_time, traffic_light_time)`
- This ensures we wait until the light turns green

**Why Dijkstra's?**
- Finds shortest path in weighted graph
- Grid with time constraints is a graph problem
- Priority queue ensures we process cells in order of earliest arrival

---

## Algorithm Logic

```
1. Initialize:
   - Priority queue: (time, row, col) starting at (0,0)
   - min_time[r][c] = minimum time to reach cell (r,c)
   - min_time[0][0] = city_map[0][0]

2. While queue not empty:
   a. Pop cell with earliest time
   b. If destination reached, return time
   c. For each neighbor (right, down):
      - Calculate next_time = max(current_time, traffic_light_time)
      - If next_time < min_time[neighbor]:
        - Update min_time[neighbor]
        - Add to priority queue

3. Return -1 if destination unreachable
```

---

## Detailed Example: Step-by-Step

**Input**: 
```python
city_map = [
    [1, 2, 0, 3],
    [4, 6, 5, 1],
    [9, 2, 5, 7],
    [5, 4, 2, 2]
]
```

### Grid Visualization

```
    0   1   2   3
0 [ 1   2   0   3 ]
1 [ 4   6   5   1 ]
2 [ 9   2   5   7 ]
3 [ 5   4   2   2 ]

Traffic light times (when light turns green)
```

### Step-by-Step Execution

#### Step 1: Initialize

```
rows = 4, cols = 4

Priority Queue:
  pq = [(1, 0, 0)]  # (time, row, col) starting at (0,0) with time 1

Min Time Matrix:
  min_time = [
    [1, inf, inf, inf],
    [inf, inf, inf, inf],
    [inf, inf, inf, inf],
    [inf, inf, inf, inf]
  ]

Directions: [(0, 1), (1, 0)]  # right, down
```

#### Step 2: Iteration 1

```
Pop: (time=1, r=0, c=0)

Check destination:
  r == 3 and c == 3? NO (we're at (0,0))

Explore neighbors:
  Right: (0, 1)
    nr, nc = 0, 1
    In bounds? YES
    next_time = max(1, city_map[0][1]) = max(1, 2) = 2
    min_time[0][1] = inf
    2 < inf? YES ✅
      min_time[0][1] = 2
      pq.push((2, 0, 1))
  
  Down: (1, 0)
    nr, nc = 1, 0
    In bounds? YES
    next_time = max(1, city_map[1][0]) = max(1, 4) = 4
    min_time[1][0] = inf
    4 < inf? YES ✅
      min_time[1][0] = 4
      pq.push((4, 1, 0))
```

**After Iteration 1:**
```
pq = [(2, 0, 1), (4, 1, 0)]  # Min-heap: 2 comes first
min_time = [
    [1, 2, inf, inf],
    [4, inf, inf, inf],
    [inf, inf, inf, inf],
    [inf, inf, inf, inf]
]
```

#### Step 3: Iteration 2

```
Pop: (time=2, r=0, c=1)

Check destination: NO

Explore neighbors:
  Right: (0, 2)
    nr, nc = 0, 2
    next_time = max(2, city_map[0][2]) = max(2, 0) = 2
    (Light is already green at time 0, but we arrive at time 2)
    min_time[0][2] = inf
    2 < inf? YES ✅
      min_time[0][2] = 2
      pq.push((2, 0, 2))
  
  Down: (1, 1)
    nr, nc = 1, 1
    next_time = max(2, city_map[1][1]) = max(2, 6) = 6
    min_time[1][1] = inf
    6 < inf? YES ✅
      min_time[1][1] = 6
      pq.push((6, 1, 1))
```

**After Iteration 2:**
```
pq = [(2, 0, 2), (4, 1, 0), (6, 1, 1)]
min_time = [
    [1, 2, 2, inf],
    [4, 6, inf, inf],
    [inf, inf, inf, inf],
    [inf, inf, inf, inf]
]
```

#### Step 4: Iteration 3

```
Pop: (time=2, r=0, c=2)

Check destination: NO

Explore neighbors:
  Right: (0, 3)
    nr, nc = 0, 3
    next_time = max(2, city_map[0][3]) = max(2, 3) = 3
    min_time[0][3] = inf
    3 < inf? YES ✅
      min_time[0][3] = 3
      pq.push((3, 0, 3))
  
  Down: (1, 2)
    nr, nc = 1, 2
    next_time = max(2, city_map[1][2]) = max(2, 5) = 5
    min_time[1][2] = inf
    5 < inf? YES ✅
      min_time[1][2] = 5
      pq.push((5, 1, 2))
```

**After Iteration 3:**
```
pq = [(3, 0, 3), (4, 1, 0), (5, 1, 2), (6, 1, 1)]
min_time = [
    [1, 2, 2, 3],
    [4, 6, 5, inf],
    [inf, inf, inf, inf],
    [inf, inf, inf, inf]
]
```

#### Step 5: Iteration 4

```
Pop: (time=3, r=0, c=3)

Check destination: NO (we're at top-right, not bottom-right)

Explore neighbors:
  Down: (1, 3)
    nr, nc = 1, 3
    next_time = max(3, city_map[1][3]) = max(3, 1) = 3
    (Light turns green at 1, but we arrive at 3, so we can go immediately)
    min_time[1][3] = inf
    3 < inf? YES ✅
      min_time[1][3] = 3
      pq.push((3, 1, 3))
```

**After Iteration 4:**
```
pq = [(3, 1, 3), (4, 1, 0), (5, 1, 2), (6, 1, 1)]
min_time = [
    [1, 2, 2, 3],
    [4, 6, 5, 3],
    [inf, inf, inf, inf],
    [inf, inf, inf, inf]
]
```

#### Step 6: Iteration 5

```
Pop: (time=3, r=1, c=3)

Check destination: NO

Explore neighbors:
  Down: (2, 3)
    nr, nc = 2, 3
    next_time = max(3, city_map[2][3]) = max(3, 7) = 7
    min_time[2][3] = inf
    7 < inf? YES ✅
      min_time[2][3] = 7
      pq.push((7, 2, 3))
```

**After Iteration 5:**
```
pq = [(4, 1, 0), (5, 1, 2), (6, 1, 1), (7, 2, 3)]
min_time = [
    [1, 2, 2, 3],
    [4, 6, 5, 3],
    [inf, inf, inf, 7],
    [inf, inf, inf, inf]
]
```

#### Step 7: Iteration 6

```
Pop: (time=4, r=1, c=0)

Check destination: NO

Explore neighbors:
  Right: (1, 1)
    nr, nc = 1, 1
    next_time = max(4, city_map[1][1]) = max(4, 6) = 6
    min_time[1][1] = 6
    6 < 6? NO (already have time 6)
    Skip (not better)
  
  Down: (2, 0)
    nr, nc = 2, 0
    next_time = max(4, city_map[2][0]) = max(4, 9) = 9
    min_time[2][0] = inf
    9 < inf? YES ✅
      min_time[2][0] = 9
      pq.push((9, 2, 0))
```

**After Iteration 6:**
```
pq = [(5, 1, 2), (6, 1, 1), (7, 2, 3), (9, 2, 0)]
min_time = [
    [1, 2, 2, 3],
    [4, 6, 5, 3],
    [9, inf, inf, 7],
    [inf, inf, inf, inf]
]
```

#### Step 8: Iteration 7

```
Pop: (time=5, r=1, c=2)

Check destination: NO

Explore neighbors:
  Right: (1, 3)
    nr, nc = 1, 3
    next_time = max(5, city_map[1][3]) = max(5, 1) = 5
    min_time[1][3] = 3
    5 < 3? NO ❌
    Skip (already have better time 3)
  
  Down: (2, 2)
    nr, nc = 2, 2
    next_time = max(5, city_map[2][2]) = max(5, 5) = 5
    min_time[2][2] = inf
    5 < inf? YES ✅
      min_time[2][2] = 5
      pq.push((5, 2, 2))
```

**After Iteration 7:**
```
pq = [(5, 2, 2), (6, 1, 1), (7, 2, 3), (9, 2, 0)]
min_time = [
    [1, 2, 2, 3],
    [4, 6, 5, 3],
    [9, inf, 5, 7],
    [inf, inf, inf, inf]
]
```

#### Step 9: Iteration 8

```
Pop: (time=5, r=2, c=2)

Check destination: NO

Explore neighbors:
  Right: (2, 3)
    nr, nc = 2, 3
    next_time = max(5, city_map[2][3]) = max(5, 7) = 7
    min_time[2][3] = 7
    7 < 7? NO ❌
    Skip (already have time 7)
  
  Down: (3, 2)
    nr, nc = 3, 2
    next_time = max(5, city_map[3][2]) = max(5, 2) = 5
    min_time[3][2] = inf
    5 < inf? YES ✅
      min_time[3][2] = 5
      pq.push((5, 3, 2))
```

**After Iteration 8:**
```
pq = [(5, 3, 2), (6, 1, 1), (7, 2, 3), (9, 2, 0)]
min_time = [
    [1, 2, 2, 3],
    [4, 6, 5, 3],
    [9, inf, 5, 7],
    [inf, inf, 5, inf]
]
```

#### Step 10: Iteration 9

```
Pop: (time=5, r=3, c=2)

Check destination: NO (we're at (3,2), need (3,3))

Explore neighbors:
  Right: (3, 3)
    nr, nc = 3, 3
    next_time = max(5, city_map[3][3]) = max(5, 2) = 5
    min_time[3][3] = inf
    5 < inf? YES ✅
      min_time[3][3] = 5
      pq.push((5, 3, 3))
```

**After Iteration 9:**
```
pq = [(5, 3, 3), (6, 1, 1), (7, 2, 3), (9, 2, 0)]
min_time = [
    [1, 2, 2, 3],
    [4, 6, 5, 3],
    [9, inf, 5, 7],
    [inf, inf, 5, 5]
]
```

#### Step 11: Iteration 10

```
Pop: (time=5, r=3, c=3)

Check destination:
  r == 3 and c == 3? YES ✅
  
Return time = 5
```

**Result**: `5` ✅

**Path taken**: (0,0) → (0,1) → (0,2) → (1,2) → (2,2) → (3,2) → (3,3)
- Times: 1 → 2 → 2 → 5 → 5 → 5 → 5

---

## Key Concepts

### 1. Dijkstra's Algorithm

**Why Dijkstra's?**
- Finds shortest path in weighted graph
- Grid with time constraints is a graph problem
- Priority queue ensures we process cells in order of earliest arrival

**Key Properties:**
- Always processes the cell with earliest arrival time first
- Once a cell is processed, we've found the shortest path to it
- Guarantees optimal solution

### 2. Traffic Light Constraint

**Rule**: When you reach a cell, you must wait until the light turns green

**Implementation**: `next_time = max(current_time, city_map[nr][nc])`

**Why max?**
- If `current_time >= traffic_light_time`: light is already green, proceed immediately
- If `current_time < traffic_light_time`: must wait until light turns green

**Example:**
```
Current time = 2, traffic_light_time = 5
next_time = max(2, 5) = 5 (wait 3 time units)

Current time = 6, traffic_light_time = 3
next_time = max(6, 3) = 6 (light already green, proceed)
```

### 3. Priority Queue (Min-Heap)

**Structure**: `(time, row, col)`

**Why priority queue?**
- Always process cell with earliest arrival time
- Ensures we find shortest path
- Similar to Dijkstra's algorithm

**Example:**
```
pq = [(2, 0, 1), (4, 1, 0), (6, 1, 1)]
Pop: (2, 0, 1)  (earliest time first)
```

### 4. Min Time Tracking

**Purpose**: Avoid processing cells multiple times unnecessarily

**Rule**: Only update if `next_time < min_time[nr][nc]`

**Why?**
- If we've already found a path with earlier time, skip
- Reduces redundant processing
- Ensures optimal solution

### 5. Movement Constraints

**Only Right and Down:**
- Can't go left or up
- This ensures we make progress toward destination
- Prevents cycles

**Directions**: `[(0, 1), (1, 0)]`
- `(0, 1)`: right (same row, next column)
- `(1, 0)`: down (next row, same column)

---

## Algorithm Pseudocode

```python
def earliest_arrival_time(city_map):
    rows, cols = len(city_map), len(city_map[0])
    
    # Initialize
    pq = [(city_map[0][0], 0, 0)]  # (time, row, col)
    min_time = [[inf] * cols for _ in range(rows)]
    min_time[0][0] = city_map[0][0]
    directions = [(0, 1), (1, 0)]  # right, down
    
    while pq:
        time, r, c = heapq.heappop(pq)
        
        # Check destination
        if r == rows - 1 and c == cols - 1:
            return time
        
        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                # Wait until light turns green
                next_time = max(time, city_map[nr][nc])
                
                # Update if found better path
                if next_time < min_time[nr][nc]:
                    min_time[nr][nc] = next_time
                    heapq.heappush(pq, (next_time, nr, nc))
    
    return -1  # Unreachable
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(R × C × log(R × C)) | R = rows, C = cols. Each cell processed at most once, heap operations O(log(R×C)) |
| **Space** | O(R × C) | Priority queue O(R×C), min_time matrix O(R×C) |

**Where:**
- R = number of rows
- C = number of columns

**Time Complexity:**
- Each cell added to heap at most once: O(R × C)
- Each heap operation: O(log(R × C))
- Total: O(R × C × log(R × C))

**Space Complexity:**
- Priority queue: O(R × C) in worst case
- Min_time matrix: O(R × C)
- Total: O(R × C)

---

## Edge Cases

### Case 1: Single Cell
```
city_map = [[5]]
Result: 5 ✅ (start and destination are same)
```

### Case 2: Single Row
```
city_map = [[1, 2, 3, 4]]
Result: max(1, 2, 3, 4) = 4 ✅
```

### Case 3: Single Column
```
city_map = [[1], [2], [3], [4]]
Result: max(1, 2, 3, 4) = 4 ✅
```

### Case 4: All Same Time
```
city_map = [[5, 5], [5, 5]]
Result: 5 ✅
```

### Case 5: Very Large Times
```
city_map = [[1, 100], [100, 1]]
Result: 100 (must wait at (1,0) or (0,1))
```

---

## Why This Algorithm Works

### Correctness

1. **Dijkstra's Guarantees Optimality:**
   - Always processes cell with earliest arrival time first
   - Once processed, we've found shortest path to that cell
   - Guarantees optimal solution

2. **Traffic Light Constraint:**
   - `max(time, traffic_light_time)` correctly handles waiting
   - Ensures we never proceed before light turns green

3. **Min Time Tracking:**
   - Prevents redundant processing
   - Ensures we only update when finding better path

### Why Dijkstra's?

**This is a shortest path problem:**
- Grid is a graph
- Edges have weights (time to traverse)
- Traffic lights add constraints
- Dijkstra's finds shortest path in weighted graph

**Why Priority Queue?**
- Need to process cells in order of arrival time
- Priority queue gives us minimum time cell efficiently
- Ensures optimal solution

---

## Alternative Approaches

### 1. Dynamic Programming

**Idea**: `dp[r][c] = min time to reach (r,c)`

```python
def earliest_arrival_time_dp(city_map):
    rows, cols = len(city_map), len(city_map[0])
    dp = [[inf] * cols for _ in range(rows)]
    dp[0][0] = city_map[0][0]
    
    for r in range(rows):
        for c in range(cols):
            if r > 0:
                dp[r][c] = min(dp[r][c], max(dp[r-1][c], city_map[r][c]))
            if c > 0:
                dp[r][c] = min(dp[r][c], max(dp[r][c-1], city_map[r][c]))
    
    return dp[rows-1][cols-1]
```

**Time**: O(R × C), **Space**: O(R × C)

**Why DP works:**
- Can only move right/down, so no cycles
- Can process in row-major or column-major order
- Simpler than Dijkstra's for this specific constraint

### 2. BFS with Time Tracking

**Idea**: BFS with time as "distance"

**Complexity**: Similar to Dijkstra's
**Less efficient**: Processes cells multiple times

---

## Visual Timeline

### Example: `city_map = [[1, 2, 0, 3], [4, 6, 5, 1], [9, 2, 5, 7], [5, 4, 2, 2]]`

```
Iteration | Pop Cell | Time | Explore | Priority Queue
----------|----------|------|---------|------------------
1         | (0,0)    | 1    | (0,1):2, (1,0):4 | [(2,0,1), (4,1,0)]
2         | (0,1)    | 2    | (0,2):2, (1,1):6 | [(2,0,2), (4,1,0), (6,1,1)]
3         | (0,2)    | 2    | (0,3):3, (1,2):5 | [(3,0,3), (4,1,0), (5,1,2), (6,1,1)]
4         | (0,3)    | 3    | (1,3):3 | [(3,1,3), (4,1,0), (5,1,2), (6,1,1)]
5         | (1,3)    | 3    | (2,3):7 | [(4,1,0), (5,1,2), (6,1,1), (7,2,3)]
6         | (1,0)    | 4    | (2,0):9 | [(5,1,2), (6,1,1), (7,2,3), (9,2,0)]
7         | (1,2)    | 5    | (2,2):5 | [(5,2,2), (6,1,1), (7,2,3), (9,2,0)]
8         | (2,2)    | 5    | (3,2):5 | [(5,3,2), (6,1,1), (7,2,3), (9,2,0)]
9         | (3,2)    | 5    | (3,3):5 | [(5,3,3), (6,1,1), (7,2,3), (9,2,0)]
10        | (3,3)    | 5    | DESTINATION! | Return 5 ✅
```

**Path**: (0,0) → (0,1) → (0,2) → (1,2) → (2,2) → (3,2) → (3,3)

---

## Real-World Applications

1. **Traffic Management:**
   - Route planning with traffic lights
   - Navigation systems

2. **Game Development:**
   - Pathfinding with time constraints
   - Puzzle games

3. **Network Routing:**
   - Find fastest path with delays
   - Resource scheduling

4. **Logistics:**
   - Delivery route optimization
   - Time-constrained routing

---

## Common Mistakes

### Mistake 1: Not Using Max for Traffic Light

```python
# WRONG: Doesn't wait for light
next_time = time + 1  # or city_map[nr][nc]
```

**Fix:** Use `max(time, city_map[nr][nc])`

### Mistake 2: Not Tracking Min Time

```python
# WRONG: Processes cells multiple times
if next_time < min_time[nr][nc]:
    # Missing: update min_time
    heapq.heappush(pq, (next_time, nr, nc))
```

**Fix:** Always update `min_time[nr][nc]`

### Mistake 3: Wrong Comparison

```python
# WRONG: Using <= instead of <
if next_time <= min_time[nr][nc]:
```

**Fix:** Use `<` to avoid redundant processing

---

## Summary

The traffic light algorithm:
- Uses **Dijkstra's algorithm** with priority queue
- Handles **traffic light constraints** with `max(time, light_time)`
- Tracks **minimum time** to each cell
- Only moves **right and down**
- Time complexity: **O(R × C × log(R × C))**
- Space complexity: **O(R × C)**

**Key Insight**: This is a shortest path problem where edge weights depend on traffic light timings. Dijkstra's algorithm finds the optimal path by always processing the cell with earliest arrival time first.

---

## Related Problems

- **LeetCode 1631**: Path With Minimum Effort (similar grid pathfinding)
- **LeetCode 787**: Cheapest Flights Within K Stops (weighted graph)
- **LeetCode 743**: Network Delay Time (Dijkstra's algorithm)
- **Grid Pathfinding**: Various shortest path problems in grids

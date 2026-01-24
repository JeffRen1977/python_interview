# Number of Circle Groups (Connected Components)

> **Problem**: Given a list of circles (each with center coordinates and radius), find groups of overlapping circles. Two circles are in the same group if they overlap (directly or indirectly through other overlapping circles).

## Problem Description

Group circles based on overlap relationships:
- **Direct Overlap**: Two circles overlap if the distance between their centers is ≤ sum of their radii
- **Indirect Overlap**: Circles are in the same group if there's a chain of overlapping circles connecting them
- **Goal**: Count groups, check if all circles form one group, or find the largest groups

**Example:**
```
Circle A: center (0,0), radius 1
Circle B: center (1,1), radius 2  → Overlaps with A
Circle C: center (5,5), radius 1  → Does not overlap with A or B

Groups:
  Group 1: {A, B}  (overlap)
  Group 2: {C}     (isolated)
Total: 2 groups
```

---

## Key Insight

**Graph Representation:**
- Circles are **nodes** in a graph
- Overlapping circles are connected by **edges**
- Groups are **connected components** in the graph
- Use **DFS** to find all circles in each connected component

**Algorithm Approach:**
1. Build adjacency list: For each circle, list all overlapping circles
2. Use DFS to traverse and mark all circles in each connected component
3. Count distinct components (groups)

---

## Algorithm Logic

```
1. IsOverlapped(circle1, circle2):
   - Calculate distance between centers
   - Check if distance <= r1 + r2

2. ConstructAdjacencyDict(circles):
   - For each pair of circles:
     - If they overlap, add edge between them
   - Return adjacency list

3. DFS(node, adjacency_dict, current_group):
   - Mark node as visited
   - Recursively visit all neighbors
   - Collect all nodes in current_group

4. CountGroups(circles):
   - For each unvisited circle:
     - Start DFS to find its group
     - Count groups

5. GetTopKGroups(circles, k):
   - Find all groups
   - Sort by size
   - Return top k largest
```

---

## Detailed Example: Step-by-Step

**Input**: 
```python
circles = [
    Circle(0, 0, 1),   # A: center (0,0), radius 1
    Circle(2, 2, 1),   # B: center (2,2), radius 1
    Circle(4, 4, 1),   # C: center (4,4), radius 1
    Circle(6, 6, 1),   # D: center (6,6), radius 1
    Circle(1, 1, 2),   # E: center (1,1), radius 2
    Circle(5, 5, 2)    # F: center (5,5), radius 2
]
```

### Visual Representation

```
Circle A: (0,0) r=1
Circle B: (2,2) r=1
Circle C: (4,4) r=1
Circle D: (6,6) r=1
Circle E: (1,1) r=2  (large circle)
Circle F: (5,5) r=2  (large circle)

Visual:
  A(0,0)     B(2,2)     C(4,4)     D(6,6)
    ●          ●          ●          ●
     \        /            \        /
      \      /              \      /
       E(1,1)                F(5,5)
         ●                      ●
      (large)               (large)

Overlaps:
  A ↔ E (distance ≈ 1.41, sum of radii = 3)
  B ↔ E (distance ≈ 1.41, sum of radii = 3)
  C ↔ F (distance ≈ 1.41, sum of radii = 3)
  D ↔ F (distance ≈ 1.41, sum of radii = 3)
  
Groups:
  Group 1: {A, B, E}  (A-E-B chain)
  Group 2: {C, D, F}  (C-F-D chain)
```

### Step 1: Check Overlaps

#### Check A and E

```
Circle A: (0, 0), r=1
Circle E: (1, 1), r=2

Distance = sqrt((0-1)² + (0-1)²) = sqrt(1 + 1) = sqrt(2) ≈ 1.41
Sum of radii = 1 + 2 = 3

1.41 <= 3? YES ✅
A and E overlap!
```

#### Check B and E

```
Circle B: (2, 2), r=1
Circle E: (1, 1), r=2

Distance = sqrt((2-1)² + (2-1)²) = sqrt(1 + 1) = sqrt(2) ≈ 1.41
Sum of radii = 1 + 2 = 3

1.41 <= 3? YES ✅
B and E overlap!
```

#### Check C and F

```
Circle C: (4, 4), r=1
Circle F: (5, 5), r=2

Distance = sqrt((4-5)² + (4-5)²) = sqrt(1 + 1) = sqrt(2) ≈ 1.41
Sum of radii = 1 + 2 = 3

1.41 <= 3? YES ✅
C and F overlap!
```

#### Check D and F

```
Circle D: (6, 6), r=1
Circle F: (5, 5), r=2

Distance = sqrt((6-5)² + (6-5)²) = sqrt(1 + 1) = sqrt(2) ≈ 1.41
Sum of radii = 1 + 2 = 3

1.41 <= 3? YES ✅
D and F overlap!
```

#### Check Other Pairs

```
A and B: distance = sqrt(8) ≈ 2.83, sum = 2 → 2.83 > 2? NO ❌
A and C: distance = sqrt(32) ≈ 5.66, sum = 2 → 5.66 > 2? NO ❌
... (all other pairs don't overlap)
```

### Step 2: Construct Adjacency Dictionary

```
Initialize: adjacency_dict = {
    A: set(),
    B: set(),
    C: set(),
    D: set(),
    E: set(),
    F: set()
}

Process pairs:
  A-E: overlap → add E to A, add A to E
  B-E: overlap → add E to B, add B to E
  C-F: overlap → add F to C, add C to F
  D-F: overlap → add F to D, add D to F

Final adjacency_dict:
  A: {E}
  B: {E}
  C: {F}
  D: {F}
  E: {A, B}
  F: {C, D}
```

### Step 3: Count Groups (DFS Traversal)

#### Process Circle A

```
visited = set()
total_groups = 0

Circle A not in visited? YES
  current_group = set()
  Call: DFS(A, adjacency_dict, current_group)
```

#### DFS from A

```
DFS(A, adjacency_dict, current_group):
  A in current_group? NO
  current_group.add(A)  → current_group = {A}
  
  Neighbors of A: {E}
  
  Process E:
    DFS(E, adjacency_dict, current_group)
```

#### DFS from E

```
DFS(E, adjacency_dict, current_group):
  E in current_group? NO
  current_group.add(E)  → current_group = {A, E}
  
  Neighbors of E: {A, B}
  
  Process A:
    DFS(A, adjacency_dict, current_group)
      A in current_group? YES → Return (already visited)
  
  Process B:
    DFS(B, adjacency_dict, current_group)
```

#### DFS from B

```
DFS(B, adjacency_dict, current_group):
  B in current_group? NO
  current_group.add(B)  → current_group = {A, E, B}
  
  Neighbors of B: {E}
  
  Process E:
    DFS(E, adjacency_dict, current_group)
      E in current_group? YES → Return (already visited)
  
  Return
```

**Back to CountGroups:**
```
current_group = {A, E, B}
visited.update({A, E, B})  → visited = {A, E, B}
total_groups = 1
```

#### Process Circle C

```
Circle C not in visited? YES
  current_group = set()
  Call: DFS(C, adjacency_dict, current_group)
```

#### DFS from C

```
DFS(C, adjacency_dict, current_group):
  C in current_group? NO
  current_group.add(C)  → current_group = {C}
  
  Neighbors of C: {F}
  
  Process F:
    DFS(F, adjacency_dict, current_group)
```

#### DFS from F

```
DFS(F, adjacency_dict, current_group):
  F in current_group? NO
  current_group.add(F)  → current_group = {C, F}
  
  Neighbors of F: {C, D}
  
  Process C:
    DFS(C, adjacency_dict, current_group)
      C in current_group? YES → Return
  
  Process D:
    DFS(D, adjacency_dict, current_group)
```

#### DFS from D

```
DFS(D, adjacency_dict, current_group):
  D in current_group? NO
  current_group.add(D)  → current_group = {C, F, D}
  
  Neighbors of D: {F}
  
  Process F:
    DFS(F, adjacency_dict, current_group)
      F in current_group? YES → Return
  
  Return
```

**Back to CountGroups:**
```
current_group = {C, F, D}
visited.update({C, F, D})  → visited = {A, E, B, C, F, D}
total_groups = 2
```

#### Process Remaining Circles

```
Circle D: in visited? YES → Skip
Circle E: in visited? YES → Skip
Circle F: in visited? YES → Skip
```

**Result**: `CountGroups(circles) = 2`

**Groups:**
- Group 1: {A, B, E}
- Group 2: {C, D, F}

---

## Example 2: IsSingleGroup

**Input**: Same circles as above

### Step-by-Step Execution

```
Call: IsSingleGroup(circles)

Step 1: Check if empty
  circles is empty? NO

Step 2: Build adjacency_dict
  (same as before)

Step 3: Start DFS from circles[0] = A
  visited = set()
  DFS(A, adjacency_dict, visited)
  
  DFS traversal:
    A → E → B
    visited = {A, E, B}

Step 4: Check if all circles visited
  len(visited) = 3
  len(circles) = 6
  3 == 6? NO ❌
  
Result: False (not all circles in one group)
```

---

## Example 3: GetTopKGroups

**Input**: Same circles, `top_k = 2`

### Step-by-Step Execution

```
Call: GetTopKGroups(circles, 2)

Step 1: Initialize
  visited = set()
  size_and_groups = []
  adjacency_dict = (same as before)

Step 2: Find all groups
  Process A: Group 1 = {A, E, B}, size = 3
    size_and_groups.append((3, {A, E, B}))
  
  Process C: Group 2 = {C, F, D}, size = 3
    size_and_groups.append((3, {C, F, D}))
  
  size_and_groups = [(3, {A, E, B}), (3, {C, F, D})]

Step 3: Find top k largest
  largest_groups = heapq.nlargest(2, size_and_groups, key=lambda x: x[0])
  
  Both groups have size 3, so both are returned:
    [(3, {A, E, B}), (3, {C, F, D})]

Step 4: Convert to lists
  return [
    [A, E, B],
    [C, F, D]
  ]
```

---

## Key Concepts

### 1. Circle Overlap Detection

**Mathematical Formula:**
```
Two circles overlap if:
  distance(center1, center2) <= radius1 + radius2

Distance formula:
  distance = sqrt((x1 - x2)² + (y1 - y2)²)
```

**Visual:**
```
Circle 1: center (x1, y1), radius r1
Circle 2: center (x2, y2), radius r2

Overlap if: distance <= r1 + r2
```

**Example:**
```
Circle 1: (0, 0), r=2
Circle 2: (3, 0), r=2

Distance = sqrt((0-3)² + (0-0)²) = 3
Sum of radii = 2 + 2 = 4
3 <= 4? YES → Overlap ✅
```

### 2. Graph Representation

**Circles as Graph:**
- **Nodes**: Each circle is a node
- **Edges**: Two nodes are connected if circles overlap
- **Groups**: Connected components in the graph

**Adjacency List:**
```python
adjacency_dict = {
    circle1: {circle2, circle3},  # circle1 overlaps with circle2 and circle3
    circle2: {circle1},
    circle3: {circle1},
    circle4: set()  # circle4 doesn't overlap with anyone
}
```

### 3. Connected Components

**Definition**: A connected component is a set of nodes where:
- Every pair of nodes is connected by a path
- No node in the component is connected to nodes outside

**Finding Components:**
- Use DFS to traverse from a starting node
- All nodes reached form one component
- Repeat for unvisited nodes

### 4. DFS Traversal

**DFS Algorithm:**
```
def DFS(node, adjacency_dict, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in adjacency_dict[node]:
        DFS(neighbor, adjacency_dict, visited)
```

**Why DFS?**
- Naturally explores all nodes in a connected component
- Simple recursive implementation
- Efficient for finding components

### 5. Counting Groups

**Algorithm:**
```
visited = set()
groups = 0

for each circle:
    if circle not in visited:
        DFS(circle)  # Mark all circles in this group
        groups += 1
```

**Key Insight**: Each unvisited circle starts a new group.

---

## Algorithm Pseudocode

```python
def IsOverlapped(circle1, circle2):
    distance = sqrt((circle1.x - circle2.x)² + (circle1.y - circle2.y)²)
    return distance <= (circle1.r + circle2.r)

def ConstructAdjacencyDict(circles):
    adjacency_dict = {circle: set() for circle in circles}
    
    for i, circle1 in enumerate(circles):
        for j in range(i+1, len(circles)):
            circle2 = circles[j]
            if IsOverlapped(circle1, circle2):
                adjacency_dict[circle1].add(circle2)
                adjacency_dict[circle2].add(circle1)
    
    return adjacency_dict

def DFS(node, adjacency_dict, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in adjacency_dict[node]:
        DFS(neighbor, adjacency_dict, visited)

def CountGroups(circles):
    visited = set()
    adjacency_dict = ConstructAdjacencyDict(circles)
    groups = 0
    
    for circle in circles:
        if circle not in visited:
            DFS(circle, adjacency_dict, visited)
            groups += 1
    
    return groups
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(N²) | N = number of circles. Check all pairs O(N²), DFS O(N+E) where E ≤ N² |
| **Space** | O(N²) | Adjacency dict O(N²) in worst case (all circles overlap) |

**Where:**
- N = number of circles
- E = number of edges (overlapping pairs)

**Time Complexity Breakdown:**

**ConstructAdjacencyDict:**
- Check all pairs: O(N²)
- For each pair: O(1) overlap check
- Total: O(N²)

**DFS:**
- Visit each node once: O(N)
- Check each edge once: O(E)
- Total: O(N + E) ≤ O(N²)

**Overall:** O(N²)

**Space Complexity:**
- Adjacency dict: O(N²) in worst case (complete graph)
- Visited set: O(N)
- DFS recursion stack: O(N)
- Total: O(N²)

---

## Edge Cases

### Case 1: No Circles
```
circles = []
CountGroups([]) = 0
IsSingleGroup([]) = True (empty is trivially one group)
```

### Case 2: Single Circle
```
circles = [Circle(0, 0, 1)]
CountGroups(circles) = 1
IsSingleGroup(circles) = True
```

### Case 3: No Overlaps
```
circles = [
    Circle(0, 0, 1),
    Circle(10, 10, 1),
    Circle(20, 20, 1)
]
CountGroups(circles) = 3 (each circle is its own group)
```

### Case 4: All Overlap
```
circles = [
    Circle(0, 0, 5),
    Circle(1, 1, 5),
    Circle(2, 2, 5)
]
CountGroups(circles) = 1 (all in one group)
```

### Case 5: Nested Circles
```
circles = [
    Circle(0, 0, 10),  # Large circle
    Circle(0, 0, 5)    # Small circle inside
]
CountGroups(circles) = 1 (overlap, same group)
```

### Case 6: Chain of Overlaps
```
circles = [
    Circle(0, 0, 1),    # A
    Circle(2, 0, 1),    # B (overlaps with A)
    Circle(4, 0, 1),    # C (overlaps with B, not A)
    Circle(6, 0, 1)     # D (overlaps with C, not A or B)
]
CountGroups(circles) = 1 (A-B-C-D chain)
```

---

## Why This Algorithm Works

### Correctness

1. **Overlap Detection is Correct:**
   - Mathematical formula accurately determines overlap
   - Distance calculation is precise

2. **Graph Construction is Complete:**
   - Checks all pairs of circles
   - Builds symmetric adjacency list (undirected graph)

3. **DFS Finds All Components:**
   - DFS explores all nodes reachable from starting node
   - Each unvisited node starts a new component
   - Ensures all groups are found

### Why DFS?

**DFS is ideal for connected components:**
- Naturally explores all nodes in a component
- Simple recursive implementation
- Efficient: O(N + E) time

**Alternative: BFS**
- Would also work
- Uses queue instead of recursion
- Same time complexity

---

## Alternative Approaches

### 1. Union-Find (Disjoint Set)

**Idea**: Use Union-Find data structure

```python
def CountGroups_UnionFind(circles):
    uf = UnionFind(len(circles))
    
    for i, circle1 in enumerate(circles):
        for j in range(i+1, len(circles)):
            circle2 = circles[j]
            if IsOverlapped(circle1, circle2):
                uf.union(i, j)
    
    return uf.count_components()
```

**Pros:**
- More efficient for sparse graphs
- O(N² × α(N)) where α is inverse Ackermann

**Cons:**
- More complex to implement
- Overkill for this problem

### 2. BFS Instead of DFS

**Idea**: Use BFS with queue

```python
def BFS(start, adjacency_dict, visited):
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        for neighbor in adjacency_dict[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**Pros:** Iterative, no recursion stack
**Cons:** Slightly more code

---

## Real-World Applications

1. **Collision Detection:**
   - Game physics
   - Detect overlapping objects

2. **Clustering:**
   - Group similar objects
   - Data analysis

3. **Network Analysis:**
   - Find connected components
   - Social networks

4. **Image Processing:**
   - Group overlapping regions
   - Blob detection

5. **Geographic Information Systems:**
   - Find overlapping regions
   - Territory analysis

---

## Common Mistakes

### Mistake 1: Not Checking Both Directions

```python
# WRONG: Only adds one direction
if IsOverlapped(circle1, circle2):
    adjacency_dict[circle1].add(circle2)
    # Missing: adjacency_dict[circle2].add(circle1)
```

**Fix:** Add both directions (undirected graph)

### Mistake 2: Incorrect Overlap Formula

```python
# WRONG: Using < instead of <=
return distance < (r1 + r2)  # Misses tangent circles!
```

**Fix:** Use `<=` to include tangent circles

### Mistake 3: Not Resetting Visited Set

```python
# WRONG: Visited set persists
visited = set()  # Should be reset for each operation
```

**Fix:** Reset visited set in each method

---

## Summary

The Number of Circle Groups algorithm:
- Uses **graph representation**: circles as nodes, overlaps as edges
- Uses **DFS** to find connected components
- **Overlap detection**: distance ≤ sum of radii
- Time complexity: **O(N²)** where N = number of circles
- Space complexity: **O(N²)** for adjacency list

**Key Insight**: Overlapping circles form a graph, and groups are connected components. DFS naturally finds all nodes in each component.

---

## Related Problems

- **LeetCode 547**: Number of Provinces (similar connected components)
- **LeetCode 200**: Number of Islands (similar DFS traversal)
- **LeetCode 323**: Number of Connected Components (exact same problem)
- **Union-Find Problems**: Disjoint set union applications

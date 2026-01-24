# Is Graph Bipartite? (2-Coloring Problem)

> **LeetCode 785**: Given an undirected graph, return `true` if and only if it is bipartite. A graph is bipartite if we can split its set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

## Problem Description

Determine if a graph can be divided into two sets such that every edge connects a node from one set to a node in the other set.

**Bipartite Graph Definition:**
- Vertices can be partitioned into two disjoint sets (U and V)
- Every edge connects a vertex in U to a vertex in V
- No edge connects two vertices in the same set

**Equivalent Definition:**
- A graph is bipartite if and only if it can be **2-colored**
- Such that no two adjacent vertices have the same color
- If we find an edge between two vertices of the same color → NOT bipartite

---

## Key Insight

**2-Coloring Approach:**
- Use two colors (e.g., "red" and "green")
- Color adjacent nodes with different colors
- If we can successfully color the entire graph → bipartite
- If we find a conflict (adjacent nodes with same color) → NOT bipartite

**Why BFS Works:**
- BFS explores nodes level by level
- Nodes at even distance from start get one color
- Nodes at odd distance get the other color
- This ensures consistent coloring

---

## Algorithm Logic

```
1. Initialize color array (all None = unvisited)

2. For each unvisited node:
   a. Start BFS from this node
   b. Color starting node as "red"
   
3. BFS:
   While queue not empty:
     Pop node
     For each neighbor:
       If unvisited:
         Color with opposite color
         Add to queue
       If already colored with same color:
         Return False (conflict!)

4. If all nodes processed without conflict:
   Return True (bipartite)
```

---

## Detailed Example 1: Bipartite Graph

**Input**: `graph = [[1, 3], [0, 2], [1, 3], [0, 2]]`

### Graph Structure

```
Node 0: connected to 1, 3
Node 1: connected to 0, 2
Node 2: connected to 1, 3
Node 3: connected to 0, 2

Visual:
    0 ──── 1
    │      │
    │      │
    3 ──── 2

This is a 4-cycle, which is bipartite!
```

### Step-by-Step Execution

#### Step 1: Initialize

```
size = 4
colors = [None, None, None, None]
```

#### Step 2: Start BFS from Node 0

```
i = 0
colors[0] is None? YES → Process it

queue = deque([0])
colors[0] = "red"
```

#### Step 3: BFS Iteration 1

```
Pop: node = 0
current_color = "red"
next_color = "green"

Neighbors of 0: [1, 3]

Process neighbor 1:
  colors[1] is None? YES
    colors[1] = "green"
    queue.append(1)  → queue = [1]

Process neighbor 3:
  colors[3] is None? YES
    colors[3] = "green"
    queue.append(3)  → queue = [1, 3]
```

**After Iteration 1:**
```
colors = ["red", "green", None, "green"]
queue = [1, 3]
```

#### Step 4: BFS Iteration 2

```
Pop: node = 1
current_color = "green"
next_color = "red"

Neighbors of 1: [0, 2]

Process neighbor 0:
  colors[0] is None? NO
  colors[0] == current_color ("green")? NO (it's "red") → OK, continue

Process neighbor 2:
  colors[2] is None? YES
    colors[2] = "red"
    queue.append(2)  → queue = [3, 2]
```

**After Iteration 2:**
```
colors = ["red", "green", "red", "green"]
queue = [3, 2]
```

#### Step 5: BFS Iteration 3

```
Pop: node = 3
current_color = "green"
next_color = "red"

Neighbors of 3: [0, 2]

Process neighbor 0:
  colors[0] is None? NO
  colors[0] == current_color ("green")? NO (it's "red") → OK

Process neighbor 2:
  colors[2] is None? NO
  colors[2] == current_color ("green")? NO (it's "red") → OK
```

**After Iteration 3:**
```
colors = ["red", "green", "red", "green"]
queue = [2]
```

#### Step 6: BFS Iteration 4

```
Pop: node = 2
current_color = "red"
next_color = "green"

Neighbors of 2: [1, 3]

Process neighbor 1:
  colors[1] is None? NO
  colors[1] == current_color ("red")? NO (it's "green") → OK

Process neighbor 3:
  colors[3] is None? NO
  colors[3] == current_color ("red")? NO (it's "green") → OK
```

**After Iteration 4:**
```
colors = ["red", "green", "red", "green"]
queue = []  (empty)
```

#### Step 7: Check Remaining Nodes

```
i = 1: colors[1] is not None → Skip
i = 2: colors[2] is not None → Skip
i = 3: colors[3] is not None → Skip
```

#### Result

```
All nodes processed without conflicts
Return True ✅

Final coloring:
  Set A (red): {0, 2}
  Set B (green): {1, 3}
  All edges connect red to green → Bipartite!
```

---

## Detailed Example 2: Non-Bipartite Graph

**Input**: `graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]`

### Graph Structure

```
Node 0: connected to 1, 2, 3
Node 1: connected to 0, 2
Node 2: connected to 0, 1, 3
Node 3: connected to 0, 2

Visual:
    0 ──── 1
    │\    /│
    │ \  / │
    │  \/  │
    │  /\  │
    │ /  \ │
    3 ──── 2

This contains a triangle (0-1-2), which makes it non-bipartite!
```

### Step-by-Step Execution

#### Step 1: Initialize

```
size = 4
colors = [None, None, None, None]
```

#### Step 2: Start BFS from Node 0

```
i = 0
colors[0] is None? YES → Process it

queue = deque([0])
colors[0] = "red"
```

#### Step 3: BFS Iteration 1

```
Pop: node = 0
current_color = "red"
next_color = "green"

Neighbors of 0: [1, 2, 3]

Process neighbor 1:
  colors[1] is None? YES
    colors[1] = "green"
    queue.append(1)  → queue = [1]

Process neighbor 2:
  colors[2] is None? YES
    colors[2] = "green"
    queue.append(2)  → queue = [1, 2]

Process neighbor 3:
  colors[3] is None? YES
    colors[3] = "green"
    queue.append(3)  → queue = [1, 2, 3]
```

**After Iteration 1:**
```
colors = ["red", "green", "green", "green"]
queue = [1, 2, 3]
```

#### Step 4: BFS Iteration 2

```
Pop: node = 1
current_color = "green"
next_color = "red"

Neighbors of 1: [0, 2]

Process neighbor 0:
  colors[0] is None? NO
  colors[0] == current_color ("green")? NO (it's "red") → OK

Process neighbor 2:
  colors[2] is None? NO
  colors[2] == current_color ("green")? YES ❌
    CONFLICT! Node 1 and Node 2 are both "green" and connected!
    Return False
```

**Result**: Return **False** ❌

**Why it failed:**
- Node 0 is "red"
- Nodes 1, 2, 3 are all "green" (neighbors of 0)
- But nodes 1 and 2 are connected to each other
- Two "green" nodes are adjacent → NOT bipartite!

---

## Example 3: Disconnected Components

**Input**: `graph = [[1], [0, 3], [3], [1, 2]]`

### Graph Structure

```
Component 1: 0 ──── 1 ──── 3 ──── 2
Component 2: (none, all nodes are in component 1)

Actually, this is one connected component:
  0 ──── 1 ──── 3 ──── 2
```

### Step-by-Step Execution

#### Step 1: Initialize

```
size = 4
colors = [None, None, None, None]
```

#### Step 2: Start BFS from Node 0

```
i = 0
colors[0] is None? YES → Process it

queue = deque([0])
colors[0] = "red"
```

#### Step 3: BFS Processing

**Iteration 1: Process Node 0**
```
Pop: node = 0
Neighbors: [1]
  colors[1] = "green"
  queue = [1]
```

**Iteration 2: Process Node 1**
```
Pop: node = 1
Neighbors: [0, 3]
  colors[0] already "red" (OK)
  colors[3] = "red"
  queue = [3]
```

**Iteration 3: Process Node 3**
```
Pop: node = 3
Neighbors: [1, 2]
  colors[1] already "green" (OK)
  colors[2] = "green"
  queue = [2]
```

**Iteration 4: Process Node 2**
```
Pop: node = 2
Neighbors: [3]
  colors[3] already "red" (OK)
  queue = []
```

#### Result

```
All nodes processed without conflicts
Return True ✅

Final coloring:
  Set A (red): {0, 3}
  Set B (green): {1, 2}
```

---

## Example 4: Multiple Disconnected Components

**Input**: `graph = [[1], [0], [3], [2]]`

### Graph Structure

```
Component 1: 0 ──── 1
Component 2: 2 ──── 3

Two separate components!
```

### Step-by-Step Execution

#### Component 1: Nodes 0-1

**Start from Node 0:**
```
i = 0
colors[0] is None? YES → Process it

queue = [0]
colors[0] = "red"

BFS:
  Process 0 → color 1 as "green"
  Process 1 → check 0 (OK)
  
colors = ["red", "green", None, None]
```

#### Component 2: Nodes 2-3

**Continue loop:**
```
i = 1: colors[1] is not None → Skip
i = 2: colors[2] is None? YES → Process it

queue = [2]
colors[2] = "red"

BFS:
  Process 2 → color 3 as "green"
  Process 3 → check 2 (OK)
  
colors = ["red", "green", "red", "green"]
```

#### Result

```
All nodes processed without conflicts
Return True ✅

Each component is bipartite, so the whole graph is bipartite!
```

---

## Key Concepts

### 1. What is a Bipartite Graph?

**Definition**: A graph whose vertices can be divided into two disjoint sets such that:
- Every edge connects a vertex from one set to a vertex in the other
- No edge connects two vertices in the same set

**Visual Example:**
```
Bipartite:
  Set A: {0, 2}
  Set B: {1, 3}
  
  0 ──── 1
  │      │
  │      │
  2 ──── 3
  
All edges go from A to B ✅
```

**Non-Bipartite:**
```
Triangle (odd cycle):
  0 ──── 1
   \    /
    \  /
     \/
     2

Cannot divide into two sets!
If 0 and 1 are in different sets, where does 2 go?
```

### 2. Why 2-Coloring Works

**Theorem**: A graph is bipartite if and only if it can be 2-colored.

**Proof Intuition:**
- If bipartite → can color set A with one color, set B with another
- If 2-colorable → the two color classes form the two sets
- If NOT 2-colorable → must have an odd cycle → NOT bipartite

**Key Insight**: Odd-length cycles cannot be 2-colored!

### 3. Why BFS Works

**BFS Property**: Explores nodes level by level

**Coloring Strategy:**
- Level 0 (start): Color "red"
- Level 1 (neighbors of start): Color "green"
- Level 2 (neighbors of level 1): Color "red"
- Level 3 (neighbors of level 2): Color "green"
- ...

**Why this works:**
- Nodes at even distance from start → same color
- Nodes at odd distance from start → same color
- If two nodes at same level are connected → conflict!

### 4. Conflict Detection

**When does a conflict occur?**
- Two adjacent nodes have the same color
- This means we found an edge within the same set
- Therefore, the graph is NOT bipartite

**Example:**
```
Node 0: "red"
Node 1: "green" (neighbor of 0)
Node 2: "green" (neighbor of 0)
Edge between 1 and 2: Both "green" → Conflict! ❌
```

### 5. Handling Disconnected Components

**Why check all nodes?**
- Graph may have multiple connected components
- Each component must be bipartite
- If any component is not bipartite → whole graph is not

**Algorithm handles this:**
- Loop through all nodes
- Skip already-visited nodes (from previous BFS)
- Start new BFS for each unvisited node
- Ensures all components are checked

### 6. Why Not DFS?

**DFS would also work**, but BFS is more intuitive:
- BFS naturally explores level by level
- Makes the coloring pattern clearer
- Both have O(V + E) complexity

**DFS approach:**
```python
def dfs(node, color):
    colors[node] = color
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
        if colors[neighbor] is None:
            if not dfs(neighbor, opposite_color):
                return False
    return True
```

---

## Visual Timeline

### Example: Bipartite Graph `[[1, 3], [0, 2], [1, 3], [0, 2]]`

```
Step | Queue    | Colors              | Action
-----|----------|---------------------|------------------
0    | [0]      | [R, _, _, _]        | Start BFS from 0
1    | [1, 3]   | [R, G, _, G]        | Process 0 → color 1,3 green
2    | [3, 2]   | [R, G, R, G]        | Process 1 → color 2 red
3    | [2]      | [R, G, R, G]        | Process 3 → check neighbors
4    | []       | [R, G, R, G]        | Process 2 → check neighbors
5    | -        | [R, G, R, G]        | All processed → Return True ✅
```

### Example: Non-Bipartite Graph `[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]`

```
Step | Queue    | Colors              | Action
-----|----------|---------------------|------------------
0    | [0]      | [R, _, _, _]        | Start BFS from 0
1    | [1,2,3]  | [R, G, G, G]        | Process 0 → color 1,2,3 green
2    | [2,3]    | [R, G, G, G]        | Process 1 → check 0 (OK)
3    | [2,3]    | [R, G, G, G]        | Process 1 → check 2: CONFLICT! ❌
     |          |                     | Return False
```

---

## Algorithm Pseudocode

```python
def isBipartite(graph):
    size = len(graph)
    colors = [None] * size  # None = unvisited
    
    for i in range(size):
        if colors[i] is not None:
            continue  # Already visited
        
        # Start BFS from unvisited node
        queue = deque([i])
        colors[i] = "red"
        
        while queue:
            node = queue.popleft()
            current_color = colors[node]
            next_color = "green" if current_color == "red" else "red"
            
            for neighbor in graph[node]:
                if colors[neighbor] is None:
                    # Unvisited: color with opposite color
                    colors[neighbor] = next_color
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:
                    # Conflict: same color adjacent nodes
                    return False
    
    return True  # No conflicts found
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(V + E) | Visit each vertex once, check each edge once |
| **Space** | O(V) | Color array O(V), BFS queue O(V) in worst case |

**Where:**
- V = number of vertices (nodes)
- E = number of edges

**Why O(V + E)?**
- Each node is visited once: O(V)
- Each edge is checked once: O(E)
- Total: O(V + E)

---

## Edge Cases

### Case 1: Single Node
```
graph = [[]]
Result: True (trivially bipartite, no edges)
```

### Case 2: Empty Graph
```
graph = []
Result: True (no edges, so bipartite)
```

### Case 3: Two Nodes, One Edge
```
graph = [[1], [0]]
Result: True (can be divided into two sets)
```

### Case 4: Triangle (Odd Cycle)
```
graph = [[1, 2], [0, 2], [0, 1]]
Result: False (odd cycle cannot be 2-colored)
```

### Case 5: Isolated Nodes
```
graph = [[], [], []]
Result: True (no edges, each node is its own component)
```

### Case 6: Complete Bipartite Graph
```
graph = [[1, 2], [0], [0]]
Result: True (star graph is bipartite)
```

---

## Why This Algorithm Works

### Correctness Proof

**1. If graph is bipartite:**
- Algorithm will find a valid 2-coloring
- No conflicts will be detected
- Returns True ✅

**2. If graph is NOT bipartite:**
- Must contain an odd cycle
- When BFS processes the odd cycle, it will:
  - Try to color nodes alternately
  - But odd cycle forces two adjacent nodes to have same color
  - Conflict detected → Returns False ✅

**3. Handles disconnected components:**
- Each component is checked independently
- If all components are bipartite → graph is bipartite
- If any component is not → graph is not

### Why BFS Guarantees Correctness

**BFS explores in levels:**
- Level 0: Start node (color "red")
- Level 1: Neighbors (color "green")
- Level 2: Neighbors of level 1 (color "red")
- ...

**If graph is bipartite:**
- All nodes at same level have same color
- No edges between nodes at same level
- No conflicts

**If graph is NOT bipartite:**
- Must have edge between nodes at same level
- These nodes have same color
- Conflict detected

---

## Alternative Approaches

### 1. DFS Approach

```python
def isBipartite_DFS(graph):
    colors = [None] * len(graph)
    
    def dfs(node, color):
        colors[node] = color
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                return False
            if colors[neighbor] is None:
                if not dfs(neighbor, "green" if color == "red" else "red"):
                    return False
        return True
    
    for i in range(len(graph)):
        if colors[i] is None:
            if not dfs(i, "red"):
                return False
    return True
```

**Time**: O(V + E), **Space**: O(V) for recursion stack

### 2. Union-Find Approach

**Idea**: Use Union-Find to detect if graph can be partitioned

**Complexity**: O(V + E × α(V)) where α is inverse Ackermann function

**Less intuitive** for this problem

---

## Real-World Applications

1. **Scheduling Problems**: Assign tasks to two groups with constraints
2. **Resource Allocation**: Divide resources into two sets
3. **Network Design**: Partition network nodes into two groups
4. **Matching Problems**: Bipartite matching (e.g., job assignment)
5. **Graph Theory**: Foundation for many graph algorithms

---

## Common Mistakes

### Mistake 1: Not Handling Disconnected Components
```python
# WRONG: Only checks first component
queue = deque([0])
colors[0] = "red"
# ... BFS ...
return True  # Misses other components!
```

**Fix**: Loop through all nodes, start BFS for each unvisited node

### Mistake 2: Checking Wrong Condition
```python
# WRONG: Check if neighbor is different color
if colors[neighbor] != next_color:
    return False
```

**Fix**: Check if neighbor has same color as current node
```python
if colors[neighbor] == current_color:
    return False
```

### Mistake 3: Not Coloring Starting Node
```python
# WRONG: Forgot to color starting node
queue = deque([0])
# colors[0] = "red"  # Missing!
```

**Fix**: Always color the starting node before BFS

---

## Summary

The bipartite graph detection algorithm:
- Uses **BFS with 2-coloring** to check if graph is bipartite
- Colors nodes alternately (red/green) as we traverse
- Detects conflicts when adjacent nodes have same color
- Handles disconnected components by checking all nodes
- Time complexity: **O(V + E)**
- Space complexity: **O(V)**

**Key Insight**: A graph is bipartite if and only if it can be 2-colored without conflicts. BFS naturally ensures proper coloring by exploring level by level.

---

## Related Problems

- **LeetCode 785**: Is Graph Bipartite? (this problem)
- **LeetCode 886**: Possible Bipartition (similar, with constraints)
- **LeetCode 785**: Check if graph can be divided into two sets
- **Graph Coloring**: General k-coloring problem (NP-complete for k > 2)

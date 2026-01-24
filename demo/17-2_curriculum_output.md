# Course Schedule (Topological Sort)

> **LeetCode 207**: There are a total of `numCourses` courses you have to take. Some courses may have prerequisites. For example, to take course 0 you have to first take course 1, which is expressed as a pair: `[0, 1]`. Given the total number of courses and an array of prerequisite pairs, return `true` if you can finish all courses.

## Problem Description

Determine if it's possible to finish all courses given their prerequisites.

**Prerequisites**: `[course, prerequisite]` means course depends on prerequisite.

**Example:**
- `numCourses = 2`, `prerequisites = [[1, 0]]`
- Meaning: Course 1 requires Course 0
- Can finish? Yes: Take Course 0 first, then Course 1

**Key Question**: Is there a cycle in the dependency graph? If yes, cannot finish all courses.

---

## Key Insight

Use **Topological Sort (Kahn's Algorithm)**:
- Build a directed graph from prerequisites
- Track in-degree (number of prerequisites) for each course
- Start with courses having in-degree 0 (no prerequisites)
- Process courses, reducing in-degrees of dependent courses
- If all courses processed → no cycle → can finish
- If some courses remain → cycle exists → cannot finish

**Strategy**: Use BFS to process courses level by level, starting from courses with no prerequisites.

---

## Algorithm Logic

```
1. Build graph and in-degree array:
   - adj[prereq] = list of courses that depend on prereq
   - indegree[course] = number of prerequisites for course

2. Initialize queue with courses having in-degree 0

3. BFS:
   While queue not empty:
     Pop course
     For each course that depends on it:
       Decrease its in-degree
       If in-degree becomes 0, add to queue
     Count processed courses

4. Return: count == numCourses
```

---

## Detailed Example: Step-by-Step

**Input**: `numCourses = 4`, `prerequisites = [[1, 0], [2, 1], [3, 2]]`

### Graph Representation

```
Prerequisites:
  [1, 0] → Course 1 depends on Course 0
  [2, 1] → Course 2 depends on Course 1
  [3, 2] → Course 3 depends on Course 2

Graph:
  0 → 1 → 2 → 3

This is a chain: 0 → 1 → 2 → 3
No cycles → Can finish all courses!
```

### Step 1: Initialize Data Structures

```
numCourses = 4

Initialize adjacency list:
  adj = [[], [], [], []]  (4 empty lists for courses 0, 1, 2, 3)

Initialize in-degree array:
  indegree = [0, 0, 0, 0]  (all courses start with 0 prerequisites)
```

### Step 2: Build Graph and In-Degree Array

**Process prerequisite [1, 0]:**
```
course = 1, prereq = 0

Add edge: adj[0].append(1)
  adj[0] = [1]
  adj = [[1], [], [], []]

Increase in-degree: indegree[1] += 1
  indegree = [0, 1, 0, 0]
  
Meaning: Course 1 now has 1 prerequisite (Course 0)
```

**Process prerequisite [2, 1]:**
```
course = 2, prereq = 1

Add edge: adj[1].append(2)
  adj[1] = [2]
  adj = [[1], [2], [], []]

Increase in-degree: indegree[2] += 1
  indegree = [0, 1, 1, 0]
  
Meaning: Course 2 now has 1 prerequisite (Course 1)
```

**Process prerequisite [3, 2]:**
```
course = 3, prereq = 2

Add edge: adj[2].append(3)
  adj[2] = [3]
  adj = [[1], [2], [3], []]

Increase in-degree: indegree[3] += 1
  indegree = [0, 1, 1, 1]
  
Meaning: Course 3 now has 1 prerequisite (Course 2)
```

**After Step 2:**
```
adj = [[1], [2], [3], []]
      ↑    ↑    ↑    ↑
      0    1    2    3

indegree = [0, 1, 1, 1]
           ↑  ↑  ↑  ↑
           0  1  2  3

Graph structure:
  0 → 1 → 2 → 3
```

### Step 3: Initialize Queue

```
Find courses with in-degree 0:
  Course 0: indegree[0] = 0 → Add to queue ✅
  Course 1: indegree[1] = 1 → Skip
  Course 2: indegree[2] = 1 → Skip
  Course 3: indegree[3] = 1 → Skip

queue = deque([0])
count = 1  (Course 0 can be taken)
```

### Step 4: BFS Processing

#### Iteration 1: Process Course 0

```
Pop: course = 0 from queue
Current count: 1

Process dependents of Course 0:
  adj[0] = [1]  (Course 1 depends on Course 0)
  
  For next_course = 1:
    Decrease in-degree: indegree[1] -= 1
      indegree[1] = 1 - 1 = 0
    
    Check: indegree[1] == 0? YES ✅
      Add Course 1 to queue: queue.append(1)
      count += 1 → count = 2
```

**After Iteration 1:**
```
queue = deque([1])
count = 2
indegree = [0, 0, 1, 1]
           ↑  ↑  ↑  ↑
           0  1  2  3
```

#### Iteration 2: Process Course 1

```
Pop: course = 1 from queue
Current count: 2

Process dependents of Course 1:
  adj[1] = [2]  (Course 2 depends on Course 1)
  
  For next_course = 2:
    Decrease in-degree: indegree[2] -= 1
      indegree[2] = 1 - 1 = 0
    
    Check: indegree[2] == 0? YES ✅
      Add Course 2 to queue: queue.append(2)
      count += 1 → count = 3
```

**After Iteration 2:**
```
queue = deque([2])
count = 3
indegree = [0, 0, 0, 1]
           ↑  ↑  ↑  ↑
           0  1  2  3
```

#### Iteration 3: Process Course 2

```
Pop: course = 2 from queue
Current count: 3

Process dependents of Course 2:
  adj[2] = [3]  (Course 3 depends on Course 2)
  
  For next_course = 3:
    Decrease in-degree: indegree[3] -= 1
      indegree[3] = 1 - 1 = 0
    
    Check: indegree[3] == 0? YES ✅
      Add Course 3 to queue: queue.append(3)
      count += 1 → count = 4
```

**After Iteration 3:**
```
queue = deque([3])
count = 4
indegree = [0, 0, 0, 0]
           ↑  ↑  ↑  ↑
           0  1  2  3
```

#### Iteration 4: Process Course 3

```
Pop: course = 3 from queue
Current count: 4

Process dependents of Course 3:
  adj[3] = []  (No courses depend on Course 3)
  
  No dependents to process
```

**After Iteration 4:**
```
queue = deque([])  (empty)
count = 4
indegree = [0, 0, 0, 0]
```

### Step 5: Check Result

```
count = 4
numCourses = 4
count == numCourses? YES ✅

Result: True (can finish all courses)
```

**Valid course order**: 0 → 1 → 2 → 3

---

## Example 2: Circular Dependency

**Input**: `numCourses = 2`, `prerequisites = [[1, 0], [0, 1]]`

### Step 1: Build Graph

```
Process [1, 0]:
  adj[0].append(1)
  indegree[1] += 1
  adj = [[1], []]
  indegree = [0, 1]

Process [0, 1]:
  adj[1].append(0)
  indegree[0] += 1
  adj = [[1], [0]]
  indegree = [1, 1]

Graph:
  0 ⇄ 1  (circular dependency!)
```

### Step 2: Initialize Queue

```
Find courses with in-degree 0:
  Course 0: indegree[0] = 1 → Skip
  Course 1: indegree[1] = 1 → Skip

queue = deque([])  (empty!)
count = 0
```

### Step 3: BFS Processing

```
Queue is empty → While loop never executes
count = 0
```

### Step 4: Check Result

```
count = 0
numCourses = 2
count == numCourses? NO ❌

Result: False (cannot finish all courses - cycle exists!)
```

**Why?** Both courses require each other, creating a cycle. No course can be taken first.

---

## Example 3: Complex Graph

**Input**: `numCourses = 6`, `prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3]]`

### Graph Structure

```
    0
   / \
  1   2
  |   |
  3   4
  |
  5

Graph: 0 → 1 → 3 → 5
       0 → 2 → 4
```

### Step-by-Step Execution

**Step 1: Build Graph**
```
adj = [[1, 2], [3], [4], [5], [], []]
indegree = [0, 1, 1, 1, 1, 1]
```

**Step 2: Initialize Queue**
```
Courses with in-degree 0: Course 0
queue = [0]
count = 1
```

**Step 3: BFS**

**Iteration 1: Process 0**
```
Pop: 0
Process: 1, 2
  indegree[1] = 0 → Add 1
  indegree[2] = 0 → Add 2
count = 3
queue = [1, 2]
```

**Iteration 2: Process 1**
```
Pop: 1
Process: 3
  indegree[3] = 0 → Add 3
count = 4
queue = [2, 3]
```

**Iteration 3: Process 2**
```
Pop: 2
Process: 4
  indegree[4] = 0 → Add 4
count = 5
queue = [3, 4]
```

**Iteration 4: Process 3**
```
Pop: 3
Process: 5
  indegree[5] = 0 → Add 5
count = 6
queue = [4, 5]
```

**Iteration 5: Process 4**
```
Pop: 4
No dependents
count = 6
queue = [5]
```

**Iteration 6: Process 5**
```
Pop: 5
No dependents
count = 6
queue = []
```

**Result**: `count = 6 == numCourses` → **True** ✅

---

## Key Concepts

### 1. Topological Sort

**Topological Sort**: An ordering of nodes in a directed graph such that for every edge (u→v), u comes before v.

**In course scheduling**: If Course A is a prerequisite for Course B, then A must come before B in the ordering.

### 2. In-Degree

**In-degree** of a node = number of incoming edges (number of prerequisites)

- `indegree[course] = 0` → Course has no prerequisites → Can be taken immediately
- `indegree[course] > 0` → Course has prerequisites → Must wait

### 3. Kahn's Algorithm

**Kahn's Algorithm** (BFS-based topological sort):
1. Find all nodes with in-degree 0
2. Add them to queue
3. Process each node:
   - Remove it (decrease in-degrees of neighbors)
   - If neighbor's in-degree becomes 0, add to queue
4. If all nodes processed → valid topological order exists
5. If some nodes remain → cycle exists

### 4. Cycle Detection

**How to detect cycles?**
- If graph has a cycle, some nodes will always have in-degree > 0
- These nodes can never be added to the queue
- `count < numCourses` indicates a cycle

**Example**: `0 ⇄ 1`
- Both have in-degree 1
- Neither can be processed first
- Cycle detected!

### 5. Why BFS Works

BFS processes courses level by level:
- Level 0: Courses with no prerequisites
- Level 1: Courses whose prerequisites are all in Level 0
- Level 2: Courses whose prerequisites are all in Levels 0-1
- And so on...

This ensures prerequisites are always taken before dependent courses.

---

## Visual Graph Representation

### Example 1: Valid (No Cycle)
```
Prerequisites: [[1,0], [2,1], [3,2]]

Graph:
  0 → 1 → 2 → 3

Topological order: 0, 1, 2, 3 ✅
```

### Example 2: Invalid (Cycle)
```
Prerequisites: [[1,0], [0,1]]

Graph:
  0 ⇄ 1

No valid topological order ❌
```

### Example 3: Complex Valid Graph
```
Prerequisites: [[1,0], [2,0], [3,1], [4,2], [5,3]]

Graph:
      0
     / \
    1   2
    |   |
    3   4
    |
    5

Topological orders:
  0 → 1 → 3 → 5, 0 → 2 → 4
  Or: 0 → 2 → 4, 0 → 1 → 3 → 5
  Or: 0 → 1 → 2 → 3 → 4 → 5
  (Multiple valid orders exist)
```

---

## Algorithm Pseudocode

```python
def canFinish(numCourses, prerequisites):
    # Build graph
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    
    for course, prereq in prerequisites:
        adj[prereq].append(course)
        indegree[course] += 1
    
    # Initialize queue with courses having no prerequisites
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = len(queue)
    
    # BFS
    while queue:
        current = queue.popleft()
        
        for next_course in adj[current]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
                count += 1
    
    # Check if all courses can be taken
    return count == numCourses
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(V + E) | V = numCourses, E = number of prerequisites. Build graph O(E), BFS O(V+E) |
| **Space** | O(V + E) | Adjacency list O(E), in-degree array O(V), queue O(V) |

---

## Edge Cases

### Case 1: No Prerequisites
```
numCourses = 5, prerequisites = []
Result: True (all courses independent, can take in any order)
```

### Case 2: Single Course
```
numCourses = 1, prerequisites = []
Result: True (one course, no prerequisites)
```

### Case 3: Zero Courses
```
numCourses = 0, prerequisites = []
Result: True (trivially true)
```

### Case 4: Self-Loop
```
numCourses = 1, prerequisites = [[0, 0]]
Result: False (course depends on itself - cycle!)
```

### Case 5: Disconnected Components
```
numCourses = 4, prerequisites = [[1, 0]]
Result: True
Graph: 0 → 1, and courses 2, 3 are independent
```

---

## Why This Algorithm Works

### Correctness

1. **Topological Sort**: Kahn's algorithm finds a valid topological ordering if one exists
2. **Cycle Detection**: If a cycle exists, some nodes remain with in-degree > 0
3. **Completeness**: If `count == numCourses`, all courses were processed → no cycle

### Why BFS?

BFS processes courses in "levels":
- First level: Courses with no prerequisites
- Second level: Courses whose prerequisites are all in first level
- This ensures prerequisites are always satisfied

### Why Decrease In-Degree?

When we process a course:
- We've "taken" that course
- All courses that depend on it have one less prerequisite
- Decrease in-degree reflects this

---

## Alternative Approach: DFS with Cycle Detection

```python
def canFinish_DFS(numCourses, prerequisites):
    adj = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        adj[prereq].append(course)
    
    # 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * numCourses
    
    def hasCycle(course):
        if state[course] == 1:  # Cycle detected
            return True
        if state[course] == 2:  # Already processed
            return False
        
        state[course] = 1  # Mark as visiting
        for next_course in adj[course]:
            if hasCycle(next_course):
                return True
        state[course] = 2  # Mark as visited
        return False
    
    for i in range(numCourses):
        if hasCycle(i):
            return False
    return True
```

**Time**: O(V + E), **Space**: O(V) for recursion stack

---

## Summary

The course schedule algorithm:
- Uses **Kahn's Algorithm** (BFS-based topological sort)
- Builds directed graph from prerequisites
- Tracks in-degrees for each course
- Processes courses with in-degree 0 first
- Detects cycles by checking if all courses are processed
- Time complexity: **O(V + E)**
- Space complexity: **O(V + E)**

**Key Insight**: A valid course schedule exists if and only if the dependency graph has no cycles. Kahn's algorithm efficiently detects cycles by attempting to find a topological ordering.

---

## Related Problems

- **LeetCode 207**: Course Schedule (this problem)
- **LeetCode 210**: Course Schedule II (return the ordering)
- **LeetCode 269**: Alien Dictionary (topological sort)
- **LeetCode 802**: Find Eventual Safe States

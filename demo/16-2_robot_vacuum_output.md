# Robot Room Cleaner

> **LeetCode 489**: Given a robot cleaner in a room modeled as a grid. Each cell in the grid can be empty or blocked. The robot can move forward, turn left or turn right. When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell. Design an algorithm to clean the entire room.

## Problem Description

Control a robot to clean all reachable cells in an unknown room layout.

**Robot API:**
- `robot.move()`: Returns True if robot moves forward, False if blocked
- `robot.turnLeft()`: Robot turns left (90 degrees)
- `robot.turnRight()`: Robot turns right (90 degrees)
- `robot.clean()`: Clean current cell

**Constraints:**
- Room layout is unknown
- Robot starts at unknown position
- Need to clean all reachable cells
- Cannot revisit cells unnecessarily

---

## Key Insight

Use **DFS (Depth-First Search) with Backtracking**:
- Track visited positions using a set
- Try all 4 directions from each cell
- Use relative coordinates (start at (0,0))
- After exploring a direction, backtrack to return to previous cell
- Rotate robot to try all directions systematically

**Strategy**: Explore like a maze, always returning to previous position after exploring a branch.

---

## Algorithm Logic

```
1. Initialize:
   - directions = [(0,1), (1,0), (0,-1), (-1,0)]  (Right, Down, Left, Up)
   - lookup = set()  (visited positions)
   - Start at (0, 0) facing direction 0 (Up)

2. DFS(pos, robot, d, lookup):
   Base case: if pos in lookup:
     return  (already cleaned)
   
   Mark pos as cleaned:
     lookup.add(pos)
     robot.clean()
   
   Try all 4 directions:
     For each direction:
       Calculate new position
       If robot.move() succeeds:
         DFS(new_pos, robot, d, lookup)
         goBack(robot)  (return to current cell)
       robot.turnRight()  (try next direction)
       d = (d + 1) % 4

3. goBack(robot):
   Turn around (turnLeft twice)
   Move back
   Turn around again (restore original facing)
```

---

## Direction System

**Directions Array:**
```python
directions = [
  (0, 1),   # Index 0: Right  (dx=0, dy=1)
  (1, 0),   # Index 1: Down   (dx=1, dy=0)
  (0, -1),  # Index 2: Left   (dx=0, dy=-1)
  (-1, 0)   # Index 3: Up      (dx=-1, dy=0)
]
```

**Direction Index:**
- `d = 0`: Facing Right
- `d = 1`: Facing Down
- `d = 2`: Facing Left
- `d = 3`: Facing Up

**Rotation:**
- `turnRight()`: `d = (d + 1) % 4` (cycle: 0→1→2→3→0)
- `turnLeft()`: `d = (d - 1) % 4` (cycle: 0→3→2→1→0)

---

## Detailed Example: Step-by-Step

**Room Layout (unknown to robot):**
```
     -1  0  1  2
  -1  #  #  #  #
   0  #  .  .  #
   1  #  .  .  #
   2  #  #  #  #
   
   # = blocked
   . = empty (cleanable)
   
   Robot starts at (0, 0) facing Up (d=0)
```

### Initial Setup

```
pos = (0, 0)
d = 0  (facing Up, which is direction index 3, but we start with d=0)
lookup = set()
```

**Note**: The algorithm uses relative coordinates. The robot's starting position is considered (0, 0).

### Step 1: DFS((0, 0), robot, 0, lookup)

```
Current position: (0, 0)
Current direction: d = 0 (Right, but robot might be facing different direction initially)

Check: (0, 0) in lookup? NO
  Add (0, 0) to lookup: {(0, 0)}
  robot.clean()  → Clean cell (0, 0)

Try 4 directions (loop 4 times):
```

#### Iteration 1: Try direction d=0 (Right)

```
d = 0
directions[0] = (0, 1)  (Right)
new_pos = (0 + 0, 0 + 1) = (0, 1)

Try to move:
  robot.move() → Check if can move right
  If room has cell (0,1) and it's not blocked:
    Move succeeds → robot.move() returns True
    
    Recursive call: DFS((0, 1), robot, 0, lookup)
      (We'll explore this later)
    
    After DFS returns, need to go back:
      goBack(robot)
        robot.turnLeft()   → Turn left
        robot.turnLeft()   → Turn left (now facing opposite)
        robot.move()       → Move back to (0, 0)
        robot.turnRight()  → Turn right
        robot.turnRight()  → Turn right (restore original facing)
  
  If blocked:
    robot.move() returns False
    Don't recurse, continue to next direction

Rotate for next direction:
  robot.turnRight()  → Now facing next direction
  d = (0 + 1) % 4 = 1  (Down)
```

#### Iteration 2: Try direction d=1 (Down)

```
d = 1
directions[1] = (1, 0)  (Down)
new_pos = (0 + 1, 0 + 0) = (1, 0)

Try to move:
  robot.move() → Check if can move down
  If succeeds:
    DFS((1, 0), robot, 1, lookup)
    goBack(robot)
  
  Rotate:
    robot.turnRight()
    d = (1 + 1) % 4 = 2  (Left)
```

#### Iteration 3: Try direction d=2 (Left)

```
d = 2
directions[2] = (0, -1)  (Left)
new_pos = (0 + 0, 0 + (-1)) = (0, -1)

Try to move:
  robot.move() → Check if can move left
  If succeeds:
    DFS((0, -1), robot, 2, lookup)
    goBack(robot)
  
  Rotate:
    robot.turnRight()
    d = (2 + 1) % 4 = 3  (Up)
```

#### Iteration 4: Try direction d=3 (Up)

```
d = 3
directions[3] = (-1, 0)  (Up)
new_pos = (0 + (-1), 0 + 0) = (-1, 0)

Try to move:
  robot.move() → Check if can move up
  If succeeds:
    DFS((-1, 0), robot, 3, lookup)
    goBack(robot)
  
  Rotate:
    robot.turnRight()
    d = (3 + 1) % 4 = 0  (Right, back to start)
```

**After Step 1:**
```
lookup = {(0, 0)}  (cleaned)
Robot back at (0, 0) facing original direction
```

### Step 2: DFS((0, 1), robot, 0, lookup) - Recursive Call

**Context**: This is called from Step 1, Iteration 1, when moving right from (0,0)

```
Current position: (0, 1)
Current direction: d = 0 (Right)
Robot just moved right from (0, 0)

Check: (0, 1) in lookup? NO
  Add (0, 1) to lookup: {(0, 0), (0, 1)}
  robot.clean()  → Clean cell (0, 1)

Try 4 directions:
```

#### Iteration 1: Try direction d=0 (Right)

```
d = 0
new_pos = (0, 1 + 1) = (0, 2)

Try to move:
  robot.move() → Move right
  If succeeds:
    DFS((0, 2), robot, 0, lookup)
    goBack(robot)
  
  Rotate: d = 1 (Down)
```

#### Iteration 2: Try direction d=1 (Down)

```
d = 1
new_pos = (0 + 1, 1) = (1, 1)

Try to move:
  robot.move() → Move down
  If succeeds:
    DFS((1, 1), robot, 1, lookup)
    goBack(robot)
  
  Rotate: d = 2 (Left)
```

#### Iteration 3: Try direction d=2 (Left)

```
d = 2
new_pos = (0, 1 - 1) = (0, 0)

Try to move:
  robot.move() → Move left
  If succeeds:
    Check: (0, 0) in lookup? YES
      → Return immediately (already cleaned)
    goBack(robot)
  
  Rotate: d = 3 (Up)
```

#### Iteration 4: Try direction d=3 (Up)

```
d = 3
new_pos = (0 - 1, 1) = (-1, 1)

Try to move:
  robot.move() → Move up
  If succeeds:
    DFS((-1, 1), robot, 3, lookup)
    goBack(robot)
  
  Rotate: d = 0 (Right, back to start)
```

**After Step 2:**
```
lookup = {(0, 0), (0, 1)}  (both cleaned)
Robot back at (0, 1) facing original direction
Return to Step 1
```

### Step 3: goBack(robot) - Backtracking

**Context**: After DFS((0, 1), ...) returns, we need to go back to (0, 0)

```
Current position: (0, 1)
Need to return to: (0, 0)

goBack(robot):
  1. robot.turnLeft()   → Turn left (now facing different direction)
  2. robot.turnLeft()   → Turn left again (now facing opposite of original)
  3. robot.move()       → Move back to (0, 0)
  4. robot.turnRight()  → Turn right
  5. robot.turnRight()  → Turn right again (restore original facing)

Result: Robot back at (0, 0) facing original direction
```

---

## Understanding goBack() Function

**Purpose**: Return robot to previous cell after exploring a branch.

**How it works:**
```
After moving forward and exploring:
  Robot is at new position, facing forward direction
  
To go back:
  1. Turn left → Now facing left relative to forward
  2. Turn left → Now facing backward (opposite of forward)
  3. Move → Go back to previous cell
  4. Turn right → Restore orientation
  5. Turn right → Restore original facing direction
```

**Example:**
```
Robot at (0, 0) facing Right
Move right → Now at (0, 1) facing Right
Explore (0, 1)...
Now need to go back:

goBack():
  turnLeft()  → Now facing Up
  turnLeft()  → Now facing Left (opposite of Right)
  move()      → Move left, back to (0, 0)
  turnRight() → Now facing Up
  turnRight() → Now facing Right (original direction)

Result: Back at (0, 0) facing Right ✅
```

---

## Complete DFS Trace (Simplified Room)

**Room Layout:**
```
     -1  0  1
  -1  #  .  #
   0  .  .  .
   1  #  .  #
   
   Robot starts at (0, 0)
```

**DFS Execution:**

```
DFS((0, 0), d=0):
  Clean (0, 0)
  Try Right (0, 1): Move → DFS((0, 1))
    DFS((0, 1), d=0):
      Clean (0, 1)
      Try Right (0, 2): Blocked
      Try Down (1, 1): Move → DFS((1, 1))
        DFS((1, 1), d=1):
          Clean (1, 1)
          Try Down (2, 1): Blocked
          Try Left (1, 0): Move → DFS((1, 0))
            DFS((1, 0), d=2):
              Clean (1, 0)
              Try Left (1, -1): Blocked
              Try Up (0, 0): Already cleaned → Return
              Try Right (1, 1): Already cleaned → Return
              Try Down (2, 0): Blocked
              Return
            goBack → (1, 1)
          Try Up (0, 1): Already cleaned → Return
          Try Right (1, 2): Blocked
          Return
        goBack → (0, 1)
      Try Left (0, 0): Already cleaned → Return
      Try Up (-1, 1): Blocked
      Return
    goBack → (0, 0)
  Try Down (1, 0): Already cleaned → Return
  Try Left (0, -1): Blocked
  Try Up (-1, 0): Blocked
  Return

Result: All reachable cells cleaned!
```

---

## Key Concepts

### 1. Relative Coordinate System

The algorithm uses **relative coordinates**:
- Robot's starting position = (0, 0)
- All other positions are relative to start
- Doesn't need to know absolute room layout

**Why?**
- Room layout is unknown
- We only care about relative positions
- Set tracks visited positions regardless of absolute coordinates

### 2. Direction Tracking

**`d`** tracks which direction we're trying:
- `d = 0`: Right
- `d = 1`: Down
- `d = 2`: Left
- `d = 3`: Up

**Important**: `d` doesn't necessarily match robot's actual facing direction initially, but after rotations, it aligns.

### 3. Systematic Exploration

The algorithm tries all 4 directions from each cell:
- Ensures no direction is missed
- Uses rotation to systematically try each direction
- After trying all directions, returns to previous cell

### 4. Backtracking

After exploring a branch:
- Must return to previous cell
- `goBack()` handles this automatically
- Ensures robot can continue exploring other directions

### 5. Visited Tracking

**`lookup` set** prevents:
- Re-cleaning already cleaned cells
- Infinite loops
- Unnecessary revisits

**Base case**: If `pos in lookup`, return immediately.

---

## Visual Exploration Pattern

```
Example room:
┌─────┬─────┬─────┐
│  #  │  .  │  #  │
├─────┼─────┼─────┤
│  .  │  .  │  .  │
├─────┼─────┼─────┤
│  #  │  .  │  #  │
└─────┴─────┴─────┘

Exploration order (DFS):
Start: (0, 0)
  → (0, 1)
    → (1, 1)
      → (1, 0) ✓
      → (1, 2) ✓
      ← Back to (1, 1)
    ← Back to (0, 1)
  ← Back to (0, 0)
  → (1, 0) (already visited, skip)
  → (0, -1) (blocked)
  → (-1, 0) (blocked)

All reachable cells cleaned!
```

---

## Algorithm Pseudocode

```python
def cleanRoom(robot):
    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # R, D, L, U
    
    def goBack(robot):
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnRight()
        robot.turnRight()
    
    def dfs(pos, robot, d, lookup):
        # Base case: already cleaned
        if pos in lookup:
            return
        
        # Clean current cell
        lookup.add(pos)
        robot.clean()
        
        # Try all 4 directions
        for _ in range(4):
            # Calculate new position
            new_pos = (pos[0] + directions[d][0], 
                      pos[1] + directions[d][1])
            
            # Try to move
            if robot.move():
                # Explore new cell
                dfs(new_pos, robot, d, lookup)
                # Return to current cell
                goBack(robot)
            
            # Rotate to next direction
            robot.turnRight()
            d = (d + 1) % 4
    
    # Start DFS from (0, 0) facing direction 0
    dfs((0, 0), robot, 0, set())
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(4^N) | N = number of cells. In worst case, try 4 directions for each cell |
| **Space** | O(N) | lookup set stores all visited positions, recursion stack O(N) |

**Note**: In practice, many directions are blocked, so actual runtime is much better. The algorithm visits each cell at most once.

---

## Edge Cases

### Case 1: Single Cell Room
```
Room: [.]
Result: Clean (0, 0), try 4 directions (all blocked), done
```

### Case 2: Linear Room
```
Room: [. . .]
Result: Clean in order: (0,0) → (0,1) → (0,2)
```

### Case 3: All Blocked
```
Room: All cells blocked except start
Result: Clean (0, 0), try 4 directions (all blocked), done
```

### Case 4: Large Open Space
```
Room: Large grid of empty cells
Result: DFS explores all cells systematically
```

---

## Why This Algorithm Works

### Correctness

1. **Exhaustive Exploration**: Tries all 4 directions from each cell
2. **No Revisits**: `lookup` set prevents cleaning same cell twice
3. **Backtracking**: Always returns to previous cell after exploring
4. **Systematic**: Rotates through all directions in order

### Completeness

- If a cell is reachable, the algorithm will eventually reach it
- DFS explores all connected cells
- Backtracking ensures all branches are explored

### Efficiency

- Each cell is visited at most once
- Directions are tried systematically
- Blocked cells are detected immediately (no wasted moves)

---

## Alternative Approaches

### Approach 1: BFS (Breadth-First Search)

```python
def cleanRoom_BFS(robot):
    from collections import deque
    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    while queue:
        x, y = queue.popleft()
        robot.clean()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited:
                if robot.move():
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    # Need to go back...
```

**Problem**: BFS requires knowing how to navigate back, which is complex with robot API.

### Approach 2: Right-Hand Rule

Always turn right when hitting a wall:
- Simple but may miss some cells
- Not guaranteed to clean all cells

**DFS is better** because it's guaranteed to explore all reachable cells.

---

## Summary

The robot room cleaner algorithm:
- Uses **DFS with backtracking** to explore all reachable cells
- Tracks visited positions to avoid re-cleaning
- Tries all 4 directions systematically from each cell
- Uses `goBack()` to return to previous cell after exploring
- Time complexity: **O(4^N)** worst case, but O(N) in practice
- Space complexity: **O(N)** for visited set and recursion stack

**Key Insight**: Use DFS to explore like a maze. Track visited positions to avoid loops. Always backtrack to previous cell after exploring a branch. This ensures all reachable cells are cleaned exactly once.

---

## Related Problems

- **LeetCode 200**: Number of Islands (similar DFS exploration)
- **LeetCode 130**: Surrounded Regions
- **LeetCode 79**: Word Search
- **LeetCode 489**: Robot Room Cleaner (this problem)

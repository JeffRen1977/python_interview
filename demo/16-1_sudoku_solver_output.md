# Sudoku Solver

> **LeetCode 37**: Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy all of the following rules: Each row must contain digits 1-9 without repetition. Each column must contain digits 1-9 without repetition. Each of the 9 3x3 sub-boxes must contain digits 1-9 without repetition.

## Problem Description

Solve a 9×9 Sudoku puzzle by filling empty cells (represented by '.') with digits 1-9.

**Rules:**
1. Each row must contain digits 1-9 without repetition
2. Each column must contain digits 1-9 without repetition
3. Each 3×3 sub-box must contain digits 1-9 without repetition

**Example:**
```
Input:
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9

Output: (solved puzzle)
```

---

## Key Insight

Use **Backtracking with DFS**:
- Find all empty cells
- Try digits 1-9 for each empty cell
- Check validity (row, column, 3×3 box)
- If valid, place digit and recurse to next empty cell
- If solution found, return True
- If no valid digit works, backtrack (undo placement)

**Strategy**: Systematically try all possibilities, backtracking when constraints are violated.

---

## Algorithm Logic

```
1. Find all empty cells (coordinates where board[i][j] == '.')

2. DFS(board, empty, start, N):
   Base case: if start >= N (all cells filled):
     return True
   
   Get current empty cell: (x, y) = empty[start]
   
   For each digit k from 1 to 9:
     If isValid(board, x, y, k):
       board[x][y] = k
       If DFS(board, empty, start + 1, N):
         return True  (solution found)
       board[x][y] = '.'  (backtrack)
   
   return False  (no valid digit)

3. isValid(board, x, y, digit):
   Check row x: no duplicate digit
   Check column y: no duplicate digit
   Check 3×3 box containing (x,y): no duplicate digit
```

---

## Detailed Example: Step-by-Step

**Input Board:**
```
    0  1  2  3  4  5  6  7  8
0   5  3  .  .  7  .  .  .  .
1   6  .  .  1  9  5  .  .  .
2   .  9  8  .  .  .  .  6  .
3   8  .  .  .  6  .  .  .  3
4   4  .  .  8  .  3  .  .  1
5   7  .  .  .  2  .  .  .  6
6   .  6  .  .  .  .  2  8  .
7   .  .  .  4  1  9  .  .  5
8   .  .  .  .  8  .  .  7  9
```

### Step 1: Find Empty Cells

```
empty = [
  (0, 2), (0, 3), (0, 5), (0, 6), (0, 7), (0, 8),  # Row 0
  (1, 1), (1, 2), (1, 6), (1, 7), (1, 8),          # Row 1
  (2, 0), (2, 3), (2, 4), (2, 5), (2, 6), (2, 8), # Row 2
  (3, 1), (3, 2), (3, 3), (3, 5), (3, 6), (3, 7), # Row 3
  (4, 1), (4, 2), (4, 4), (4, 6), (4, 7),         # Row 4
  (5, 1), (5, 2), (5, 3), (5, 5), (5, 6), (5, 7), # Row 5
  (6, 0), (6, 2), (6, 3), (6, 4), (6, 5), (6, 8), # Row 6
  (7, 0), (7, 1), (7, 2), (7, 6), (7, 7),         # Row 7
  (8, 0), (8, 1), (8, 2), (8, 3), (8, 5), (8, 6)  # Row 8
]

Total empty cells: N = 51
```

### Step 2: DFS Traversal

**DFS call sequence (simplified for first few cells):**

#### DFS(empty, start=0) - Cell (0, 2)

```
Current cell: (0, 2)
Row 0: [5, 3, ., ., 7, ., ., ., .]
Column 2: [., ., 8, ., ., ., ., ., .]
Box (0,0): 
  5  3  .
  6  .  .
  .  9  8

Try digits 1-9:
  k=1: Row 0 has no 1, Col 2 has no 1, Box has no 1 → Valid ✅
    Place: board[0][2] = '1'
    Call: DFS(empty, start=1)
    
    ... (recursive call) ...
    
    If solution found → return True
    If no solution → backtrack: board[0][2] = '.'
  
  k=2: Row 0 has no 2, Col 2 has no 2, Box has no 2 → Valid ✅
    Place: board[0][2] = '2'
    Call: DFS(empty, start=1)
    ...
  
  k=3: Row 0 has 3 → Invalid ❌
  
  k=4: Row 0 has no 4, Col 2 has no 4, Box has no 4 → Valid ✅
    ...
  
  ... (continue for all digits) ...
```

**Detailed validation for (0, 2) with digit '1':**

```
isValid(board, 0, 2, rows, cols, '1'):

1. Check Row 0:
   for j in range(9):
     board[0][j] == '1'?
     Row 0: [5, 3, ., ., 7, ., ., ., .]
     No '1' found ✅

2. Check Column 2:
   for i in range(9):
     board[i][2] == '1'?
     Column 2: [., ., 8, ., ., ., ., ., .]
     No '1' found ✅

3. Check 3×3 Box:
   boundary_x = 0 - 0 % 3 = 0
   boundary_y = 2 - 2 % 3 = 0
   Box (0,0) to (2,2):
     5  3  .
     6  .  .
     .  9  8
   No '1' found ✅

Result: Valid! ✅
```

#### DFS(empty, start=1) - Cell (0, 3)

```
Current cell: (0, 3)
Row 0: [5, 3, 1, ., 7, ., ., ., .]  (assuming '1' was placed)
Column 3: [., 1, ., ., 8, ., ., 4, .]
Box (0,0): 
  5  3  1
  6  .  .
  .  9  8

Try digits 1-9:
  k=1: Row 0 has 1 (at col 2) → Invalid ❌
  k=2: Row 0 has no 2, Col 3 has no 2, Box has no 2 → Valid ✅
    Place: board[0][3] = '2'
    Call: DFS(empty, start=2)
    ...
  
  k=3: Row 0 has 3 → Invalid ❌
  k=4: Row 0 has no 4, Col 3 has 4 (at row 7) → Invalid ❌
  ...
```

### Step 3: Backtracking Example

**Scenario**: We've filled several cells, but reach a dead end:

```
Partial solution:
5  3  1  2  7  .  .  .  .
6  .  .  1  9  5  .  .  .
.  9  8  .  .  .  .  6  .
...

Current cell: (1, 1) - trying to fill
Row 1: [6, ., ., 1, 9, 5, ., ., .]
Column 1: [3, ., 9, ., ., ., 6, ., .]
Box (0,0): 
  5  3  1
  6  .  .
  .  9  8

Try digits 1-9:
  k=1: Row 1 has 1 → Invalid ❌
  k=2: Row 1 has no 2, Col 1 has no 2, Box has no 2 → Valid ✅
    Place: board[1][1] = '2'
    Call: DFS(empty, start=next)
    
    ... (continue recursively) ...
    
    Eventually reach a cell where NO digit works
    → Return False
    
    Backtrack: board[1][1] = '.'
  
  k=3: Row 1 has no 3, Col 1 has 3 (at row 0) → Invalid ❌
  k=4: Row 1 has no 4, Col 1 has no 4, Box has no 4 → Valid ✅
    Place: board[1][1] = '4'
    Call: DFS(empty, start=next)
    ...
    (continue until solution found or all options exhausted)
```

---

## Detailed Validation Function

### isValid(board, x, y, rows, cols, digit)

**Example: Check if '4' is valid at (4, 1)**

```
x = 4, y = 1, digit = '4'

1. Check Row 4:
   for j in range(9):
     board[4][j] == '4'?
     Row 4: [4, ., ., 8, ., 3, ., ., 1]
     board[4][0] = '4' → Found! ❌
   Return False
```

**Example: Check if '2' is valid at (4, 1)**

```
x = 4, y = 1, digit = '2'

1. Check Row 4:
   for j in range(9):
     board[4][j] == '2'?
     Row 4: [4, ., ., 8, ., 3, ., ., 1]
     No '2' found ✅

2. Check Column 1:
   for i in range(9):
     board[i][1] == '2'?
     Column 1: [3, ., 9, ., ., ., 6, ., .]
     No '2' found ✅

3. Check 3×3 Box:
   boundary_x = 4 - 4 % 3 = 4 - 1 = 3
   boundary_y = 1 - 1 % 3 = 1 - 1 = 0
   Box (3,0) to (5,2):
     8  .  .
     4  .  .
     7  .  .
   No '2' found ✅

Result: Valid! ✅
```

### Understanding 3×3 Box Boundaries

**Formula**: `boundary = position - position % 3`

| Position | % 3 | Boundary | Box Range |
|----------|-----|----------|-----------|
| 0 | 0 | 0 | 0-2 |
| 1 | 1 | 0 | 0-2 |
| 2 | 2 | 0 | 0-2 |
| 3 | 0 | 3 | 3-5 |
| 4 | 1 | 3 | 3-5 |
| 5 | 2 | 3 | 3-5 |
| 6 | 0 | 6 | 6-8 |
| 7 | 1 | 6 | 6-8 |
| 8 | 2 | 6 | 6-8 |

**Example**: Cell (4, 7)
- `boundary_x = 4 - 1 = 3` → Box rows: 3, 4, 5
- `boundary_y = 7 - 1 = 6` → Box cols: 6, 7, 8
- Box: (3,6) to (5,8)

---

## Complete DFS Trace (Simplified)

**For first few empty cells:**

```
DFS(empty, start=0): Cell (0, 2)
  Try '1': Valid → Place → DFS(start=1)
    DFS(empty, start=1): Cell (0, 3)
      Try '1': Invalid (row has '1')
      Try '2': Valid → Place → DFS(start=2)
        DFS(empty, start=2): Cell (0, 5)
          Try '1': Invalid (row has '1')
          Try '2': Invalid (row has '2')
          Try '3': Invalid (row has '3')
          Try '4': Valid → Place → DFS(start=3)
            ... (continue) ...
            If solution found → return True
            If dead end → backtrack
          Backtrack: board[0][5] = '.'
        Backtrack: board[0][3] = '.'
    Backtrack: board[0][2] = '.'
  
  Try '2': Valid → Place → DFS(start=1)
    ... (similar process) ...
  
  Try '4': Valid → Place → DFS(start=1)
    ... (eventually finds solution) ...
    return True
```

---

## Key Concepts

### 1. Backtracking

**Backtracking** is a systematic way to try all possibilities:
1. Make a choice (place a digit)
2. Recurse to solve the rest
3. If solution found → return True
4. If no solution → undo choice (backtrack) and try next option

**Why backtrack?**
- Early choices might lead to dead ends
- Need to undo wrong choices and try alternatives
- `board[x][y] = '.'` undoes the placement

### 2. Constraint Checking

Three constraints must be satisfied:
1. **Row constraint**: No duplicate in the same row
2. **Column constraint**: No duplicate in the same column
3. **Box constraint**: No duplicate in the 3×3 box

### 3. Empty Cell Ordering

The algorithm processes empty cells in order:
- First finds all empty cells
- Processes them sequentially (left-to-right, top-to-bottom)
- This order doesn't affect correctness, but affects efficiency

### 4. Why Process Empty Cells First?

By finding all empty cells upfront:
- We know exactly how many cells need filling
- We can process them in order
- Base case is clear: `start >= N`

---

## Visual Example

```
Initial Board:
┌─────┬─────┬─────┐
│ 5 3 │ . . │ 7 . │
│ 6 . │ . 1 │ 9 5 │
│ . 9 │ 8 . │ . . │
├─────┼─────┼─────┤
│ 8 . │ . . │ 6 . │
│ 4 . │ . 8 │ . 3 │
│ 7 . │ . . │ 2 . │
├─────┼─────┼─────┤
│ . 6 │ . . │ . . │
│ . . │ . 4 │ 1 9 │
│ . . │ . . │ 8 . │
└─────┴─────┴─────┘

After filling first few cells:
┌─────┬─────┬─────┐
│ 5 3 │ 1 2 │ 7 4 │
│ 6 . │ . 1 │ 9 5 │
│ . 9 │ 8 . │ . . │
├─────┼─────┼─────┤
│ 8 . │ . . │ 6 . │
│ 4 . │ . 8 │ . 3 │
│ 7 . │ . . │ 2 . │
├─────┼─────┼─────┤
│ . 6 │ . . │ . . │
│ . . │ . 4 │ 1 9 │
│ . . │ . . │ 8 . │
└─────┴─────┴─────┘
```

---

## Algorithm Pseudocode

```python
def solveSudoku(board):
    rows, cols = len(board), len(board[0])
    empty = emptySlots(board, rows, cols)
    DFS(board, empty, 0, len(empty), rows, cols)

def emptySlots(board, rows, cols):
    empty = []
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '.':
                empty.append((i, j))
    return empty

def DFS(board, empty, start, N, rows, cols):
    if start >= N:
        return True  # All cells filled
    
    x, y = empty[start]
    
    for k in range(1, 10):
        if isValid(board, x, y, rows, cols, str(k)):
            board[x][y] = str(k)
            if DFS(board, empty, start + 1, N, rows, cols):
                return True
            board[x][y] = '.'  # Backtrack
    
    return False

def isValid(board, x, y, rows, cols, digit):
    # Check row
    for j in range(cols):
        if board[x][j] == digit:
            return False
    
    # Check column
    for i in range(rows):
        if board[i][y] == digit:
            return False
    
    # Check 3×3 box
    boundary_x = x - x % 3
    boundary_y = y - y % 3
    for i in range(boundary_x, boundary_x + 3):
        for j in range(boundary_y, boundary_y + 3):
            if board[i][j] == digit:
                return False
    
    return True
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(9^m) | m = number of empty cells. In worst case, try 9 digits for each empty cell |
| **Space** | O(m) | Recursion stack depth (m levels), plus empty list storage |

**Note**: In practice, many branches are pruned early by constraint checking, so actual runtime is much better than worst case.

---

## Optimization Strategies

### 1. Most Constrained First

Process cells with fewer valid options first:
- Count valid digits for each empty cell
- Sort empty cells by number of valid options
- Process most constrained cells first

### 2. Forward Checking

After placing a digit, immediately check if any empty cell has no valid options:
- If yes, backtrack early (don't recurse)

### 3. Constraint Propagation

Use constraint propagation to eliminate possibilities:
- When a digit is placed, remove it from possibilities in same row/column/box

---

## Edge Cases

### Case 1: Already Solved
```
Board has no empty cells
Result: Return immediately (start >= N)
```

### Case 2: Unsolvable
```
No valid solution exists
Result: After trying all possibilities, return False
Board remains unchanged
```

### Case 3: Multiple Solutions
```
Multiple valid solutions exist
Result: Algorithm finds one solution (first valid one)
```

### Case 4: Single Empty Cell
```
Only one empty cell
Result: Try digits 1-9, find valid one, place it, done
```

---

## Why This Algorithm Works

### Correctness

1. **Exhaustive Search**: Tries all possible digit placements
2. **Constraint Satisfaction**: Only places valid digits (satisfies all rules)
3. **Backtracking**: Undoes wrong choices and tries alternatives
4. **Termination**: Either finds solution or exhausts all possibilities

### Completeness

- If a solution exists, the algorithm will find it (eventually)
- If no solution exists, the algorithm will determine this after trying all possibilities

### Efficiency

- Constraint checking prunes invalid branches early
- Backtracking avoids exploring impossible paths
- In practice, solves most puzzles quickly

---

## Summary

The sudoku solver algorithm:
- Uses **backtracking with DFS** to try all possibilities
- Finds all empty cells first
- For each empty cell, tries digits 1-9
- Checks validity (row, column, 3×3 box)
- Backtracks when no valid digit works
- Time complexity: **O(9^m)** where m = empty cells
- Space complexity: **O(m)** for recursion stack

**Key Insight**: Use backtracking to systematically explore all possibilities. Constraint checking prunes invalid branches early, making the algorithm efficient in practice.

---

## Related Problems

- **LeetCode 36**: Valid Sudoku (check if board is valid)
- **LeetCode 37**: Sudoku Solver (this problem)
- **LeetCode 51**: N-Queens (similar backtracking)
- **LeetCode 52**: N-Queens II

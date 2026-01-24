# File System Size Calculation

> **Problem**: Implement a file system that can calculate the total size of files and directories. Directories contain files and/or other directories, and their size is the sum of all their contents.

## Problem Description

Calculate the size of a file or directory in a file system:
- **Files** have a direct size
- **Directories** have a size equal to the sum of all files and subdirectories they contain
- The file system is represented as a tree structure with entities (files/directories) identified by IDs

**Key Requirements:**
- Files have a fixed size
- Directories contain children (files or subdirectories)
- Directory size = sum of all descendant file sizes
- Handle invalid entity IDs

---

## Key Insight

**Tree Structure with Recursive Size Calculation:**
- File system is a tree: directories are nodes, files are leaves
- Use **DFS (Depth-First Search)** to traverse the tree
- For files: return their size directly
- For directories: recursively sum sizes of all children

**Algorithm Approach:**
- Build a dictionary mapping entity IDs to entities
- Use DFS to recursively calculate directory sizes
- Base case: file → return size
- Recursive case: directory → sum sizes of all children

---

## Data Structure

### Entity Class

```python
class Entity:
    id: int           # Unique identifier
    type: str         # 'file' or 'directory'
    name: str         # Name of the entity
    size: int         # Size (for files) or 0 (for directories)
    children: List   # List of child entity IDs (for directories)
```

**Example:**
```python
Entity(id=3, type='file', name="file1", size=300, children=[])
Entity(id=1, type='directory', name="root", size=0, children=[2, 3])
```

---

## Algorithm Logic

```
1. Build entity dictionary:
   - Map entity ID → Entity object
   - Allows O(1) lookup by ID

2. entity_size(entity_id):
   - Check if entity_id exists
   - If file: return entity.size
   - If directory: call dfs(entity)

3. dfs(entity):
   - Base case: if file → return size
   - Base case: if empty directory → return 0
   - Recursive: sum dfs(child) for all children
```

---

## File System Structure

**Example File System:**

```
root (id=1, directory)
├── dir (id=2, directory)
│   ├── file2 (id=4, file, size=100)
│   └── file3 (id=5, file, size=200)
└── file1 (id=3, file, size=300)

Entity Details:
  ID 1: directory "root", children=[2, 3]
  ID 2: directory "dir", children=[4, 5]
  ID 3: file "file1", size=300
  ID 4: file "file2", size=100
  ID 5: file "file3", size=200
```

---

## Detailed Example: Step-by-Step

### Example 1: Calculate Size of Root Directory (ID=1)

**Input**: `entity_id = 1`

#### Step 1: Check Entity Existence

```
entity_id = 1
Check: 1 in id_to_entity? YES
entity = id_to_entity[1]
  entity.type = 'directory'
  entity.name = "root"
  entity.children = [2, 3]
```

#### Step 2: Call DFS on Root Directory

```
Call: dfs(entity with id=1)
```

#### Step 3: DFS Recursion - Process Root

```
dfs(entity id=1):
  entity.type = 'directory' (not 'file')
  entity.children = [2, 3] (not empty)
  
  Initialize: total_size = 0
  
  Process child_id = 2:
    child_entity = id_to_entity[2]
    Call: dfs(child_entity id=2)
    Add result to total_size
```

#### Step 4: DFS Recursion - Process Directory "dir" (ID=2)

```
dfs(entity id=2):
  entity.type = 'directory'
  entity.children = [4, 5]
  
  Initialize: total_size = 0
  
  Process child_id = 4:
    child_entity = id_to_entity[4]
    Call: dfs(child_entity id=4)
```

#### Step 5: DFS Base Case - Process File "file2" (ID=4)

```
dfs(entity id=4):
  entity.type = 'file' ✅ (base case)
  Return: entity.size = 100
```

**Back to dfs(id=2):**
```
total_size += 100  → total_size = 100

Process child_id = 5:
  child_entity = id_to_entity[5]
  Call: dfs(child_entity id=5)
```

#### Step 6: DFS Base Case - Process File "file3" (ID=5)

```
dfs(entity id=5):
  entity.type = 'file' ✅ (base case)
  Return: entity.size = 200
```

**Back to dfs(id=2):**
```
total_size += 200  → total_size = 100 + 200 = 300
Return: 300
```

**Back to dfs(id=1):**
```
total_size += 300  → total_size = 0 + 300 = 300

Process child_id = 3:
  child_entity = id_to_entity[3]
  Call: dfs(child_entity id=3)
```

#### Step 7: DFS Base Case - Process File "file1" (ID=3)

```
dfs(entity id=3):
  entity.type = 'file' ✅ (base case)
  Return: entity.size = 300
```

**Back to dfs(id=1):**
```
total_size += 300  → total_size = 300 + 300 = 600
Return: 600
```

#### Result

```
entity_size(1) = 600 ✅

Breakdown:
  Directory "dir" (id=2): 100 + 200 = 300
  File "file1" (id=3): 300
  Total: 300 + 300 = 600
```

---

### Example 2: Calculate Size of Directory "dir" (ID=2)

**Input**: `entity_id = 2`

#### Step-by-Step Execution

```
Step 1: Check entity_id = 2
  entity = id_to_entity[2]
  entity.type = 'directory'
  
Step 2: Call dfs(entity id=2)
  
Step 3: Process children [4, 5]
  dfs(id=4) → returns 100 (file)
  dfs(id=5) → returns 200 (file)
  
Step 4: Sum
  total_size = 100 + 200 = 300
  
Result: entity_size(2) = 300 ✅
```

---

### Example 3: Calculate Size of File (ID=3)

**Input**: `entity_id = 3`

#### Step-by-Step Execution

```
Step 1: Check entity_id = 3
  entity = id_to_entity[3]
  entity.type = 'file' ✅
  
Step 2: Return entity.size directly
  return 300
  
Result: entity_size(3) = 300 ✅
```

**Note**: For files, no DFS is needed - just return the size directly.

---

### Example 4: Invalid Entity ID

**Input**: `entity_id = 10`

#### Step-by-Step Execution

```
Step 1: Check entity_id = 10
  10 in id_to_entity? NO
  
Step 2: Return -1 (error indicator)
  
Result: entity_size(10) = -1 ✅
```

---

## Visual DFS Execution Tree

### Calculating Size of Root Directory (ID=1)

```
entity_size(1)
  │
  ├─> dfs(id=1, directory "root")
      │
      ├─> dfs(id=2, directory "dir")
      │   │
      │   ├─> dfs(id=4, file "file2")
      │   │   └─> Return 100 ✅
      │   │
      │   └─> dfs(id=5, file "file3")
      │       └─> Return 200 ✅
      │
      │   Sum: 100 + 200 = 300
      │   Return 300 ✅
      │
      └─> dfs(id=3, file "file1")
          └─> Return 300 ✅
      
      Sum: 300 + 300 = 600
      Return 600 ✅
```

**Execution Order:**
1. dfs(1) → calls dfs(2) and dfs(3)
2. dfs(2) → calls dfs(4) and dfs(5)
3. dfs(4) → returns 100 (base case)
4. dfs(5) → returns 200 (base case)
5. dfs(2) → returns 300 (100 + 200)
6. dfs(3) → returns 300 (base case)
7. dfs(1) → returns 600 (300 + 300)

---

## Key Concepts

### 1. Tree Structure

**File System as Tree:**
- Root directory is the root node
- Directories are internal nodes
- Files are leaf nodes
- Children relationships form edges

**Visual:**
```
        root (1)
       /        \
    dir (2)    file1 (3)
   /      \
file2 (4) file3 (5)
```

### 2. Recursive Size Calculation

**Recursive Definition:**
- **File size**: Direct size value
- **Directory size**: Sum of sizes of all children

**Mathematical:**
```
size(entity) = {
    entity.size,                    if entity is file
    Σ size(child) for all children,  if entity is directory
}
```

### 3. DFS (Depth-First Search)

**Why DFS?**
- Natural fit for tree traversal
- Processes all descendants before returning
- Ensures children are calculated before parent

**DFS Pattern:**
```
def dfs(node):
    if is_leaf(node):
        return base_value
    result = 0
    for child in children(node):
        result += dfs(child)
    return result
```

### 4. Base Cases

**Two Base Cases:**

1. **File**: Return size directly
   ```python
   if entity.type == 'file':
       return entity.size
   ```

2. **Empty Directory**: Return 0
   ```python
   if entity.type == 'directory' and len(entity.children) == 0:
       return 0
   ```

### 5. Dictionary Lookup

**Why use dictionary?**
- O(1) lookup by entity ID
- Efficient access to entities
- Maps ID → Entity object

**Structure:**
```python
id_to_entity = {
    1: Entity(id=1, type='directory', ...),
    2: Entity(id=2, type='directory', ...),
    3: Entity(id=3, type='file', ...),
    ...
}
```

---

## Algorithm Pseudocode

```python
def entity_size(entity_id):
    if entity_id not in id_to_entity:
        return -1  # Error: entity not found
    
    entity = id_to_entity[entity_id]
    
    if entity.type == 'file':
        return entity.size  # Direct return for files
    
    if entity.type == 'directory':
        return dfs(entity)  # Recursive calculation for directories

def dfs(entity):
    # Base case: file
    if entity.type == 'file':
        return entity.size
    
    # Base case: empty directory
    if entity.type == 'directory' and len(entity.children) == 0:
        return 0
    
    # Recursive case: sum children
    total_size = 0
    for child_id in entity.children:
        child_entity = id_to_entity[child_id]
        total_size += dfs(child_entity)
    
    return total_size
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(N) | N = total number of entities. DFS visits each entity once |
| **Space** | O(H) | H = height of tree. Recursion stack depth equals tree height |

**Where:**
- N = total number of entities in the file system
- H = maximum depth of the directory tree

**Time Complexity:**
- Each entity is visited exactly once
- Dictionary lookup: O(1)
- Total: O(N)

**Space Complexity:**
- Recursion stack: O(H) where H is tree height
- In worst case (linear tree): O(N)
- In balanced tree: O(log N)

---

## Edge Cases

### Case 1: Empty Directory
```
Directory with no children
Result: 0 (correct - empty directory has size 0)
```

### Case 2: Single File
```
Directory containing one file
Result: size of that file
```

### Case 3: Nested Directories
```
Directory containing subdirectories
Result: Sum of all nested file sizes
```

### Case 4: Invalid Entity ID
```
entity_id not in id_to_entity
Result: -1 (error indicator)
```

### Case 5: File (Not Directory)
```
Direct file access
Result: Direct size (no recursion needed)
```

### Case 6: Deep Nesting
```
Very deep directory structure
Result: Correctly calculates sum (handled by recursion)
```

---

## Step-by-Step Execution Table

### Example: Calculate Size of Root (ID=1)

| Step | Function Call | Entity | Type | Action | Return Value |
|------|--------------|--------|------|--------|--------------|
| 1 | entity_size(1) | root (1) | directory | Call dfs(1) | - |
| 2 | dfs(1) | root (1) | directory | Process child 2 | - |
| 3 | dfs(2) | dir (2) | directory | Process child 4 | - |
| 4 | dfs(4) | file2 (4) | file | Base case | 100 |
| 5 | dfs(2) | dir (2) | directory | Add 100, process child 5 | - |
| 6 | dfs(5) | file3 (5) | file | Base case | 200 |
| 7 | dfs(2) | dir (2) | directory | Sum: 100+200 | 300 |
| 8 | dfs(1) | root (1) | directory | Add 300, process child 3 | - |
| 9 | dfs(3) | file1 (3) | file | Base case | 300 |
| 10 | dfs(1) | root (1) | directory | Sum: 300+300 | 600 |
| 11 | entity_size(1) | root (1) | directory | Return result | 600 |

---

## Why This Algorithm Works

### Correctness

1. **Base Cases Handle Leaves:**
   - Files return their size directly
   - Empty directories return 0
   - Both are correct

2. **Recursive Case Handles Internal Nodes:**
   - Sums sizes of all children
   - Children are processed recursively
   - Ensures all descendants are included

3. **DFS Ensures Complete Traversal:**
   - Visits all nodes in subtree
   - Processes children before parent
   - No node is missed or double-counted

### Why DFS?

**DFS is natural for tree problems:**
- Tree structure matches recursive nature
- Processes all descendants before returning
- Simple to implement and understand

**Alternative: BFS**
- Could use BFS with level-order traversal
- More complex (need to track levels)
- DFS is more intuitive for this problem

---

## Alternative Approaches

### 1. Iterative DFS (Using Stack)

```python
def dfs_iterative(entity):
    stack = [entity]
    total = 0
    
    while stack:
        current = stack.pop()
        if current.type == 'file':
            total += current.size
        else:
            for child_id in current.children:
                stack.append(id_to_entity[child_id])
    
    return total
```

**Pros:** No recursion stack limit
**Cons:** More complex, less intuitive

### 2. Memoization (Caching)

```python
cache = {}

def dfs_memoized(entity):
    if entity.id in cache:
        return cache[entity.id]
    
    if entity.type == 'file':
        result = entity.size
    else:
        result = sum(dfs_memoized(id_to_entity[c]) for c in entity.children)
    
    cache[entity.id] = result
    return result
```

**Pros:** Avoids recalculating same directory
**Cons:** More memory, only useful if same directory queried multiple times

### 3. Bottom-Up Calculation

**Idea:** Calculate all sizes once, store in dictionary

```python
def calculate_all_sizes():
    sizes = {}
    
    def dfs(entity):
        if entity.id in sizes:
            return sizes[entity.id]
        # ... calculate size ...
        sizes[entity.id] = result
        return result
    
    # Calculate for all entities
    for entity in id_to_entity.values():
        dfs(entity)
    
    return sizes
```

**Pros:** Efficient for multiple queries
**Cons:** More memory, unnecessary if only querying once

---

## Real-World Applications

1. **File System Management:**
   - Calculate disk usage
   - Find largest directories
   - Disk quota management

2. **Package Managers:**
   - Calculate total package size
   - Dependency size analysis

3. **Cloud Storage:**
   - Storage billing
   - Usage monitoring

4. **Backup Systems:**
   - Estimate backup size
   - Progress tracking

---

## Common Mistakes

### Mistake 1: Not Handling Empty Directories

```python
# WRONG: Assumes directories always have children
def dfs(entity):
    total = 0
    for child_id in entity.children:  # Error if children is empty!
        total += dfs(id_to_entity[child_id])
    return total
```

**Fix:** Check for empty directory:
```python
if len(entity.children) == 0:
    return 0
```

### Mistake 2: Not Checking Entity Type

```python
# WRONG: Doesn't distinguish files from directories
def dfs(entity):
    return entity.size  # Wrong for directories!
```

**Fix:** Check type first:
```python
if entity.type == 'file':
    return entity.size
```

### Mistake 3: Infinite Recursion (Circular References)

**Problem:** If directory contains itself (circular reference), DFS loops forever

**Solution:** Add visited set or validate structure:
```python
visited = set()

def dfs(entity, visited):
    if entity.id in visited:
        return 0  # Already processed
    visited.add(entity.id)
    # ... rest of DFS ...
```

---

## Summary

The File System size calculation algorithm:
- Uses **tree structure** to represent file system
- Uses **DFS** to recursively calculate directory sizes
- **Base cases**: Files return size, empty directories return 0
- **Recursive case**: Sum sizes of all children
- Time complexity: **O(N)** where N = number of entities
- Space complexity: **O(H)** where H = tree height

**Key Insight**: Directory size is the sum of all descendant file sizes. DFS naturally traverses the tree and accumulates sizes from leaves to root.

---

## Related Problems

- **LeetCode 690**: Employee Importance (similar tree structure)
- **LeetCode 339**: Nested List Weight Sum (recursive sum calculation)
- **Directory Size Calculation**: Real-world file system problem
- **Tree Sum Problems**: Various tree traversal and sum problems

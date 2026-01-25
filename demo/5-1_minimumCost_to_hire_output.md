# Minimum Cost to Hire K Workers

> **LeetCode 857**: There are N workers. The i-th worker has a quality[i] and a minimum wage expectation wage[i]. We want to hire exactly K workers to form a paid group. When hiring a group of K workers, we must pay them according to the following rules:
> 1. Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
> 2. Every worker in the paid group must be paid at least their minimum wage expectation.
> Given integer K, return the least amount of money needed to form a paid group satisfying the above conditions.

## Problem Description

Find the minimum cost to hire exactly K workers such that:
- All workers are paid proportionally to their quality
- Each worker receives at least their minimum wage
- Total cost is minimized

**Payment Rule:**
- If worker i has quality `q_i` and we use ratio `r`
- Worker i is paid: `r × q_i`
- Constraint: `r × q_i ≥ wage[i]`
- This means: `r ≥ wage[i] / q_i = ratio[i]`

**Key Insight:**
- If we use worker j as "captain" (determines the ratio)
- Ratio used: `r = wage[j] / quality[j]`
- All workers must have `ratio[i] ≤ r` (to satisfy minimum wage)
- Cost: `r × sum of all K workers' qualities`
- To minimize cost: minimize `sum of qualities` for given ratio

---

## Key Insight

**Greedy Strategy:**
1. **Sort by ratio**: `wage[i] / quality[i]` (ascending)
2. **For each worker as captain**: Use their ratio for all workers
3. **Select K-1 lowest quality workers**: From workers with ratio ≤ captain's ratio
4. **Calculate cost**: `captain_ratio × sum_of_qualities`
5. **Return minimum cost**

**Why This Works:**
- When processing workers in sorted order, we've seen all workers with ratio ≤ current
- For each worker as captain, we want the K workers (including captain) with lowest quality
- Max-heap tracks highest quality workers, remove them when we exceed K

**Data Structure:**
- Max-heap (using negative values) to track highest quality workers
- When we have more than K workers, remove the one with highest quality
- This keeps the K workers with lowest quality

---

## Algorithm Logic

```
1. Calculate ratios: wq = [(wage[i]/quality[i], quality[i]) for all i]
2. Sort by ratio (ascending)

3. Initialize:
   - res = infinity
   - heap = [] (max-heap using negative values)
   - qSum = 0 (sum of qualities in current group)

4. For each (ratio, quality) in sorted list:
   a. Add quality to qSum
   b. Push -quality to heap (max-heap simulation)
   c. If heap size > K:
      - Pop highest quality (most negative value)
      - Subtract from qSum (add negative = subtract)
   d. If heap size == K:
      - Calculate cost = ratio × qSum
      - Update res = min(res, cost)

5. Return res
```

---

## Detailed Example 1: Step-by-Step

**Input**: `quality = [10, 20, 5]`, `wage = [70, 50, 30]`, `K = 2`

### Step 1: Calculate Ratios

```
Worker 0: ratio = 70/10 = 7.0, quality = 10
Worker 1: ratio = 50/20 = 2.5, quality = 20
Worker 2: ratio = 30/5 = 6.0, quality = 5

wq = [(2.5, 20), (6.0, 5), (7.0, 10)]
     (sorted by ratio: 2.5 < 6.0 < 7.0)
```

### Step 2: Initialize

```
res = inf
heap = []
qSum = 0
```

### Step 3: Process Worker 1 (ratio = 2.5, quality = 20)

```
ratio = 2.5, q = 20

Add to heap:
  qSum += 20 → qSum = 20
  heapq.heappush(heap, -20) → heap = [-20]
  (Note: Python's heapq is min-heap, so -20 makes it max-heap)

Check size:
  len(heap) = 1 < K = 2
  Not enough workers yet, skip cost calculation

State:
  heap = [-20]  (represents quality 20)
  qSum = 20
  res = inf
```

### Step 4: Process Worker 2 (ratio = 6.0, quality = 5)

```
ratio = 6.0, q = 5

Add to heap:
  qSum += 5 → qSum = 25
  heapq.heappush(heap, -5) → heap = [-20, -5]
  (Heap structure: [-20, -5] or [-5, -20] depending on heapify)

Check size:
  len(heap) = 2 == K ✅
  We have exactly K workers!
  
  Calculate cost:
    cost = ratio × qSum = 6.0 × 25 = 150.0
    res = min(inf, 150.0) = 150.0

State:
  heap = [-20, -5]  (qualities: 20, 5)
  qSum = 25
  res = 150.0
```

**Interpretation:**
- Using worker 2 (ratio 6.0) as captain
- Group: worker 1 (quality 20, ratio 2.5) + worker 2 (quality 5, ratio 6.0)
- Both workers have ratio ≤ 6.0 ✅
- Cost: 6.0 × 25 = 150
- Worker 1 gets: 6.0 × 20 = 120 (≥ 50 ✅)
- Worker 2 gets: 6.0 × 5 = 30 (≥ 30 ✅)

### Step 5: Process Worker 0 (ratio = 7.0, quality = 10)

```
ratio = 7.0, q = 10

Add to heap:
  qSum += 10 → qSum = 35
  heapq.heappush(heap, -10) → heap = [-20, -5, -10]
  (After heapify, smallest negative = -20, which is largest quality)

Check size:
  len(heap) = 3 > K = 2
  Need to remove highest quality worker
  
  Remove highest quality:
    popped = heapq.heappop(heap) = -20
    (This is the smallest negative, which is largest quality)
    qSum += (-20) = qSum - 20 = 35 - 20 = 15
    heap = [-10, -5]  (qualities: 10, 5)

Check size:
  len(heap) = 2 == K ✅
  Calculate cost:
    cost = ratio × qSum = 7.0 × 15 = 105.0
    res = min(150.0, 105.0) = 105.0

State:
  heap = [-10, -5]  (qualities: 10, 5)
  qSum = 15
  res = 105.0
```

**Interpretation:**
- Using worker 0 (ratio 7.0) as captain
- Group: worker 0 (quality 10, ratio 7.0) + worker 2 (quality 5, ratio 6.0)
- Both workers have ratio ≤ 7.0 ✅
- Cost: 7.0 × 15 = 105
- Worker 0 gets: 7.0 × 10 = 70 (≥ 70 ✅)
- Worker 2 gets: 7.0 × 5 = 35 (≥ 30 ✅)

### Result

```
res = 105.0 ✅

Optimal group: Worker 0 + Worker 2
Cost: 105
```

---

## Detailed Example 2: Complex Case

**Input**: `quality = [3, 1, 10, 1, 1]`, `wage = [4, 8, 2, 2, 7]`, `K = 3`

### Step 1: Calculate Ratios

```
Worker 0: ratio = 4/3 ≈ 1.333, quality = 3
Worker 1: ratio = 8/1 = 8.0, quality = 1
Worker 2: ratio = 2/10 = 0.2, quality = 10
Worker 3: ratio = 2/1 = 2.0, quality = 1
Worker 4: ratio = 7/1 = 7.0, quality = 1

wq = [(0.2, 10), (1.333, 3), (2.0, 1), (7.0, 1), (8.0, 1)]
     (sorted by ratio)
```

### Step-by-Step Execution

#### Process Worker 2 (ratio = 0.2, quality = 10)

```
qSum = 10
heap = [-10]
len(heap) = 1 < K = 3
res = inf
```

#### Process Worker 0 (ratio = 1.333, quality = 3)

```
qSum = 10 + 3 = 13
heap = [-10, -3]
len(heap) = 2 < K = 3
res = inf
```

#### Process Worker 3 (ratio = 2.0, quality = 1)

```
qSum = 13 + 1 = 14
heap = [-10, -3, -1]
len(heap) = 3 == K ✅
cost = 2.0 × 14 = 28.0
res = min(inf, 28.0) = 28.0
```

**Group**: Workers 2, 0, 3 (qualities: 10, 3, 1, sum = 14)
- All have ratio ≤ 2.0 ✅
- Cost: 2.0 × 14 = 28

#### Process Worker 4 (ratio = 7.0, quality = 1)

```
qSum = 14 + 1 = 15
heap = [-10, -3, -1, -1]
len(heap) = 4 > K = 3

Remove highest quality:
  popped = heapq.heappop(heap) = -10
  qSum = 15 + (-10) = 15 - 10 = 5
  heap = [-3, -1, -1]  (qualities: 3, 1, 1)

len(heap) = 3 == K ✅
cost = 7.0 × 5 = 35.0
res = min(28.0, 35.0) = 28.0
```

**Group**: Workers 0, 3, 4 (qualities: 3, 1, 1, sum = 5)
- All have ratio ≤ 7.0 ✅
- Cost: 7.0 × 5 = 35

#### Process Worker 1 (ratio = 8.0, quality = 1)

```
qSum = 5 + 1 = 6
heap = [-3, -1, -1, -1]
len(heap) = 4 > K = 3

Remove highest quality:
  popped = heapq.heappop(heap) = -3
  qSum = 6 + (-3) = 6 - 3 = 3
  heap = [-1, -1, -1]  (qualities: 1, 1, 1)

len(heap) = 3 == K ✅
cost = 8.0 × 3 = 24.0
res = min(28.0, 24.0) = 24.0
```

**Group**: Workers 1, 3, 4 (qualities: 1, 1, 1, sum = 3)
- All have ratio ≤ 8.0 ✅
- Cost: 8.0 × 3 = 24

### Result

```
res = 24.0

Optimal group: Workers 1, 3, 4
Cost: 24
```

---

## Key Concepts

### 1. Wage-to-Quality Ratio

**Definition**: `ratio[i] = wage[i] / quality[i]`

**Meaning**: Minimum ratio needed to pay worker i their minimum wage

**Example:**
```
Worker: quality = 10, wage = 70
Ratio = 70/10 = 7.0
If we use ratio 7.0: payment = 7.0 × 10 = 70 ✅
If we use ratio < 7.0: payment < 70 ❌ (violates minimum wage)
```

### 2. Payment Constraint

**Rule**: If we use ratio `r`, worker i gets paid `r × quality[i]`

**Constraint**: `r × quality[i] ≥ wage[i]`

**This means**: `r ≥ wage[i] / quality[i] = ratio[i]`

**Implication**: If we use worker j as captain (ratio = `ratio[j]`), we can only include workers with `ratio[i] ≤ ratio[j]`

### 3. Cost Calculation

**Cost Formula**: `cost = captain_ratio × sum_of_all_K_qualities`

**To Minimize Cost**:
- For a given captain ratio, minimize `sum_of_qualities`
- This means selecting the K workers with lowest quality (among valid workers)

### 4. Why Sort by Ratio?

**Processing Order**:
- Sort workers by ratio (ascending)
- When processing worker j with ratio `r_j`:
  - All workers processed so far have `ratio ≤ r_j`
  - So all are valid candidates
  - We want the K with lowest quality

**Why This Works**:
- For each possible captain, we consider all valid workers
- We find the optimal group for that captain
- Return the minimum across all captains

### 5. Max-Heap with Negative Values

**Python's heapq is min-heap**:
- To simulate max-heap, we store negative values
- `heappush(heap, -quality)` stores `-quality`
- `heappop(heap)` returns the smallest negative = largest quality

**Example:**
```
Qualities: [10, 20, 5]
Store as: [-10, -20, -5]
Heap structure: [-20, -10, -5] (min-heap of negatives)
Smallest negative: -20 = largest quality: 20 ✅
```

### 6. Why Remove Highest Quality?

**When we have more than K workers**:
- We want to keep the K with lowest quality
- So we remove the one with highest quality
- This minimizes the sum of qualities

**Example:**
```
Have: qualities [10, 20, 5, 1], K = 3
Remove highest: 20
Keep: [10, 5, 1] (sum = 16) ✅
```

---

## Algorithm Pseudocode

```python
def mincostToHireWorkers(quality, wage, K):
    # Step 1: Calculate ratios and sort
    wq = sorted([(w/q, q) for w, q in zip(wage, quality)])
    
    # Step 2: Initialize
    res = inf
    heap = []
    qSum = 0
    
    # Step 3: Process each worker
    for ratio, q in wq:
        # Add current worker
        qSum += q
        heapq.heappush(heap, -q)
        
        # Remove highest quality if we exceed K
        if len(heap) > K:
            popped = heapq.heappop(heap)
            qSum += popped  # popped is negative, so this subtracts
        
        # Calculate cost if we have exactly K workers
        if len(heap) == K:
            cost = ratio * qSum
            res = min(res, cost)
    
    return res
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(N log N) | N = number of workers. Sort O(N log N), heap operations O(N log K) |
| **Space** | O(N) | Store ratios O(N), heap O(K) |

**Where:**
- N = number of workers
- K = number of workers to hire

**Time Complexity:**
- Sort: O(N log N)
- Heap operations: O(N log K) (each worker added/removed at most once)
- Total: O(N log N)

**Space Complexity:**
- Ratios array: O(N)
- Heap: O(K)
- Total: O(N)

---

## Edge Cases

### Case 1: K = 1
```
quality = [10], wage = [70], K = 1
Result: 70.0 ✅
```

### Case 2: K = N (All Workers)
```
quality = [10, 20], wage = [70, 50], K = 2
Result: max(ratio) × sum(qualities)
```

### Case 3: All Same Ratio
```
quality = [10, 20], wage = [50, 100], K = 2
Ratios: 5.0, 5.0
Result: 5.0 × 30 = 150.0
```

### Case 4: High Quality, Low Wage
```
Worker with very high quality but low wage
Has very low ratio
Can be included in many groups
```

---

## Why This Algorithm Works

### Correctness

1. **Considers All Possibilities:**
   - For each worker as captain, finds optimal group
   - Returns minimum across all possibilities

2. **Optimal Group Selection:**
   - For given captain, selects K workers with lowest quality
   - This minimizes cost for that captain

3. **Maintains Validity:**
   - Only considers workers with ratio ≤ captain's ratio
   - Ensures all workers get at least minimum wage

### Why Greedy Works

**Optimal Substructure:**
- For a given captain, the optimal group is the K workers with lowest quality
- This is independent of other captains
- Greedy selection (lowest quality) is optimal

### Why Sort by Ratio?

**Processing Order Matters:**
- When we process worker j, all previous workers have ratio ≤ ratio[j]
- So all are valid candidates
- We can form a valid group with any K of them
- We want the K with lowest quality

---

## Alternative Approaches

### 1. Brute Force

**Try all combinations:**
```python
def mincostToHireWorkers_bruteforce(quality, wage, K):
    from itertools import combinations
    min_cost = inf
    for group in combinations(range(len(quality)), K):
        # Try each worker as captain
        for captain in group:
            ratio = wage[captain] / quality[captain]
            # Check if all workers valid
            if all(wage[i] <= ratio * quality[i] for i in group):
                cost = ratio * sum(quality[i] for i in group)
                min_cost = min(min_cost, cost)
    return min_cost
```

**Time**: O(N^K × K), **Space**: O(K)

### 2. Dynamic Programming

**Could use DP, but greedy is more efficient:**
- State: (index, workers_selected)
- Transition: select or skip current worker
- Complexity: O(N × 2^N) - exponential

---

## Visual Timeline

### Example: `quality = [10, 20, 5]`, `wage = [70, 50, 30]`, `K = 2`

```
Step | Worker | Ratio | Quality | qSum | Heap      | Action
-----|--------|-------|---------|------|-----------|------------------
0    | -      | -     | -       | 0    | []        | Initialize
1    | 1      | 2.5   | 20      | 20   | [-20]     | Add worker 1
2    | 2      | 6.0   | 5       | 25   | [-20,-5]  | Add worker 2, cost=150
3    | 0      | 7.0   | 10      | 35   | [-20,-5,-10] | Add worker 0
     |        |       |         | 15   | [-10,-5]  | Remove 20, cost=105 ✅
```

---

## Real-World Applications

1. **Project Management:**
   - Hire team with minimum cost
   - Balance quality and wage requirements

2. **Resource Allocation:**
   - Select resources with cost constraints
   - Optimize team composition

3. **Budget Planning:**
   - Minimize hiring costs
   - Meet quality requirements

---

## Common Mistakes

### Mistake 1: Not Sorting by Ratio

```python
# WRONG: Process in original order
for i in range(len(quality)):
    ratio = wage[i] / quality[i]
    # Can't guarantee all previous workers are valid
```

**Fix:** Sort by ratio first

### Mistake 2: Wrong Heap Operation

```python
# WRONG: Not negating for max-heap
heapq.heappush(heap, q)  # Would get min-heap, not max-heap
```

**Fix:** Use `-q` to simulate max-heap

### Mistake 3: Wrong Sum Update

```python
# WRONG: Subtracting instead of adding negative
qSum -= heapq.heappop(heap)
```

**Fix:** `qSum += heapq.heappop(heap)` (popped value is already negative)

---

## Summary

The minimum cost to hire workers algorithm:
- Uses **greedy strategy** with sorting by ratio
- Uses **max-heap** to track highest quality workers
- For each worker as captain, finds **K workers with lowest quality**
- Calculates cost: `ratio × sum_of_qualities`
- Returns **minimum cost** across all captains
- Time complexity: **O(N log N)**
- Space complexity: **O(N)**

**Key Insight**: Sort workers by ratio. For each worker as captain, select the K workers (including captain) with lowest quality from all workers with ratio ≤ captain's ratio. This minimizes cost for that captain, and we return the minimum across all captains.

---

## Related Problems

- **LeetCode 857**: Minimum Cost to Hire K Workers (this problem)
- **LeetCode 253**: Meeting Rooms II (similar greedy with heap)
- **LeetCode 630**: Course Schedule III (greedy with priority queue)
- **LeetCode 502**: IPO (greedy with heap)

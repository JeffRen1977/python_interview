# Shortest Subarray with Sum at Least K

> **LeetCode 862**: Given an integer array `nums` and an integer `k`, return the length of the shortest non-empty subarray of `nums` with a sum of at least `k`. If there is no such subarray, return `-1`.

## Problem Description

Find the shortest contiguous subarray whose sum is at least `K`.

**Constraints:**
- Array can contain negative numbers
- Subarray must be contiguous
- Return the minimum length, or `-1` if no such subarray exists

**Example:**
- Input: `A = [2, -1, 2]`, `K = 3`
- Output: `3` (entire array: 2 + (-1) + 2 = 3)

---

## Key Insight

**Monotonic Deque Approach:**
- Use prefix sums to calculate subarray sums efficiently
- Use a deque to maintain candidate starting positions
- Maintain monotonicity: keep prefix sums in increasing order
- For each position, check if we can form a valid subarray

**Why Monotonic Deque?**
- If `prefix_sum[i] >= prefix_sum[j]` where `i < j`, then `prefix_sum[i]` is never useful
- For any future position `k`: `prefix_sum[k] - prefix_sum[j] >= prefix_sum[k] - prefix_sum[i]`
- And `k - j < k - i` (shorter subarray)
- So we can remove `prefix_sum[i]` from consideration

---

## Algorithm Logic

```
1. Initialize:
   - Deque q with (-1, 0) for prefix sum calculations
   - min_size = infinity
   - cumsum = 0

2. For each index j:
   a. Update cumsum += A[j]
   
   b. Check valid subarrays:
      While q exists and cumsum - q[0][1] >= K:
        - Update min_size = min(min_size, j - q[0][0])
        - Remove front element (no longer useful)
   
   c. Maintain monotonicity:
      While q exists and q[-1][1] >= cumsum:
        - Remove back element (never useful)
   
   d. Add (j, cumsum) to deque

3. Return min_size or -1
```

---

## Detailed Example 1: Step-by-Step

**Input**: `A = [2, -1, 2]`, `K = 3`

### Step-by-Step Execution

#### Step 1: Initialize

```
A = [2, -1, 2]
K = 3
q = deque([(-1, 0)])  # (index, prefix_sum)
min_size = inf
cumsum = 0
```

#### Step 2: Process Index 0

```
j = 0, A[0] = 2
cumsum = 0 + 2 = 2

Check valid subarrays:
  q[0] = (-1, 0)
  cumsum - q[0][1] = 2 - 0 = 2
  2 >= 3? NO ❌
  No valid subarray found

Maintain monotonicity:
  q[-1] = (-1, 0)
  q[-1][1] = 0
  0 >= 2? NO ❌
  No removal needed

Add to deque:
  q.append((0, 2))
  q = [(-1, 0), (0, 2)]
```

**After Index 0:**
```
q = [(-1, 0), (0, 2)]
min_size = inf
cumsum = 2
```

#### Step 3: Process Index 1

```
j = 1, A[1] = -1
cumsum = 2 + (-1) = 1

Check valid subarrays:
  q[0] = (-1, 0)
  cumsum - q[0][1] = 1 - 0 = 1
  1 >= 3? NO ❌
  No valid subarray

Maintain monotonicity:
  q[-1] = (0, 2)
  q[-1][1] = 2
  2 >= 1? YES ✅
  Remove (0, 2) because:
    - For any future j, cumsum_j - 1 >= cumsum_j - 2
    - Index 1 > 0, so shorter subarray
  q.pop() → q = [(-1, 0)]

Add to deque:
  q.append((1, 1))
  q = [(-1, 0), (1, 1)]
```

**After Index 1:**
```
q = [(-1, 0), (1, 1)]
min_size = inf
cumsum = 1
```

#### Step 4: Process Index 2

```
j = 2, A[2] = 2
cumsum = 1 + 2 = 3

Check valid subarrays:
  q[0] = (-1, 0)
  cumsum - q[0][1] = 3 - 0 = 3
  3 >= 3? YES ✅
    min_size = min(inf, 2 - (-1)) = min(inf, 3) = 3
    q.popleft() → q = [(1, 1)]
  
  Continue checking:
    q[0] = (1, 1)
    cumsum - q[0][1] = 3 - 1 = 2
    2 >= 3? NO ❌
    Stop

Maintain monotonicity:
  q[-1] = (1, 1)
  q[-1][1] = 1
  1 >= 3? NO ❌
  No removal needed

Add to deque:
  q.append((2, 3))
  q = [(1, 1), (2, 3)]
```

**After Index 2:**
```
q = [(1, 1), (2, 3)]
min_size = 3
cumsum = 3
```

#### Result

```
min_size = 3
Return: 3 ✅

Subarray: A[0:3] = [2, -1, 2], sum = 3
```

---

## Detailed Example 2: Complex Case

**Input**: `A = [84, -37, 32, 40, 95]`, `K = 167`

### Step-by-Step Execution

#### Step 1: Initialize

```
A = [84, -37, 32, 40, 95]
K = 167
q = [(-1, 0)]
min_size = inf
cumsum = 0
```

#### Step 2: Process Index 0

```
j = 0, A[0] = 84
cumsum = 0 + 84 = 84

Check valid: 84 - 0 = 84 < 167 ❌
Monotonicity: 0 >= 84? NO ❌
Add: q = [(-1, 0), (0, 84)]
```

#### Step 3: Process Index 1

```
j = 1, A[1] = -37
cumsum = 84 + (-37) = 47

Check valid: 47 - 0 = 47 < 167 ❌
Monotonicity: 84 >= 47? YES ✅
  Remove (0, 84) because:
    - 47 < 84 (smaller prefix sum)
    - Index 1 > 0 (later index)
    - (1, 47) is always better than (0, 84)
  q.pop() → q = [(-1, 0)]
Add: q = [(-1, 0), (1, 47)]
```

#### Step 4: Process Index 2

```
j = 2, A[2] = 32
cumsum = 47 + 32 = 79

Check valid: 79 - 0 = 79 < 167 ❌
Monotonicity: 47 >= 79? NO ❌
Add: q = [(-1, 0), (1, 47), (2, 79)]
```

#### Step 5: Process Index 3

```
j = 3, A[3] = 40
cumsum = 79 + 40 = 119

Check valid: 119 - 0 = 119 < 167 ❌
Monotonicity: 79 >= 119? NO ❌
Add: q = [(-1, 0), (1, 47), (2, 79), (3, 119)]
```

#### Step 6: Process Index 4

```
j = 4, A[4] = 95
cumsum = 119 + 95 = 214

Check valid subarrays:
  q[0] = (-1, 0)
  cumsum - q[0][1] = 214 - 0 = 214
  214 >= 167? YES ✅
    min_size = min(inf, 4 - (-1)) = 5
    q.popleft() → q = [(1, 47), (2, 79), (3, 119)]
  
  Continue:
    q[0] = (1, 47)
    cumsum - q[0][1] = 214 - 47 = 167
    167 >= 167? YES ✅
      min_size = min(5, 4 - 1) = min(5, 3) = 3
      q.popleft() → q = [(2, 79), (3, 119)]
  
  Continue:
    q[0] = (2, 79)
    cumsum - q[0][1] = 214 - 79 = 135
    135 >= 167? NO ❌
    Stop

Monotonicity: 119 >= 214? NO ❌
Add: q = [(2, 79), (3, 119), (4, 214)]
```

**Result**: `min_size = 3` ✅

**Subarray**: `A[1:4] = [-37, 32, 40]`, but wait, let me recalculate:
- Starting from index 1: sum = -37 + 32 + 40 + 95 = 130? No
- Actually: cumsum[4] - cumsum[1] = 214 - 47 = 167 ✅
- Subarray: A[2:5] = [32, 40, 95], sum = 167 ✅
- Length: 4 - 1 = 3 ✅

---

## Detailed Example 3: Why Monotonicity Matters

**Input**: `A = [1, -1, 6, -1, 2, 5]`, `K = 7`

### Without Monotonicity (Wrong Approach)

```
Index 0: cumsum = 1, q = [(-1, 0), (0, 1)]
Index 1: cumsum = 0, q = [(-1, 0), (0, 1), (1, 0)]  # Keeps both!
Index 2: cumsum = 6
  Check: 6 - 0 = 6 < 7 ❌
  Check: 6 - 1 = 5 < 7 ❌
  Check: 6 - 0 = 6 < 7 ❌
  (Would miss optimal solution)
```

### With Monotonicity (Correct Approach)

```
Index 0: cumsum = 1, q = [(-1, 0), (0, 1)]
Index 1: cumsum = 0
  Remove (0, 1) because 1 >= 0
  q = [(-1, 0), (1, 0)]
Index 2: cumsum = 6
  Check: 6 - 0 = 6 < 7 ❌
  q = [(-1, 0), (1, 0), (2, 6)]
Index 3: cumsum = 5
  Remove (2, 6) because 6 >= 5
  q = [(-1, 0), (1, 0), (3, 5)]
Index 4: cumsum = 7
  Check: 7 - 0 = 7 >= 7 ✅
    min_size = 4 - (-1) = 5
  Check: 7 - 0 = 7 >= 7 ✅
    min_size = min(5, 4 - 1) = 3
  q = [(3, 5)]
Index 5: cumsum = 12
  Check: 12 - 5 = 7 >= 7 ✅
    min_size = min(3, 5 - 3) = 2 ✅
```

**Result**: `2` ✅ (subarray [2, 5] starting from index 4)

---

## Key Concepts

### 1. Prefix Sums

**Definition**: `prefix_sum[i] = sum of A[0] to A[i]`

**Subarray Sum**: `sum(A[i:j+1]) = prefix_sum[j] - prefix_sum[i-1]`

**Example:**
```
A = [2, -1, 2]
prefix_sum = [2, 1, 3]
sum(A[0:3]) = prefix_sum[2] - prefix_sum[-1] = 3 - 0 = 3
```

### 2. Monotonic Deque

**Property**: Deque maintains prefix sums in increasing order

**Why?**
- If `prefix_sum[i] >= prefix_sum[j]` where `i < j`
- Then `prefix_sum[i]` is never useful:
  - For any future `k`: `prefix_sum[k] - prefix_sum[j] >= prefix_sum[k] - prefix_sum[i]`
  - And `k - j < k - i` (shorter subarray)
- So we remove `prefix_sum[i]`

### 3. Two-Pointer Logic

**Front Pointer (q[0]):**
- Check if `cumsum - q[0][1] >= K`
- If yes, we found a valid subarray
- Remove front (no longer useful for shorter subarrays)

**Back Pointer (q[-1]):**
- Maintain monotonicity
- Remove if `q[-1][1] >= cumsum`

### 4. Why Remove from Front?

**After finding valid subarray:**
- `cumsum - q[0][1] >= K`
- For any future `j > current_j`:
  - If `cumsum_j - q[0][1] >= K`, then `j - q[0][0] > current_j - q[0][0]`
  - So `q[0]` can never give us a shorter subarray
  - Safe to remove

### 5. Why Remove from Back?

**Monotonicity maintenance:**
- If `q[-1][1] >= cumsum`:
  - `q[-1]` has larger prefix sum and earlier index
  - Current position has smaller prefix sum and later index
  - Current is always better, so remove `q[-1]`

---

## Algorithm Pseudocode

```python
def shortestSubarray(A, K):
    q = deque([(-1, 0)])  # (index, prefix_sum)
    min_size = inf
    cumsum = 0
    
    for j in range(len(A)):
        cumsum += A[j]
        
        # Check valid subarrays from front
        while q and cumsum - q[0][1] >= K:
            min_size = min(min_size, j - q[0][0])
            q.popleft()
        
        # Maintain monotonicity from back
        while q and q[-1][1] >= cumsum:
            q.pop()
        
        q.append((j, cumsum))
    
    return -1 if min_size == inf else min_size
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(N) | Each element added/removed from deque at most once |
| **Space** | O(N) | Deque stores at most N elements |

**Where:**
- N = length of array

**Time Complexity:**
- Each element added to deque once: O(N)
- Each element removed from deque at most once: O(N)
- Total: O(N)

**Space Complexity:**
- Deque: O(N) in worst case
- Other variables: O(1)
- Total: O(N)

---

## Edge Cases

### Case 1: No Valid Subarray
```
A = [1, 2], K = 4
Result: -1 ✅
```

### Case 2: Single Element
```
A = [1], K = 1
Result: 1 ✅
```

### Case 3: Entire Array
```
A = [1, 2, 3, 4, 5], K = 15
Result: 5 ✅
```

### Case 4: Negative Numbers
```
A = [2, -1, 2], K = 3
Result: 3 ✅
```

### Case 5: All Negative
```
A = [-1, -2, -3], K = 1
Result: -1 ✅ (no valid subarray)
```

---

## Why This Algorithm Works

### Correctness

1. **Finds All Valid Subarrays:**
   - Checks every possible starting position
   - For each position, finds shortest valid subarray ending at current index

2. **Maintains Optimality:**
   - Monotonic deque ensures we only keep useful candidates
   - Removed elements can never give shorter subarrays

3. **Efficient:**
   - Each element processed once
   - Deque operations are amortized O(1)

### Why Monotonic Deque?

**Without monotonicity:**
- Would need to check all previous positions
- O(N²) time complexity

**With monotonicity:**
- Only check useful candidates
- O(N) time complexity

---

## Alternative Approaches

### 1. Brute Force

```python
def shortestSubarray_bruteforce(A, K):
    min_size = inf
    for i in range(len(A)):
        for j in range(i, len(A)):
            if sum(A[i:j+1]) >= K:
                min_size = min(min_size, j - i + 1)
    return -1 if min_size == inf else min_size
```

**Time**: O(N³), **Space**: O(1)

### 2. Prefix Sum + Brute Force

```python
def shortestSubarray_prefix(A, K):
    prefix = [0]
    for x in A:
        prefix.append(prefix[-1] + x)
    
    min_size = inf
    for i in range(len(A)):
        for j in range(i, len(A)):
            if prefix[j+1] - prefix[i] >= K:
                min_size = min(min_size, j - i + 1)
    return -1 if min_size == inf else min_size
```

**Time**: O(N²), **Space**: O(N)

### 3. Sliding Window (Doesn't Work with Negatives)

**Why it fails:**
- Sliding window assumes all positive numbers
- With negatives, we can't shrink window when sum >= K
- Need monotonic deque instead

---

## Visual Timeline

### Example: `A = [84, -37, 32, 40, 95]`, `K = 167`

```
Step | j | A[j] | cumsum | q State              | Action
-----|---|------|--------|----------------------|------------------
0    | - | -    | 0      | [(-1, 0)]            | Initialize
1    | 0 | 84   | 84     | [(-1, 0), (0, 84)]   | Add (0, 84)
2    | 1 | -37  | 47     | [(-1, 0), (1, 47)]   | Remove (0, 84), add (1, 47)
3    | 2 | 32   | 79     | [(-1, 0), (1, 47), (2, 79)] | Add (2, 79)
4    | 3 | 40   | 119    | [(-1, 0), (1, 47), (2, 79), (3, 119)] | Add (3, 119)
5    | 4 | 95   | 214    | [(2, 79), (3, 119), (4, 214)] | Found: min_size=3
```

**Result**: Length 3 (subarray from index 1 to 4: [32, 40, 95])

---

## Real-World Applications

1. **Stock Trading:**
   - Find shortest period with profit >= target
   - Portfolio analysis

2. **Network Analysis:**
   - Find shortest time window with traffic >= threshold
   - Bandwidth monitoring

3. **Data Analysis:**
   - Find shortest segment meeting criteria
   - Time series analysis

4. **Resource Management:**
   - Find shortest period with resource usage >= limit
   - Capacity planning

---

## Common Mistakes

### Mistake 1: Not Maintaining Monotonicity

```python
# WRONG: Doesn't remove larger prefix sums
while q and q[-1][1] >= cumsum:
    # Missing this check!
```

**Fix:** Always maintain monotonicity

### Mistake 2: Wrong Comparison

```python
# WRONG: Using > instead of >=
while q and cumsum - q[0][1] > K:
```

**Fix:** Use `>=` to include equal sums

### Mistake 3: Not Removing from Front

```python
# WRONG: Doesn't remove after finding valid subarray
if cumsum - q[0][1] >= K:
    min_size = min(min_size, j - q[0][0])
    # Missing: q.popleft()
```

**Fix:** Remove front element after processing

---

## Summary

The shortest subarray algorithm:
- Uses **monotonic deque** to maintain candidate starting positions
- Uses **prefix sums** to calculate subarray sums efficiently
- **Maintains monotonicity** by removing larger prefix sums
- **Removes from front** after finding valid subarrays
- Time complexity: **O(N)**
- Space complexity: **O(N)**

**Key Insight**: Maintain a deque with increasing prefix sums. If a prefix sum is larger than a later one, it's never useful and can be removed. This allows O(N) time instead of O(N²).

---

## Related Problems

- **LeetCode 862**: Shortest Subarray with Sum at Least K (this problem)
- **LeetCode 209**: Minimum Size Subarray Sum (all positive numbers, sliding window)
- **LeetCode 560**: Subarray Sum Equals K (count subarrays with sum K)
- **LeetCode 325**: Maximum Size Subarray Sum Equals k (similar concept)

# Split Array into Consecutive Subsequences

> **LeetCode 659**: Given an integer array `nums` that is sorted in ascending order, return `true` if and only if you can split it into one or more subsequences such that each subsequence consists of consecutive integers and has a length of at least 3.

## Problem Description

Determine if an array can be split into consecutive subsequences, each of length at least 3.

**Rules:**
- Each subsequence must consist of consecutive integers (e.g., [1, 2, 3])
- Each subsequence must have length ≥ 3
- Every element must be used exactly once
- Subsequences don't need to be contiguous in the original array

**Example:**
- Input: `[1, 2, 3, 3, 4, 5]`
- Output: `True` (can split into `[1, 2, 3]` and `[3, 4, 5]`)

---

## Key Insight

**Greedy Strategy with Min-Heap:**
- Track sequences ending at each number using min-heaps
- For each number `n`, always extend the shortest sequence ending at `n-1`
- Why shortest? To maximize chances of all sequences being ≥ 3
- If no sequence ends at `n-1`, start a new sequence

**Data Structure:**
- `heaps[n]` = min-heap of sequence lengths ending at number `n`
- Always extend shortest sequence (greedy choice)

**Why Min-Heap?**
- We want to extend the shortest sequence first
- This maximizes the chance that all sequences reach length ≥ 3
- If we extend longer sequences, shorter ones might remain < 3

---

## Algorithm Logic

```
1. Initialize heaps dictionary:
   - For each number in range [min-1, max], create empty heap
   - heaps[n] stores lengths of sequences ending at n

2. Process each number n in nums:
   a. If heaps[n-1] is not empty:
      - Pop shortest sequence length from heaps[n-1]
      - Extend it: length = popped_length + 1
   b. Else:
      - Start new sequence: length = 1
   c. Push length to heaps[n]

3. Check all heaps:
   - For each number in nums, check if shortest sequence >= 3
   - If any sequence has length < 3, return False
   - Otherwise, return True
```

---

## Detailed Example 1: Step-by-Step

**Input**: `nums = [1, 2, 3, 3, 4, 5]`

### Step 1: Initialize Heaps

```
nums = [1, 2, 3, 3, 4, 5]
min = 1, max = 5

Initialize heaps for range [0, 5]:
heaps = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}
```

### Step 2: Process Each Number

#### Process n = 1

```
n = 1

Check: heaps[0] (sequences ending at 0)
  heaps[0] = [] (empty)
  
No sequence ending at 0 → Start new sequence
  length = 1
  
Push to heaps[1]:
  heapq.heappush(heaps[1], 1)
  heaps[1] = [1]
```

**State:**
```
heaps = {
    0: [],
    1: [1],    ← Sequence of length 1 ending at 1
    2: [],
    3: [],
    4: [],
    5: []
}
```

#### Process n = 2

```
n = 2

Check: heaps[1] (sequences ending at 1)
  heaps[1] = [1] (not empty)
  
Extend sequence:
  popped = heapq.heappop(heaps[1]) = 1
  length = 1 + 1 = 2
  
Push to heaps[2]:
  heapq.heappush(heaps[2], 2)
  heaps[2] = [2]
```

**State:**
```
heaps = {
    0: [],
    1: [],
    2: [2],    ← Sequence of length 2 ending at 2
    3: [],
    4: [],
    5: []
}
```

#### Process n = 3 (First occurrence)

```
n = 3

Check: heaps[2] (sequences ending at 2)
  heaps[2] = [2] (not empty)
  
Extend sequence:
  popped = heapq.heappop(heaps[2]) = 2
  length = 2 + 1 = 3
  
Push to heaps[3]:
  heapq.heappush(heaps[3], 3)
  heaps[3] = [3]
```

**State:**
```
heaps = {
    0: [],
    1: [],
    2: [],
    3: [3],    ← Sequence of length 3 ending at 3 ✅
    4: [],
    5: []
}
```

#### Process n = 3 (Second occurrence)

```
n = 3

Check: heaps[2] (sequences ending at 2)
  heaps[2] = [] (empty)
  
No sequence ending at 2 → Start new sequence
  length = 1
  
Push to heaps[3]:
  heapq.heappush(heaps[3], 1)
  heaps[3] = [1, 3]  (min-heap: 1 is at root)
```

**State:**
```
heaps = {
    0: [],
    1: [],
    2: [],
    3: [1, 3],  ← Two sequences: length 1 and 3
    4: [],
    5: []
}
```

#### Process n = 4

```
n = 4

Check: heaps[3] (sequences ending at 3)
  heaps[3] = [1, 3] (not empty)
  
Extend shortest sequence (greedy choice):
  popped = heapq.heappop(heaps[3]) = 1  (shortest!)
  length = 1 + 1 = 2
  
Push to heaps[4]:
  heapq.heappush(heaps[4], 2)
  heaps[4] = [2]
```

**State:**
```
heaps = {
    0: [],
    1: [],
    2: [],
    3: [3],     ← One sequence of length 3
    4: [2],     ← One sequence of length 2
    5: []
}
```

#### Process n = 5

```
n = 5

Check: heaps[4] (sequences ending at 4)
  heaps[4] = [2] (not empty)
  
Extend sequence:
  popped = heapq.heappop(heaps[4]) = 2
  length = 2 + 1 = 3
  
Push to heaps[5]:
  heapq.heappush(heaps[5], 3)
  heaps[5] = [3]
```

**State:**
```
heaps = {
    0: [],
    1: [],
    2: [],
    3: [3],     ← Sequence of length 3 ✅
    4: [],
    5: [3]      ← Sequence of length 3 ✅
}
```

### Step 3: Check All Sequences

```
Check heaps for numbers in nums:
  heaps[1]: [] → empty (no sequences)
  heaps[2]: [] → empty
  heaps[3]: [3] → 3 >= 3 ✅
  heaps[4]: [] → empty
  heaps[5]: [3] → 3 >= 3 ✅

All sequences have length >= 3 ✅
Return True
```

**Result**: `True` ✅

**Subsequences:**
- `[1, 2, 3]` (length 3) - uses first 3
- `[3, 4, 5]` (length 3) - uses second 3

---

## Detailed Example 2: Impossible Case

**Input**: `nums = [1, 2, 3, 4, 4, 5, 6]`

### Step-by-Step Execution

#### Initialize

```
heaps = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
```

#### Process Numbers

**n = 1:**
```
heaps[0] = [] → Start new: length = 1
heaps[1] = [1]
```

**n = 2:**
```
heaps[1] = [1] → Extend: length = 2
heaps[2] = [2]
```

**n = 3:**
```
heaps[2] = [2] → Extend: length = 3
heaps[3] = [3]
```

**n = 4 (First):**
```
heaps[3] = [3] → Extend: length = 4
heaps[4] = [4]
```

**n = 4 (Second):**
```
heaps[3] = [] → Start new: length = 1
heaps[4] = [1, 4]  (min-heap: 1 is shortest)
```

**n = 5:**
```
heaps[4] = [1, 4] → Extend shortest: length = 2
heaps[5] = [2]
```

**n = 6:**
```
heaps[5] = [2] → Extend: length = 3
heaps[6] = [3]
```

#### Final State

```
heaps = {
    1: [],
    2: [],
    3: [],
    4: [4],    ← Sequence of length 4 ✅
    5: [],
    6: [3]     ← Sequence of length 3 ✅
}
```

#### Check All Sequences

```
Check heaps for numbers in nums:
  heaps[1]: [] → empty
  heaps[2]: [] → empty
  heaps[3]: [] → empty
  heaps[4]: [4] → 4 >= 3 ✅
  heaps[5]: [] → empty
  heaps[6]: [3] → 3 >= 3 ✅

All sequences have length >= 3
Return True
```

**Note**: This example returns `True` based on the algorithm, but the expected output in the code is `False`. This might indicate a different problem interpretation or a test case issue.

---

## Detailed Example 3: Simple Valid Case

**Input**: `nums = [1, 2, 3, 4, 5, 6]`

### Step-by-Step Execution

#### Process Numbers

**n = 1:**
```
heaps[0] = [] → Start new: length = 1
heaps[1] = [1]
```

**n = 2:**
```
heaps[1] = [1] → Extend: length = 2
heaps[2] = [2]
```

**n = 3:**
```
heaps[2] = [2] → Extend: length = 3
heaps[3] = [3]
```

**n = 4:**
```
heaps[3] = [3] → Extend: length = 4
heaps[4] = [4]
```

**n = 5:**
```
heaps[4] = [4] → Extend: length = 5
heaps[5] = [5]
```

**n = 6:**
```
heaps[5] = [5] → Extend: length = 6
heaps[6] = [6]
```

#### Final State

```
heaps = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [6]     ← One sequence of length 6 ✅
}
```

**Result**: `True` ✅

**Subsequence**: `[1, 2, 3, 4, 5, 6]` (length 6)

---

## Example 4: Why Extend Shortest?

**Input**: `nums = [1, 2, 3, 4, 5, 5, 6, 7]`

### If We Extend Longest (Wrong)

```
After processing [1,2,3,4,5]:
  Sequence: [1,2,3,4,5] (length 5) ending at 5

Process second 5:
  Extend longest: [1,2,3,4,5,5] (length 6)
  Start new: [5] (length 1)

Process 6:
  Extend longest: [1,2,3,4,5,5,6] (length 7)
  (Short sequence [5] remains length 1)

Process 7:
  Extend longest: [1,2,3,4,5,5,6,7] (length 8)
  (Short sequence [5] remains length 1) ❌
  
Result: False (sequence [5] has length 1 < 3)
```

### If We Extend Shortest (Correct)

```
After processing [1,2,3,4,5]:
  Sequence: [1,2,3,4,5] (length 5) ending at 5

Process second 5:
  Extend shortest: Can't, no shorter sequence
  Start new: [5] (length 1)

Process 6:
  Extend shortest [5]: [5,6] (length 2)
  Keep [1,2,3,4,5] (length 5)

Process 7:
  Extend shortest [5,6]: [5,6,7] (length 3) ✅
  Keep [1,2,3,4,5] (length 5) ✅
  
Result: True (both sequences >= 3)
```

**Key**: Always extend the shortest sequence to maximize chances of all sequences reaching length ≥ 3.

---

## Key Concepts

### 1. Greedy Choice: Extend Shortest

**Why always extend shortest?**
- Goal: All sequences must have length ≥ 3
- If we extend a longer sequence, shorter ones might remain < 3
- By extending shortest first, we maximize chances of all reaching ≥ 3

**Example:**
```
Have: sequences of length [1, 5]
Next number: 6

Option 1: Extend length 5 → [1, 6] (still < 3) ❌
Option 2: Extend length 1 → [2, 6] (closer to 3) ✅
```

### 2. Min-Heap for Sequence Lengths

**Why min-heap?**
- We want to quickly find the shortest sequence
- Min-heap gives us the minimum length in O(1) (root)
- Pop and push are O(log n)

**Structure:**
```
heaps[n] = [length1, length2, ...]  (min-heap)
heaps[n][0] = shortest sequence ending at n
```

### 3. Sequence Tracking

**What does `heaps[n]` represent?**
- All sequences ending at number `n`
- Each value is the length of a sequence
- Multiple sequences can end at the same number

**Example:**
```
heaps[3] = [1, 3]
Means: Two sequences end at 3
  - One of length 1: [3]
  - One of length 3: [1, 2, 3]
```

### 4. Extending Sequences

**When we see number `n`:**
- Check if any sequence ends at `n-1`
- If yes: extend the shortest one (greedy)
- If no: start a new sequence of length 1

**Why check `n-1`?**
- To form consecutive sequences: [..., n-1, n]
- If a sequence ends at `n-1`, we can extend it to `n`

### 5. Final Validation

**Check all sequences:**
- After processing all numbers, check if all sequences have length ≥ 3
- If any sequence has length < 3, return False
- Otherwise, return True

**Why check minimum?**
- If shortest sequence >= 3, then all sequences >= 3
- So we only need to check `heaps[n][0] >= 3`

---

## Algorithm Pseudocode

```python
def isPossible(nums):
    # Step 1: Initialize heaps
    heaps = {}
    for n in range(nums[0] - 1, nums[-1] + 1):
        heaps[n] = []
    
    # Step 2: Process each number
    for n in nums:
        if heaps[n - 1]:
            # Extend shortest sequence ending at n-1
            length = heapq.heappop(heaps[n - 1]) + 1
        else:
            # Start new sequence
            length = 1
        heapq.heappush(heaps[n], length)
    
    # Step 3: Validate all sequences
    for n in nums:
        if heaps[n] and heaps[n][0] < 3:
            return False
    return True
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(N log N) | N = array length. Sort not needed (already sorted), heap operations O(N log M) where M = max sequences per number |
| **Space** | O(N) | Heaps store at most N sequence lengths |

**Where:**
- N = length of array
- M = maximum number of sequences ending at a single number

**Time Complexity:**
- Initialize heaps: O(R) where R = range of numbers
- Process each number: O(log M) for heap operations
- Check sequences: O(N)
- Total: O(N log M) where M ≤ N in worst case

**Space Complexity:**
- Heaps: O(N) in worst case (each number starts a sequence)
- Total: O(N)

---

## Edge Cases

### Case 1: All Consecutive
```
nums = [1, 2, 3, 4, 5]
Result: True ✅ (one sequence of length 5)
```

### Case 2: Multiple Duplicates
```
nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]
Result: True ✅ (three sequences of length 3)
```

### Case 3: Too Short
```
nums = [1, 2]
Result: False ✅ (can't form sequence of length >= 3)
```

### Case 4: Single Number Repeated
```
nums = [1, 1, 1]
Result: True ✅ (one sequence [1, 1, 1], but wait...)
```

Actually, [1, 1, 1] is not consecutive! Consecutive means [1, 2, 3], not [1, 1, 1].

So this should return False. But the algorithm might return True if it doesn't check for consecutiveness properly. However, since the array is sorted and we only extend sequences ending at n-1, we should only form consecutive sequences.

Let me reconsider: if we have [1, 1, 1]:
- First 1: start sequence [1]
- Second 1: heaps[0] is empty, start new [1]
- Third 1: heaps[0] is empty, start new [1]
- Final: heaps[1] = [1, 1, 1] (three sequences of length 1)
- Check: 1 < 3 → False ✅

So it correctly returns False.

---

## Why This Algorithm Works

### Correctness

1. **Greedy Choice is Optimal:**
   - Always extending shortest sequence maximizes chances
   - If we can form valid sequences, greedy will find them
   - If greedy fails, no solution exists

2. **Tracks All Possibilities:**
   - For each number, considers all sequences ending at n-1
   - Extends the one that needs it most (shortest)
   - Ensures no valid solution is missed

3. **Validates Correctly:**
   - After processing, checks if all sequences >= 3
   - If any sequence < 3, returns False
   - Otherwise, returns True

### Why Greedy Works

**Optimal Substructure:**
- If we can form valid sequences, the greedy choice (extend shortest) is optimal
- Extending shortest first doesn't prevent other sequences from being valid
- In fact, it maximizes the chance of all sequences being valid

**Greedy Choice Property:**
- At each step, extending the shortest sequence is the best choice
- This choice doesn't affect future optimality
- Leads to globally optimal solution

---

## Alternative Approaches

### 1. Dynamic Programming

**Idea**: Track state of sequences

**Complexity**: O(N²) or worse
**More complex**: Harder to implement

### 2. Two-Pass Greedy

**Idea**: First pass to identify sequences, second to validate

**Similar complexity**: O(N log N)
**More complex**: Two passes needed

---

## Visual Timeline

### Example: `nums = [1, 2, 3, 3, 4, 5]`

```
Step | n | heaps[n-1] | Action              | heaps[n] After
-----|---|------------|---------------------|------------------
1    | 1 | []         | Start new: length=1 | [1]
2    | 2 | [1]        | Extend: length=2    | [2]
3    | 3 | [2]        | Extend: length=3    | [3]
4    | 3 | []         | Start new: length=1 | [1,3]
5    | 4 | [1,3]      | Extend shortest: 2   | [2]
6    | 5 | [2]        | Extend: length=3    | [3]

Final check: All sequences >= 3 ✅
```

---

## Real-World Applications

1. **Data Streaming:**
   - Identify consecutive sequences in data streams
   - Pattern recognition

2. **Time Series Analysis:**
   - Find consecutive time periods
   - Event sequence detection

3. **Game Development:**
   - Validate move sequences
   - Pattern matching

---

## Common Mistakes

### Mistake 1: Not Using Min-Heap

```python
# WRONG: Extends arbitrary sequence
if heaps[n - 1]:
    length = heaps[n - 1][0] + 1  # Might not be shortest
```

**Fix:** Use `heappop` to get shortest

### Mistake 2: Not Checking All Sequences

```python
# WRONG: Only checks last heap
if heaps[nums[-1]][0] < 3:
    return False
```

**Fix:** Check all heaps for numbers in nums

### Mistake 3: Wrong Heap Operation

```python
# WRONG: Using list instead of heap
heaps[n - 1].pop(0)  # O(N) operation
```

**Fix:** Use `heappop` for O(log N)

---

## Summary

The split into consecutive subsequences algorithm:
- Uses **greedy strategy** with min-heap
- **Always extends shortest sequence** ending at n-1
- Tracks sequences using **heaps indexed by ending number**
- Validates that **all sequences have length >= 3**
- Time complexity: **O(N log N)**
- Space complexity: **O(N)**

**Key Insight**: Always extend the shortest sequence ending at n-1. This greedy choice maximizes the chance that all sequences reach length ≥ 3, leading to an optimal solution.

---

## Related Problems

- **LeetCode 659**: Split Array into Consecutive Subsequences (this problem)
- **LeetCode 846**: Hand of Straights (similar consecutive grouping)
- **LeetCode 1296**: Divide Array in Sets of K Consecutive Numbers (similar concept)

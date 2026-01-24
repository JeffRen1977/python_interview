# Coin Change

> **LeetCode 322**: You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

## Problem Description

Find the minimum number of coins needed to make a given amount.

**Example:**
- `coins = [1, 2, 5]`, `amount = 11`
- Answer: `3` (5 + 5 + 1 = 11)

---

## Key Insight

Use **Dynamic Programming**:
- `dp[i]` = minimum number of coins needed to make amount `i`
- For each coin, try using it: `dp[i] = min(dp[i], dp[i - coin] + 1)`
- Build solution bottom-up from smaller amounts

**Strategy**: For each amount, try all coins and take the minimum.

---

## Algorithm Logic

```
1. Initialize:
   - dp[0..amount] = infinity (impossible initially)
   - dp[0] = 0 (0 coins needed for amount 0)

2. For each coin:
   For each amount i from 1 to amount:
     If i >= coin:
       dp[i] = min(dp[i], dp[i - coin] + 1)

3. Return:
   - dp[amount] if it's not infinity
   - -1 otherwise
```

---

## Detailed Example: Step-by-Step

**Input**: `coins = [1, 2, 5]`, `amount = 11`

### Initial Setup

```
coins = [1, 2, 5]
amount = 11

dp = [∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞, ∞]
      0   1   2   3   4   5   6   7   8   9  10  11

Base case:
dp[0] = 0  (0 coins needed for amount 0)
```

### Processing Coin 1

**Coin = 1**

| Amount i | i >= 1? | dp[i-1] | dp[i] = min(dp[i], dp[i-1] + 1) | dp Array |
|----------|---------|---------|----------------------------------|----------|
| 1 | Yes | dp[0]=0 | min(∞, 0+1) = 1 | `[0, 1, ∞, ∞, ...]` |
| 2 | Yes | dp[1]=1 | min(∞, 1+1) = 2 | `[0, 1, 2, ∞, ...]` |
| 3 | Yes | dp[2]=2 | min(∞, 2+1) = 3 | `[0, 1, 2, 3, ...]` |
| 4 | Yes | dp[3]=3 | min(∞, 3+1) = 4 | `[0, 1, 2, 3, 4, ...]` |
| 5 | Yes | dp[4]=4 | min(∞, 4+1) = 5 | `[0, 1, 2, 3, 4, 5, ...]` |
| 6 | Yes | dp[5]=5 | min(∞, 5+1) = 6 | `[0, 1, 2, 3, 4, 5, 6, ...]` |
| 7 | Yes | dp[6]=6 | min(∞, 6+1) = 7 | `[0, 1, 2, 3, 4, 5, 6, 7, ...]` |
| 8 | Yes | dp[7]=7 | min(∞, 7+1) = 8 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, ...]` |
| 9 | Yes | dp[8]=8 | min(∞, 8+1) = 9 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...]` |
| 10 | Yes | dp[9]=9 | min(∞, 9+1) = 10 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]` |
| 11 | Yes | dp[10]=10 | min(∞, 10+1) = 11 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` |

**After processing coin 1:**
```
dp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
      ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑   ↑
      0  1  2  3  4  5  6  7  8  9  10  11

Interpretation: Using only coin 1, we need i coins to make amount i
```

### Processing Coin 2

**Coin = 2**

| Amount i | i >= 2? | dp[i-2] | dp[i] = min(dp[i], dp[i-2] + 1) | dp Array |
|----------|---------|---------|----------------------------------|----------|
| 1 | No | — | No update | `[0, 1, 2, 3, ...]` |
| 2 | Yes | dp[0]=0 | min(2, 0+1) = 1 | `[0, 1, 1, 3, ...]` ✅ |
| 3 | Yes | dp[1]=1 | min(3, 1+1) = 2 | `[0, 1, 1, 2, ...]` ✅ |
| 4 | Yes | dp[2]=1 | min(4, 1+1) = 2 | `[0, 1, 1, 2, 2, ...]` ✅ |
| 5 | Yes | dp[3]=2 | min(5, 2+1) = 3 | `[0, 1, 1, 2, 2, 3, ...]` ✅ |
| 6 | Yes | dp[4]=2 | min(6, 2+1) = 3 | `[0, 1, 1, 2, 2, 3, 3, ...]` ✅ |
| 7 | Yes | dp[5]=3 | min(7, 3+1) = 4 | `[0, 1, 1, 2, 2, 3, 3, 4, ...]` ✅ |
| 8 | Yes | dp[6]=3 | min(8, 3+1) = 4 | `[0, 1, 1, 2, 2, 3, 3, 4, 4, ...]` ✅ |
| 9 | Yes | dp[7]=4 | min(9, 4+1) = 5 | `[0, 1, 1, 2, 2, 3, 3, 4, 4, 5, ...]` ✅ |
| 10 | Yes | dp[8]=4 | min(10, 4+1) = 5 | `[0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, ...]` ✅ |
| 11 | Yes | dp[9]=5 | min(11, 5+1) = 6 | `[0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]` ✅ |

**After processing coin 2:**
```
dp = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
      ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑   ↑
      0  1  2  3  4  5  6  7  8  9  10  11

Improvements:
- Amount 2: 2 coins → 1 coin (using coin 2)
- Amount 4: 4 coins → 2 coins (2+2)
- Amount 6: 6 coins → 3 coins (2+2+2)
- etc.
```

### Processing Coin 5

**Coin = 5**

| Amount i | i >= 5? | dp[i-5] | dp[i] = min(dp[i], dp[i-5] + 1) | dp Array |
|----------|---------|---------|----------------------------------|----------|
| 1-4 | No | — | No update | No change |
| 5 | Yes | dp[0]=0 | min(3, 0+1) = 1 | `[0, 1, 1, 2, 2, 1, 3, ...]` ✅ |
| 6 | Yes | dp[1]=1 | min(3, 1+1) = 2 | `[0, 1, 1, 2, 2, 1, 2, ...]` ✅ |
| 7 | Yes | dp[2]=1 | min(4, 1+1) = 2 | `[0, 1, 1, 2, 2, 1, 2, 2, ...]` ✅ |
| 8 | Yes | dp[3]=2 | min(4, 2+1) = 3 | `[0, 1, 1, 2, 2, 1, 2, 2, 3, ...]` ✅ |
| 9 | Yes | dp[4]=2 | min(5, 2+1) = 3 | `[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, ...]` ✅ |
| 10 | Yes | dp[5]=1 | min(5, 1+1) = 2 | `[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, ...]` ✅ |
| 11 | Yes | dp[6]=2 | min(6, 2+1) = 3 | `[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]` ✅ |

**After processing coin 5:**
```
dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
      ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑   ↑
      0  1  2  3  4  5  6  7  8  9  10  11

Final result: dp[11] = 3
Optimal solution: 5 + 5 + 1 = 11 (3 coins)
```

---

## Detailed Step Breakdown

### Initialization

```
coins = [1, 2, 5]
amount = 11

dp = [maxsize, maxsize, maxsize, ..., maxsize]  (12 elements, indices 0-11)
     [0,       1,       2,       ..., 11]

Base case:
dp[0] = 0  (0 coins needed to make amount 0)
```

**Why dp[0] = 0?**
- To make amount 0, we need 0 coins (base case)
- This allows us to build up solutions for larger amounts

### Processing Coin 1: Building Base Solutions

**For amount 1:**
```
i = 1, coin = 1
i >= coin? Yes (1 >= 1)
dp[1] = min(dp[1], dp[1-1] + 1)
       = min(∞, dp[0] + 1)
       = min(∞, 0 + 1)
       = 1

Meaning: To make amount 1, we need 1 coin (coin 1)
```

**For amount 2:**
```
i = 2, coin = 1
i >= coin? Yes (2 >= 1)
dp[2] = min(dp[2], dp[2-1] + 1)
       = min(∞, dp[1] + 1)
       = min(∞, 1 + 1)
       = 2

Meaning: To make amount 2, we need 2 coins (coin 1 + coin 1)
```

**Pattern**: After processing coin 1, `dp[i] = i` (using only coin 1, we need i coins for amount i)

### Processing Coin 2: Finding Better Solutions

**For amount 2:**
```
i = 2, coin = 2
i >= coin? Yes (2 >= 2)
dp[2] = min(dp[2], dp[2-2] + 1)
       = min(2, dp[0] + 1)
       = min(2, 0 + 1)
       = 1  ← IMPROVEMENT!

Meaning: To make amount 2, we can use 1 coin (coin 2) instead of 2 coins
```

**For amount 4:**
```
i = 4, coin = 2
i >= coin? Yes (4 >= 2)
dp[4] = min(dp[4], dp[4-2] + 1)
       = min(4, dp[2] + 1)
       = min(4, 1 + 1)
       = 2  ← IMPROVEMENT!

Meaning: To make amount 4, we can use 2 coins (2+2) instead of 4 coins
```

**For amount 3:**
```
i = 3, coin = 2
i >= coin? Yes (3 >= 2)
dp[3] = min(dp[3], dp[3-2] + 1)
       = min(3, dp[1] + 1)
       = min(3, 1 + 1)
       = 2  ← IMPROVEMENT!

Meaning: To make amount 3, we can use 2 coins (2+1) instead of 3 coins
```

### Processing Coin 5: Final Optimizations

**For amount 5:**
```
i = 5, coin = 5
i >= coin? Yes (5 >= 5)
dp[5] = min(dp[5], dp[5-5] + 1)
       = min(3, dp[0] + 1)
       = min(3, 0 + 1)
       = 1  ← IMPROVEMENT!

Meaning: To make amount 5, we can use 1 coin (coin 5) instead of 3 coins
```

**For amount 10:**
```
i = 10, coin = 5
i >= coin? Yes (10 >= 5)
dp[10] = min(dp[10], dp[10-5] + 1)
        = min(5, dp[5] + 1)
        = min(5, 1 + 1)
        = 2  ← IMPROVEMENT!

Meaning: To make amount 10, we can use 2 coins (5+5) instead of 5 coins
```

**For amount 11:**
```
i = 11, coin = 5
i >= coin? Yes (11 >= 5)
dp[11] = min(dp[11], dp[11-5] + 1)
        = min(6, dp[6] + 1)
        = min(6, 2 + 1)
        = 3  ← IMPROVEMENT!

Meaning: To make amount 11, we can use 3 coins (5+5+1) instead of 6 coins
```

### Final Result

```
dp[11] = 3

Optimal solution: Use coins [5, 5, 1] to make amount 11
Total coins: 3
```

---

## Key Concepts

### 1. Dynamic Programming State

**`dp[i]`** = minimum number of coins needed to make amount `i`

**State Transition:**
- To make amount `i` using coin `c`:
  - We need `dp[i - c]` coins to make amount `(i - c)`
  - Plus 1 coin (the coin `c` itself)
  - So: `dp[i] = min(dp[i], dp[i - c] + 1)`

### 2. Why Process Coins in Any Order?

The algorithm processes coins one by one, but the order doesn't matter because:
- We try all coins for each amount
- We always take the minimum
- The DP table accumulates the best solution

**However**, processing smaller coins first can be more intuitive for understanding.

### 3. Why Check `i >= coin`?

We can only use a coin if the amount is at least as large as the coin value:
- Can't use coin 5 to make amount 3
- Can use coin 2 to make amount 3 (3 - 2 = 1, then use coin 1)

### 4. Why Initialize with `maxsize`?

We initialize with a large number (`maxsize`) to represent "impossible":
- If `dp[amount]` remains `maxsize`, we can't make that amount
- When comparing, `min(∞, x)` always chooses `x` if `x` is valid

---

## Visual DP Table Evolution

```
Initial:
Amount:  0  1  2  3  4  5  6  7  8  9  10 11
dp:      0  ∞  ∞  ∞  ∞  ∞  ∞  ∞  ∞  ∞  ∞  ∞

After coin 1:
Amount:  0  1  2  3  4  5  6  7  8  9  10 11
dp:      0  1  2  3  4  5  6  7  8  9  10 11

After coin 2:
Amount:  0  1  2  3  4  5  6  7  8  9  10 11
dp:      0  1  1  2  2  3  3  4  4  5  5  6
         ↑     ↑  ↑  ↑     ↑  ↑  ↑  ↑  ↑  ↑
         base  improved values

After coin 5:
Amount:  0  1  2  3  4  5  6  7  8  9  10 11
dp:      0  1  1  2  2  1  2  2  3  3  2  3
                     ↑     ↑  ↑  ↑  ↑     ↑
                     improved values
```

---

## Algorithm Pseudocode

```python
def coinChange(coins, amount):
    # Initialize DP table
    dp = [infinity] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins for amount 0
    
    # For each coin
    for coin in coins:
        # For each amount from 1 to amount
        for i in range(1, amount + 1):
            # If we can use this coin
            if i >= coin:
                # Try using this coin
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result
    if dp[amount] == infinity:
        return -1  # Cannot make amount
    else:
        return dp[amount]
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(n × amount) | n = number of coins. For each coin, iterate through all amounts |
| **Space** | O(amount) | DP table of size (amount + 1) |

---

## Edge Cases

### Case 1: Cannot Make Amount
```
coins = [2], amount = 3
Result: -1

DP table:
Amount:  0  1  2  3
dp:      0  ∞  ∞  ∞

After processing coin 2:
Amount:  0  1  2  3
dp:      0  ∞  1  ∞

dp[3] = ∞ → return -1
```

### Case 2: Amount is 0
```
coins = [1, 2, 5], amount = 0
Result: 0

dp[0] = 0 (base case)
```

### Case 3: Single Coin
```
coins = [1], amount = 2
Result: 2

After processing coin 1:
Amount:  0  1  2
dp:      0  1  2
```

### Case 4: Optimal Uses Multiple Coins
```
coins = [1, 3, 4], amount = 6
Result: 2 (3 + 3, not 4 + 1 + 1)

Step-by-step:
- After coin 1: dp = [0, 1, 2, 3, 4, 5, 6]
- After coin 3: dp = [0, 1, 2, 1, 2, 3, 2]  (improved at 3, 6)
- After coin 4: dp = [0, 1, 2, 1, 1, 2, 2]  (improved at 4, 5)
- Final: dp[6] = 2
```

---

## Why This Algorithm Works

### Optimal Substructure

The problem has optimal substructure:
- If we know the minimum coins for amount `(i - coin)`, we can get minimum for amount `i` by adding 1 coin
- `dp[i] = min over all coins: dp[i - coin] + 1`

### Greedy Choice Property

**Note**: This is NOT a greedy algorithm! Greedy would choose the largest coin first, which doesn't always work.

**Example where greedy fails:**
```
coins = [1, 3, 4], amount = 6
Greedy: 4 + 1 + 1 = 3 coins
Optimal: 3 + 3 = 2 coins
```

DP considers all possibilities and chooses the minimum.

### Correctness Proof

**Invariant**: After processing coins up to coin `c`, `dp[i]` contains the minimum coins needed to make amount `i` using coins `[c1, c2, ..., c]`.

**Base case**: After processing no coins, only `dp[0] = 0` is valid.

**Inductive step**: When processing coin `c`:
- For each amount `i >= c`, we consider using coin `c`
- `dp[i] = min(dp[i], dp[i-c] + 1)` ensures we get the minimum
- Invariant maintained ✓

---

## Alternative Approaches

### Approach 1: Recursion with Memoization
```python
def coinChange_memo(coins, amount, memo={}):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if amount in memo:
        return memo[amount]
    
    min_coins = float('inf')
    for coin in coins:
        result = coinChange_memo(coins, amount - coin, memo)
        if result != -1:
            min_coins = min(min_coins, result + 1)
    
    memo[amount] = -1 if min_coins == float('inf') else min_coins
    return memo[amount]
```
**Time**: O(n × amount), **Space**: O(amount) for memoization

### Approach 2: BFS (Breadth-First Search)
```python
def coinChange_bfs(coins, amount):
    from collections import deque
    queue = deque([(0, 0)])  # (current_amount, coins_used)
    visited = set([0])
    
    while queue:
        curr_amount, coins_used = queue.popleft()
        if curr_amount == amount:
            return coins_used
        
        for coin in coins:
            next_amount = curr_amount + coin
            if next_amount <= amount and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, coins_used + 1))
    
    return -1
```
**Time**: O(amount × n), **Space**: O(amount)

---

## Summary

The coin change algorithm:
- Uses **dynamic programming** with bottom-up approach
- `dp[i]` = minimum coins needed for amount `i`
- For each coin, update all amounts that can use it
- Time complexity: **O(n × amount)**
- Space complexity: **O(amount)**

**Key Insight**: To make amount `i` using coin `c`, we need `dp[i-c]` coins plus 1. Try all coins and take the minimum.

---

## Related Problems

- **LeetCode 518**: Coin Change 2 (count number of ways)
- **LeetCode 279**: Perfect Squares (similar DP structure)
- **LeetCode 377**: Combination Sum IV
- **LeetCode 416**: Partition Equal Subset Sum

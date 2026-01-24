# Best Time to Buy and Sell Stock

> **LeetCode 121**: You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction.

## Problem Description

Find the maximum profit from buying and selling a stock once (one transaction).

**Constraints:**
- You can only buy once and sell once
- You must buy before you sell
- If no profit is possible, return 0

**Example:**
- `prices = [7, 1, 5, 3, 6, 4]`
- Answer: `5` (buy at 1, sell at 6)

---

## Key Insight

Use a **greedy approach**:
- Track the **minimum price seen so far** (best buy price)
- For each day, calculate profit if we sell today (price - min_price)
- Keep track of the **maximum profit** seen so far

**Strategy**: As we iterate, we always know the best buy price up to now, so we can calculate the best profit if we sell today.

---

## Algorithm Logic

```
1. Initialize:
   - min_price = infinity (no price seen yet)
   - profit = 0 (no profit yet)

2. For each price in prices:
   a. Update min_price = min(min_price, current_price)
   b. Calculate potential profit = current_price - min_price
   c. Update profit = max(profit, potential_profit)

3. Return profit
```

---

## Detailed Example: Step-by-Step

**Input**: `prices = [7, 1, 5, 3, 6, 4]`

### Visual Representation

```
Day:     0    1    2    3    4    5
Price:   7    1    5    3    6    4
         │    │    │    │    │    │
         └────┴────┴────┴────┴────┘
         
Best buy: Day 1 (price = 1)
Best sell: Day 4 (price = 6)
Profit: 6 - 1 = 5
```

### Step-by-Step Execution

| Step | Day | Price | min_price | Potential Profit | profit | Action |
|------|-----|-------|-----------|-----------------|--------|--------|
| 0 | — | — | `∞` | — | 0 | Initialize |
| 1 | 0 | 7 | `7` | 7-7=0 | 0 | Update min, profit=0 |
| 2 | 1 | 1 | `1` | 1-1=0 | 0 | Update min (better buy) |
| 3 | 2 | 5 | `1` | 5-1=4 | 4 | Keep min, profit=4 |
| 4 | 3 | 3 | `1` | 3-1=2 | 4 | Keep min, profit=4 |
| 5 | 4 | 6 | `1` | 6-1=5 | 5 | Keep min, profit=5 ✅ |
| 6 | 5 | 4 | `1` | 4-1=3 | 5 | Keep min, profit=5 |

**Final Result**: `profit = 5` ✅

---

## Detailed Step Breakdown

### Initialization
```
prices = [7, 1, 5, 3, 6, 4]

min_price = float('inf')  (infinity - no price seen yet)
profit = 0                 (no profit yet)
```

### Step 1: Day 0, Price = 7

```
Current price: 7

Update minimum price:
  min_price = min(∞, 7) = 7
  Best buy price so far: 7

Calculate potential profit:
  If we sell today at price 7:
    profit = 7 - 7 = 0
  
Update maximum profit:
  profit = max(0, 0) = 0

State after step 1:
  min_price = 7
  profit = 0
  Best buy: Day 0 (price 7)
  Best sell: Day 0 (price 7) → profit = 0
```

**Visualization:**
```
Day:  0    1    2    3    4    5
Price: 7    1    5    3    6    4
      [B]                          Buy at 7, sell at 7 → profit = 0
      min_price = 7
```

### Step 2: Day 1, Price = 1 ✅ **NEW MINIMUM!**

```
Current price: 1

Update minimum price:
  min_price = min(7, 1) = 1
  Best buy price so far: 1 (better than 7!)

Calculate potential profit:
  If we sell today at price 1:
    profit = 1 - 1 = 0
  
Update maximum profit:
  profit = max(0, 0) = 0

State after step 2:
  min_price = 1
  profit = 0
  Best buy: Day 1 (price 1) ← Better buy price found!
  Best sell: Day 1 (price 1) → profit = 0
```

**Visualization:**
```
Day:  0    1    2    3    4    5
Price: 7    1    5    3    6    4
           [B]                    Buy at 1, sell at 1 → profit = 0
           min_price = 1 (better!)
```

**Key Insight**: We found a better buy price (1 < 7), so we update our minimum. Even though profit is 0, this sets us up for better profits later.

### Step 3: Day 2, Price = 5 ✅ **FIRST PROFIT!**

```
Current price: 5

Update minimum price:
  min_price = min(1, 5) = 1
  Best buy price so far: 1 (keep it)

Calculate potential profit:
  If we sell today at price 5:
    profit = 5 - 1 = 4
  
Update maximum profit:
  profit = max(0, 4) = 4  ← NEW MAXIMUM!

State after step 3:
  min_price = 1
  profit = 4
  Best buy: Day 1 (price 1)
  Best sell: Day 2 (price 5) → profit = 4 ✅
```

**Visualization:**
```
Day:  0    1    2    3    4    5
Price: 7    1    5    3    6    4
           [B]  [S]                 Buy at 1, sell at 5 → profit = 4
           min_price = 1
```

**Key Insight**: If we bought at day 1 (price 1) and sell today at day 2 (price 5), we make a profit of 4. This is the best profit so far!

### Step 4: Day 3, Price = 3

```
Current price: 3

Update minimum price:
  min_price = min(1, 3) = 1
  Best buy price so far: 1 (keep it)

Calculate potential profit:
  If we sell today at price 3:
    profit = 3 - 1 = 2
  
Update maximum profit:
  profit = max(4, 2) = 4  (keep current best)

State after step 4:
  min_price = 1
  profit = 4
  Best buy: Day 1 (price 1)
  Best sell: Day 2 (price 5) → profit = 4 (still best)
```

**Visualization:**
```
Day:  0    1    2    3    4    5
Price: 7    1    5    3    6    4
           [B]  [S]  [x]            Buy at 1, sell at 3 → profit = 2 (worse)
           min_price = 1
```

**Key Insight**: Selling today gives profit 2, which is less than our current best (4). We keep the previous best.

### Step 5: Day 4, Price = 6 ✅ **BEST PROFIT!**

```
Current price: 6

Update minimum price:
  min_price = min(1, 6) = 1
  Best buy price so far: 1 (keep it)

Calculate potential profit:
  If we sell today at price 6:
    profit = 6 - 1 = 5
  
Update maximum profit:
  profit = max(4, 5) = 5  ← NEW MAXIMUM!

State after step 5:
  min_price = 1
  profit = 5
  Best buy: Day 1 (price 1)
  Best sell: Day 4 (price 6) → profit = 5 ✅ BEST!
```

**Visualization:**
```
Day:  0    1    2    3    4    5
Price: 7    1    5    3    6    4
           [B]              [S]            Buy at 1, sell at 6 → profit = 5
           min_price = 1
```

**Key Insight**: If we bought at day 1 (price 1) and sell today at day 4 (price 6), we make a profit of 5. This is the best profit we can achieve!

### Step 6: Day 5, Price = 4

```
Current price: 4

Update minimum price:
  min_price = min(1, 4) = 1
  Best buy price so far: 1 (keep it)

Calculate potential profit:
  If we sell today at price 4:
    profit = 4 - 1 = 3
  
Update maximum profit:
  profit = max(5, 3) = 5  (keep current best)

State after step 6:
  min_price = 1
  profit = 5
  Best buy: Day 1 (price 1)
  Best sell: Day 4 (price 6) → profit = 5 (still best)
```

**Visualization:**
```
Day:  0    1    2    3    4    5
Price: 7    1    5    3    6    4
           [B]              [S]  [x]      Buy at 1, sell at 4 → profit = 3 (worse)
           min_price = 1
```

### Final Result

```
Maximum profit: 5
Best strategy:
  Buy on Day 1 at price 1
  Sell on Day 4 at price 6
  Profit: 6 - 1 = 5 ✅
```

---

## Key Concepts

### 1. Greedy Algorithm

At each step, we make the locally optimal choice:
- **Track minimum price**: Always know the best buy price seen so far
- **Calculate potential profit**: For each day, see what profit we'd get if we sell today
- **Track maximum profit**: Keep the best profit we've seen

### 2. Why Track Minimum Price?

We want to **buy low**, so we track the lowest price we've seen:
- If we see a lower price, it becomes our new "best buy" candidate
- We can always calculate: "If I bought at the minimum and sell today, what's my profit?"

### 3. Why Calculate Profit at Each Step?

For each day, we ask: **"If I sell today, what's my profit?"**
- We've already tracked the best buy price (minimum)
- Selling today at current price gives: `current_price - min_price`
- We keep the maximum of all these potential profits

### 4. Why This Works

**Invariant**: After processing day `i`, we know:
- The minimum price in `prices[0..i]` (best buy price)
- The maximum profit achievable by selling on any day in `[0..i]`

This is optimal because:
- We've considered all possible sell days up to day `i`
- We always use the best buy price (minimum) for each sell day
- We track the maximum profit across all possibilities

---

## Visual Timeline

```
Day:     0    1    2    3    4    5
Price:   7    1    5    3    6    4
         │    │    │    │    │    │
         
Step 1:  [B]                          min=7, profit=0
Step 2:      [B]                      min=1, profit=0 (better buy!)
Step 3:      [B]  [S]                 min=1, profit=4 (buy at 1, sell at 5)
Step 4:      [B]      [x]             min=1, profit=4 (sell at 3 gives 2, worse)
Step 5:      [B]          [S]         min=1, profit=5 (buy at 1, sell at 6) ✅ BEST!
Step 6:      [B]          [S]  [x]    min=1, profit=5 (sell at 4 gives 3, worse)

Final: Buy at day 1 (price 1), Sell at day 4 (price 6) → Profit = 5
```

---

## Algorithm Pseudocode

```python
def maxProfit(prices):
    min_price = infinity  # Best buy price seen so far
    profit = 0            # Maximum profit seen so far
    
    for price in prices:
        # Update best buy price (minimum seen so far)
        min_price = min(min_price, price)
        
        # Calculate profit if we sell today
        # (using the best buy price we've seen)
        potential_profit = price - min_price
        
        # Update maximum profit
        profit = max(profit, potential_profit)
    
    return profit
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(n) | Single pass through the array |
| **Space** | O(1) | Only uses two variables (min_price, profit) |

---

## Edge Cases

### Case 1: No Profit Possible (Decreasing Prices)
```
prices = [7, 6, 4, 3, 1]
Result: 0
Explanation: Prices only decrease, can't make profit
```

**Step-by-step:**
- Day 0: price=7, min=7, profit=0
- Day 1: price=6, min=6, profit=0
- Day 2: price=4, min=4, profit=0
- Day 3: price=3, min=3, profit=0
- Day 4: price=1, min=1, profit=0
- Final: profit = 0

### Case 2: Always Increasing
```
prices = [1, 2, 3, 4, 5]
Result: 4
Explanation: Buy at 1, sell at 5 → profit = 4
```

**Step-by-step:**
- Day 0: price=1, min=1, profit=0
- Day 1: price=2, min=1, profit=1
- Day 2: price=3, min=1, profit=2
- Day 3: price=4, min=1, profit=3
- Day 4: price=5, min=1, profit=4 ✅
- Final: profit = 4

### Case 3: Single Element
```
prices = [5]
Result: 0
Explanation: Can't buy and sell on same day
```

### Case 4: Two Elements
```
prices = [3, 2]
Result: 0 (decreasing)

prices = [2, 3]
Result: 1 (buy at 2, sell at 3)
```

### Case 5: Multiple Local Maxima
```
prices = [3, 2, 6, 1, 4]
Result: 4
Explanation: Buy at 2, sell at 6 → profit = 4
```

**Step-by-step:**
- Day 0: price=3, min=3, profit=0
- Day 1: price=2, min=2, profit=0
- Day 2: price=6, min=2, profit=4 ✅
- Day 3: price=1, min=1, profit=4
- Day 4: price=4, min=1, profit=4
- Final: profit = 4

---

## Why This Algorithm Works

### Correctness Proof

**Claim**: After processing all prices, `profit` contains the maximum profit achievable.

**Proof by Invariant**:
1. **After day i**, we know:
   - `min_price` = minimum price in `prices[0..i]`
   - `profit` = maximum profit achievable by selling on any day in `[0..i]`

2. **Base case** (i=0):
   - `min_price = prices[0]` ✓
   - `profit = 0` (can't sell before buying) ✓

3. **Inductive step**:
   - For day i+1:
     - `min_price` is updated to include `prices[i+1]` ✓
     - We calculate profit if selling on day i+1: `prices[i+1] - min_price`
     - We update `profit` to maximum of previous best and current profit ✓
   - Invariant maintained! ✓

4. **After all days**:
   - We've considered selling on every possible day
   - For each sell day, we used the best buy price (minimum)
   - Therefore, `profit` is the maximum possible ✓

### Optimal Substructure

The problem has optimal substructure:
- Maximum profit up to day `i` depends only on:
  - Minimum price seen so far
  - Maximum profit seen so far
- We don't need to reconsider previous decisions

---

## Alternative Approaches

### Approach 1: Brute Force (O(n²))
```python
def maxProfit_brute_force(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit
```
**Time**: O(n²), **Space**: O(1)

### Approach 2: Dynamic Programming (O(n))
```python
def maxProfit_dp(prices):
    n = len(prices)
    # dp[i] = max profit up to day i
    dp = [0] * n
    min_price = prices[0]
    
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        dp[i] = max(dp[i-1], prices[i] - min_price)
    
    return dp[n-1]
```
**Time**: O(n), **Space**: O(n)

Our greedy approach is essentially the space-optimized version of DP!

---

## Summary

The maximum profit algorithm:
- Uses **greedy approach** with single pass
- Tracks **minimum price** (best buy price)
- Calculates **potential profit** at each step
- Maintains **maximum profit** seen so far
- Time complexity: **O(n)**
- Space complexity: **O(1)**

**Key Insight**: For each day, if we sell today, the best profit uses the minimum buy price seen so far. Track both the minimum price and maximum profit.

---

## Related Problems

- **LeetCode 122**: Best Time to Buy and Sell Stock II (multiple transactions)
- **LeetCode 123**: Best Time to Buy and Sell Stock III (at most 2 transactions)
- **LeetCode 188**: Best Time to Buy and Sell Stock IV (at most k transactions)
- **LeetCode 309**: Best Time to Buy and Sell Stock with Cooldown
- **LeetCode 714**: Best Time to Buy and Sell Stock with Transaction Fee

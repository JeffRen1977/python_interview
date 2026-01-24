# Decode Ways

> **LeetCode 91**: A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> "1", 'B' -> "2", ..., 'Z' -> "26". Given a string `s` containing only digits, return the number of ways to decode it.

## Problem Description

Count the number of ways to decode a string of digits into letters.

**Mapping:**
- 'A' = "1"
- 'B' = "2"
- ...
- 'Z' = "26"

**Example:**
- `s = "226"` → Can be decoded as:
  - "2" + "2" + "6" = "BBF"
  - "22" + "6" = "VF"
  - "2" + "26" = "BZ"
  - Answer: `3` ways

---

## Key Insight

Use **Dynamic Programming**:
- `dp[i]` = number of ways to decode substring `s[0..i-1]`
- At position `i`, we can decode:
  - Single digit: if `s[i-1]` is valid (1-9), add `dp[i-1]`
  - Two digits: if `s[i-2..i-1]` is valid (10-26), add `dp[i-2]`

**Strategy**: Build solution bottom-up, considering both single and two-digit decodings.

---

## Algorithm Logic

```
1. Initialize:
   - dp[0] = 1 (one way to decode empty string)
   - dp[1] = 0 if s[0] == '0', else 1

2. For each position i from 2 to n:
   a. Check single digit: s[i-1]
      - If valid (1-9): dp[i] += dp[i-1]
   b. Check two digits: s[i-2..i-1]
      - If valid (10-26): dp[i] += dp[i-2]

3. Return dp[n]
```

---

## Detailed Example: Step-by-Step

**Input**: `s = "226"`

### Initial Setup

```
s = "226"
n = len(s) = 3

dp = [0, 0, 0, 0]  (n+1 = 4 elements, indices 0-3)
      ↑  ↑  ↑  ↑
      0  1  2  3

Base cases:
dp[0] = 1  (one way to decode empty string)
dp[1] = 1  (s[0] = '2' is valid, so 1 way to decode "2")
```

### Visual Representation

```
String:  2  2  6
Index:   0  1  2
         │  │  │
         
dp[i] = number of ways to decode s[0..i-1]

dp[0] = 1  (decode "")
dp[1] = 1  (decode "2")
dp[2] = ?  (decode "22")
dp[3] = ?  (decode "226")
```

### Step-by-Step Execution

| Step | i | Substring | first (s[i-1]) | second (s[i-2..i-1]) | Valid? | dp[i] Calculation | dp Array |
|------|---|-----------|----------------|----------------------|--------|-------------------|----------|
| 0 | — | "" | — | — | — | Base case | `[1, 1, 0, 0]` |
| 1 | — | "2" | — | — | — | Base case | `[1, 1, 0, 0]` |
| 2 | 2 | "22" | '2' (2) | "22" (22) | Both valid | `dp[2] = dp[1] + dp[0] = 1 + 1 = 2` | `[1, 1, 2, 0]` |
| 3 | 3 | "226" | '6' (6) | "26" (26) | Both valid | `dp[3] = dp[2] + dp[1] = 2 + 1 = 3` | `[1, 1, 2, 3]` |

**Final Result**: `dp[3] = 3` ✅

---

## Detailed Step Breakdown

### Initialization

```
s = "226"
n = 3

dp = [0, 0, 0, 0]
      ↑  ↑  ↑  ↑
      0  1  2  3

Base case 1: dp[0] = 1
  Meaning: There is 1 way to decode an empty string
  (This is needed for the recurrence relation)

Base case 2: dp[1] = ?
  s[0] = '2'
  '2' is valid (1-9) → dp[1] = 1
  Meaning: There is 1 way to decode "2" → "B"
```

**After initialization:**
```
dp = [1, 1, 0, 0]
      ↑  ↑  ↑  ↑
      0  1  2  3
```

### Step 2: i = 2, Decoding "22"

```
Substring to decode: s[0..1] = "22"

Check single digit (first):
  first = int(s[1]) = int('2') = 2
  1 <= 2 <= 9? YES ✅
  This means we can decode the last digit '2' as a single letter "B"
  If we do this, we need to decode "2" (first character)
  Number of ways to decode "2" = dp[1] = 1
  So: dp[2] += dp[1] = 1

Check two digits (second):
  second = int(s[0..1]) = int("22") = 22
  10 <= 22 <= 26? YES ✅
  This means we can decode "22" as a two-digit number "V"
  If we do this, we need to decode "" (empty string before "22")
  Number of ways to decode "" = dp[0] = 1
  So: dp[2] += dp[0] = 1

Total: dp[2] = 1 + 1 = 2

Decoding ways for "22":
  1. "2" + "2" = "B" + "B" = "BB"
  2. "22" = "V"
  Total: 2 ways ✅
```

**Visualization:**
```
String:  2  2  6
Index:   0  1  2

Decoding "22":
  Option 1: [2] [2]     → "B" + "B" = "BB"
            ↑   ↑
            Use dp[1] (decode "2") + decode "2"
  
  Option 2: [22]        → "V"
            ↑↑
            Use dp[0] (decode "") + decode "22"
```

**After step 2:**
```
dp = [1, 1, 2, 0]
      ↑  ↑  ↑  ↑
      0  1  2  3
```

### Step 3: i = 3, Decoding "226"

```
Substring to decode: s[0..2] = "226"

Check single digit (first):
  first = int(s[2]) = int('6') = 6
  1 <= 6 <= 9? YES ✅
  This means we can decode the last digit '6' as a single letter "F"
  If we do this, we need to decode "22" (first two characters)
  Number of ways to decode "22" = dp[2] = 2
  So: dp[3] += dp[2] = 2

Check two digits (second):
  second = int(s[1..2]) = int("26") = 26
  10 <= 26 <= 26? YES ✅
  This means we can decode "26" as a two-digit number "Z"
  If we do this, we need to decode "2" (first character)
  Number of ways to decode "2" = dp[1] = 1
  So: dp[3] += dp[1] = 1

Total: dp[3] = 2 + 1 = 3

Decoding ways for "226":
  1. "2" + "2" + "6" = "B" + "B" + "F" = "BBF"
  2. "22" + "6" = "V" + "F" = "VF"
  3. "2" + "26" = "B" + "Z" = "BZ"
  Total: 3 ways ✅
```

**Visualization:**
```
String:  2  2  6
Index:   0  1  2

Decoding "226":
  Option 1: [2] [2] [6]   → "B" + "B" + "F" = "BBF"
            ↑   ↑   ↑
            Use dp[2] (decode "22") + decode "6"
  
  Option 2: [22] [6]       → "V" + "F" = "VF"
            ↑↑   ↑
            Use dp[2] (decode "22") + decode "6"
            (Wait, this is the same as Option 1...)
  
  Actually, let me reconsider:
  
  From dp[2] = 2 ways to decode "22":
    - "2" + "2" → "BB"
    - "22" → "V"
  
  If we add "6":
    - "BB" + "F" = "BBF"  (from "2" + "2" + "6")
    - "V" + "F" = "VF"     (from "22" + "6")
  
  Option 3: [2] [26]       → "B" + "Z" = "BZ"
            ↑   ↑↑
            Use dp[1] (decode "2") + decode "26"
```

**After step 3:**
```
dp = [1, 1, 2, 3]
      ↑  ↑  ↑  ↑
      0  1  2  3
```

### Final Result

```
dp[3] = 3

Total ways to decode "226":
  1. "BBF" (2 + 2 + 6)
  2. "VF" (22 + 6)
  3. "BZ" (2 + 26)
```

---

## Another Example: "11106"

**Input**: `s = "11106"`

### Step-by-Step

| Step | i | Substring | first | second | Valid? | dp[i] | dp Array |
|------|---|-----------|-------|--------|--------|-------|----------|
| 0 | — | "" | — | — | — | 1 | `[1, ...]` |
| 1 | — | "1" | — | — | — | 1 | `[1, 1, ...]` |
| 2 | 2 | "11" | 1 | 11 | Both | 2 | `[1, 1, 2, ...]` |
| 3 | 3 | "111" | 1 | 11 | Both | 3 | `[1, 1, 2, 3, ...]` |
| 4 | 4 | "1110" | 0 | 10 | Only second | 2 | `[1, 1, 2, 3, 2, ...]` |
| 5 | 5 | "11106" | 6 | 06 | Only first | 2 | `[1, 1, 2, 3, 2, 2]` |

**Detailed Step 4 (i=4, "1110"):**
```
first = int(s[3]) = int('0') = 0
1 <= 0 <= 9? NO ✗
Cannot decode '0' as single digit

second = int(s[2..3]) = int("10") = 10
10 <= 10 <= 26? YES ✅
Can decode "10" as "J"
dp[4] += dp[2] = 2

Result: dp[4] = 2
Ways: "11" + "10" = "AA" + "J" = "AAJ"
      "1" + "1" + "10" = "A" + "A" + "J" = "AAJ"
Wait, that's the same... Let me recalculate:

Actually:
  dp[2] = 2 ways to decode "11":
    1. "1" + "1" = "A" + "A" = "AA"
    2. "11" = "K"
  
  Adding "10":
    1. "AA" + "J" = "AAJ"
    2. "K" + "J" = "KJ"
  
  So dp[4] = 2 ✅
```

**Detailed Step 5 (i=5, "11106"):**
```
first = int(s[4]) = int('6') = 6
1 <= 6 <= 9? YES ✅
Can decode '6' as "F"
dp[5] += dp[4] = 2

second = int(s[3..4]) = int("06") = 6
10 <= 6 <= 26? NO ✗
Cannot decode "06" (starts with 0)

Result: dp[5] = 2
Ways: "AAJ" + "F" = "AAJF"
      "KJ" + "F" = "KJF"
```

**Final Result**: `dp[5] = 2` ✅

---

## Key Concepts

### 1. Dynamic Programming State

**`dp[i]`** = number of ways to decode substring `s[0..i-1]`

**State Transition:**
- If we decode the last character as a single digit:
  - `dp[i] += dp[i-1]` (if `s[i-1]` is valid 1-9)
- If we decode the last two characters as a two-digit number:
  - `dp[i] += dp[i-2]` (if `s[i-2..i-1]` is valid 10-26)

### 2. Base Cases

**`dp[0] = 1`**: One way to decode empty string
- Needed for recurrence: when we decode two digits, we need `dp[i-2]`
- If `i = 2`, we need `dp[0]` to represent decoding the prefix

**`dp[1]`**: 
- If `s[0] == '0'`: `dp[1] = 0` (invalid, can't start with 0)
- Otherwise: `dp[1] = 1` (one way to decode single digit)

### 3. Valid Single Digit (1-9)

A single digit is valid if it's between 1 and 9:
- '0' is NOT valid (no letter maps to 0)
- '1' to '9' are valid

### 4. Valid Two Digits (10-26)

A two-digit number is valid if it's between 10 and 26:
- "01" to "09" are NOT valid (can't start with 0)
- "10" to "26" are valid
- "27" to "99" are NOT valid (no letters map to them)

### 5. Why Add Both Possibilities?

At each position, we consider TWO ways to decode:
1. **Single digit**: Decode just the last character
2. **Two digits**: Decode the last two characters together

We add both because they represent different decoding strategies, and we want to count ALL possible ways.

---

## Visual DP Table Evolution

```
Example: s = "226"

Initial:
Index:  0  1  2  3
dp:    [1, 1, 0, 0]
       ↑  ↑
    base cases

After i=2 ("22"):
Index:  0  1  2  3
dp:    [1, 1, 2, 0]
              ↑
        1 (single '2') + 1 (two "22") = 2

After i=3 ("226"):
Index:  0  1  2  3
dp:    [1, 1, 2, 3]
                 ↑
        2 (single '6', use dp[2]) + 1 (two "26", use dp[1]) = 3
```

---

## Algorithm Pseudocode

```python
def numDecodings(s):
    n = len(s)
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 1  # Empty string
    dp[1] = 0 if s[0] == '0' else 1  # First character
    
    # Fill DP table
    for i in range(2, n + 1):
        # Check single digit
        first = int(s[i-1])
        if 1 <= first <= 9:
            dp[i] += dp[i-1]
        
        # Check two digits
        second = int(s[i-2:i])
        if 10 <= second <= 26:
            dp[i] += dp[i-2]
    
    return dp[n]
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(n) | Single pass through the string |
| **Space** | O(n) | DP array of size (n+1) |

**Space Optimization**: Can be optimized to O(1) by only keeping `dp[i-2]` and `dp[i-1]` instead of the entire array.

---

## Edge Cases

### Case 1: Starts with '0'
```
s = "06"
Result: 0

dp[0] = 1
dp[1] = 0  (s[0] = '0' is invalid)
dp[2] = 0  (can't decode "06")
```

### Case 2: Contains '0' in Middle
```
s = "10"
Result: 1

dp[0] = 1
dp[1] = 1  (s[0] = '1' is valid)
dp[2] = 1  (s[1] = '0' invalid, but "10" is valid)
  - Single digit '0': invalid
  - Two digits "10": valid → dp[2] += dp[0] = 1
```

### Case 3: All Valid Single Digits
```
s = "123"
Result: 3

Ways:
  1. "1" + "2" + "3" = "ABC"
  2. "12" + "3" = "LC"
  3. "1" + "23" = "AW"
```

### Case 4: Two-Digit Numbers Only
```
s = "1010"
Result: 1

Only valid decoding: "10" + "10" = "JJ"
Cannot decode as single digits (contains '0')
```

### Case 5: Large Two-Digit Numbers
```
s = "27"
Result: 1

"27" > 26, so cannot decode as two digits
Only: "2" + "7" = "BG"
```

---

## Why This Algorithm Works

### Optimal Substructure

The problem has optimal substructure:
- To decode `s[0..i-1]`, we can either:
  - Decode `s[0..i-2]` and then decode `s[i-1]` as single digit
  - Decode `s[0..i-3]` and then decode `s[i-2..i-1]` as two digits
- `dp[i] = dp[i-1]` (if single digit valid) + `dp[i-2]` (if two digits valid)

### Overlapping Subproblems

The same substrings are decoded multiple times:
- "22" appears when decoding "226" and "2226"
- DP memoizes these results

### Correctness Proof

**Invariant**: After processing position `i`, `dp[i]` contains the number of ways to decode `s[0..i-1]`.

**Base case**: `dp[0] = 1` and `dp[1]` are correct.

**Inductive step**: For position `i`:
- If single digit `s[i-1]` is valid, we can decode it and need `dp[i-1]` ways for the prefix
- If two digits `s[i-2..i-1]` is valid, we can decode them and need `dp[i-2]` ways for the prefix
- We sum both possibilities to get all ways
- Invariant maintained ✓

---

## Space-Optimized Version

```python
def numDecodings_optimized(s):
    n = len(s)
    
    # Only need dp[i-2] and dp[i-1]
    prev2 = 1  # dp[0]
    prev1 = 0 if s[0] == '0' else 1  # dp[1]
    
    for i in range(2, n + 1):
        current = 0
        
        # Single digit
        first = int(s[i-1])
        if 1 <= first <= 9:
            current += prev1
        
        # Two digits
        second = int(s[i-2:i])
        if 10 <= second <= 26:
            current += prev2
        
        # Move pointers
        prev2 = prev1
        prev1 = current
    
    return prev1
```

**Space**: O(1) instead of O(n)

---

## Summary

The decode ways algorithm:
- Uses **dynamic programming** with bottom-up approach
- `dp[i]` = number of ways to decode `s[0..i-1]`
- Considers both single-digit and two-digit decodings
- Time complexity: **O(n)**
- Space complexity: **O(n)** (can be optimized to O(1))

**Key Insight**: At each position, we can decode the last character alone OR the last two characters together. Sum both possibilities to get total ways.

---

## Related Problems

- **LeetCode 639**: Decode Ways II (includes '*' wildcard)
- **LeetCode 91**: Decode Ways (this problem)
- **LeetCode 70**: Climbing Stairs (similar DP structure)
- **LeetCode 198**: House Robber (similar DP pattern)

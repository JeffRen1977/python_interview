# Expression Add Operators

> **LeetCode 282**: Given a string `num` that contains only digits and an integer `target`, return all possibilities to insert the binary operators `+`, `-`, or `*` between the digits of `num` so that the resultant expression evaluates to the `target` value.

## Problem Description

Insert `+`, `-`, or `*` operators between digits to create expressions that evaluate to a target value.

**Rules:**
- Operators can only be inserted between digits
- No leading zeros (e.g., "05" is invalid, but "0" is valid)
- Must use all digits in order
- Return all valid expressions

**Example:**
- `num = "123"`, `target = 6`
- Valid expressions: `"1+2+3"`, `"1*2*3"`
- Answer: `["1+2+3", "1*2*3"]`

---

## Key Insight

Use **Backtracking/DFS** to try all operator placements:
- For each position, try `+`, `-`, or `*`
- Handle operator precedence: multiplication has higher precedence
- Use `flast` to correctly handle multiplication (undo last operation, apply multiplication)

**Strategy**: Build expressions recursively, tracking current value and last operand for multiplication.

---

## Algorithm Logic

```
1. For each possible first number (1 to len(num) digits):
   - If valid (no leading zero), start DFS

2. DFS(num, fstr, fval, flast, res):
   - fstr: current expression string
   - fval: current expression value
   - flast: last operand (for handling multiplication)
   
   Base case: if num is empty:
     - If fval == target, add fstr to result
   
   For each possible next number (1 to len(num) digits):
     - If valid (no leading zero):
       - Try '+': fval + val, flast = val
       - Try '-': fval - val, flast = -val
       - Try '*': fval - flast + flast * val, flast = flast * val
```

---

## Key Concept: Handling Multiplication

**Problem**: Multiplication has higher precedence than addition/subtraction.

**Example**: `2 + 3 * 4`
- If we compute left-to-right: `2 + 3 = 5`, then `5 * 4 = 20` ❌
- Correct: `2 + (3 * 4) = 2 + 12 = 14` ✅

**Solution**: Use `flast` to track the last operand:
- For `+` and `-`: `flast = val` (or `-val`)
- For `*`: Undo last operation, then apply multiplication
  - `fval = fval - flast + flast * val`
  - `flast = flast * val`

---

## Detailed Example: Step-by-Step

**Input**: `num = "123"`, `target = 6`

### Initial Setup

```
num = "123"
target = 6
res = []
```

### Phase 1: Choose First Number

**Option 1: First number = "1"**
```
fstr = "1"
fval = 1
flast = 1
Remaining: "23"
```

**Option 2: First number = "12"**
```
fstr = "12"
fval = 12
flast = 12
Remaining: "3"
```

**Option 3: First number = "123"**
```
fstr = "123"
fval = 123
flast = 123
Remaining: ""
→ Check: 123 == 6? NO
```

### Detailed DFS: Starting with "1"

**DFS("23", "1", 1, 1, res)**

#### Try Next Number: "2"

**Option A: Add "+"**
```
fstr = "1+2"
fval = 1 + 2 = 3
flast = 2  (last operand for multiplication)
Remaining: "3"
Call: DFS("3", "1+2", 3, 2, res)
```

**DFS("3", "1+2", 3, 2, res)**
```
Remaining: "3"
Try number: "3"

Option A1: Add "+"
  fstr = "1+2+3"
  fval = 3 + 3 = 6
  flast = 3
  Remaining: ""
  → Check: 6 == 6? YES ✅
  → Add "1+2+3" to res

Option A2: Add "-"
  fstr = "1+2-3"
  fval = 3 - 3 = 0
  flast = -3
  Remaining: ""
  → Check: 0 == 6? NO

Option A3: Add "*"
  fstr = "1+2*3"
  fval = 3 - 2 + 2 * 3 = 3 - 2 + 6 = 7
  flast = 2 * 3 = 6
  Remaining: ""
  → Check: 7 == 6? NO
```

**Option B: Add "-"**
```
fstr = "1-2"
fval = 1 - 2 = -1
flast = -2  (negative for subtraction)
Remaining: "3"
Call: DFS("3", "1-2", -1, -2, res)
```

**DFS("3", "1-2", -1, -2, res)**
```
Remaining: "3"
Try number: "3"

Option B1: Add "+"
  fstr = "1-2+3"
  fval = -1 + 3 = 2
  flast = 3
  → Check: 2 == 6? NO

Option B2: Add "-"
  fstr = "1-2-3"
  fval = -1 - 3 = -4
  flast = -3
  → Check: -4 == 6? NO

Option B3: Add "*"
  fstr = "1-2*3"
  fval = -1 - (-2) + (-2) * 3 = -1 + 2 - 6 = -5
  flast = -2 * 3 = -6
  → Check: -5 == 6? NO
```

**Option C: Add "*"**
```
fstr = "1*2"
fval = 1 - 1 + 1 * 2 = 0 + 2 = 2
flast = 1 * 2 = 2
Remaining: "3"
Call: DFS("3", "1*2", 2, 2, res)
```

**DFS("3", "1*2", 2, 2, res)**
```
Remaining: "3"
Try number: "3"

Option C1: Add "+"
  fstr = "1*2+3"
  fval = 2 + 3 = 5
  flast = 3
  → Check: 5 == 6? NO

Option C2: Add "-"
  fstr = "1*2-3"
  fval = 2 - 3 = -1
  flast = -3
  → Check: -1 == 6? NO

Option C3: Add "*"
  fstr = "1*2*3"
  fval = 2 - 2 + 2 * 3 = 0 + 6 = 6
  flast = 2 * 3 = 6
  → Check: 6 == 6? YES ✅
  → Add "1*2*3" to res
```

#### Try Next Number: "23"

**Option A: Add "+"**
```
fstr = "1+23"
fval = 1 + 23 = 24
flast = 23
Remaining: ""
→ Check: 24 == 6? NO
```

**Option B: Add "-"**
```
fstr = "1-23"
fval = 1 - 23 = -22
flast = -23
Remaining: ""
→ Check: -22 == 6? NO
```

**Option C: Add "*"**
```
fstr = "1*23"
fval = 1 - 1 + 1 * 23 = 0 + 23 = 23
flast = 1 * 23 = 23
Remaining: ""
→ Check: 23 == 6? NO
```

### Detailed DFS: Starting with "12"

**DFS("3", "12", 12, 12, res)**

#### Try Next Number: "3"

**Option A: Add "+"**
```
fstr = "12+3"
fval = 12 + 3 = 15
flast = 3
Remaining: ""
→ Check: 15 == 6? NO
```

**Option B: Add "-"**
```
fstr = "12-3"
fval = 12 - 3 = 9
flast = -3
Remaining: ""
→ Check: 9 == 6? NO
```

**Option C: Add "*"**
```
fstr = "12*3"
fval = 12 - 12 + 12 * 3 = 0 + 36 = 36
flast = 12 * 3 = 36
Remaining: ""
→ Check: 36 == 6? NO
```

### Final Result

```
res = ["1+2+3", "1*2*3"]
```

---

## Understanding Multiplication Handling

### Example: "2+3*4"

**Step-by-step calculation:**

```
Initial: fstr = "2", fval = 2, flast = 2

Add "+3":
  fstr = "2+3"
  fval = 2 + 3 = 5
  flast = 3  (last operand)

Add "*4":
  fstr = "2+3*4"
  fval = 5 - 3 + 3 * 4  (undo last +3, apply *4)
       = 5 - 3 + 12
       = 2 + 12
       = 14 ✅
  flast = 3 * 4 = 12
```

**Why this works:**
- Original: `2 + 3 = 5`
- We want: `2 + (3 * 4) = 2 + 12 = 14`
- Formula: `fval - flast + flast * val`
  - `5 - 3 + 3 * 4 = 2 + 12 = 14` ✅

### Example: "2*3*4"

```
Initial: fstr = "2", fval = 2, flast = 2

Add "*3":
  fstr = "2*3"
  fval = 2 - 2 + 2 * 3 = 6
  flast = 2 * 3 = 6

Add "*4":
  fstr = "2*3*4"
  fval = 6 - 6 + 6 * 4  (undo last *3, apply *4)
       = 0 + 24
       = 24 ✅
  flast = 6 * 4 = 24
```

---

## Visual Decision Tree

```
Example: "123", target = 6

                    "123"
                   /  |  \
            "1"   "12"  "123"
            /|\     |      |
        +2  -2  *2  3      (check: 123==6? NO)
        |   |   |
       "3" "3" "3"
       /|\ /|\ /|\
      + - * + - * + - *
      | | | | | | | | |
      
Valid paths:
  "1+2+3" = 6 ✅
  "1*2*3" = 6 ✅
```

---

## Algorithm Pseudocode

```python
def addOperators(num, target):
    res = []
    
    # Try all possible first numbers
    for i in range(1, len(num) + 1):
        first_num = num[:i]
        # Check for leading zero
        if i == 1 or (i > 1 and num[0] != '0'):
            dfs(num[i:], first_num, int(first_num), int(first_num), res)
    
    return res

def dfs(num, fstr, fval, flast, res):
    # Base case: no more digits
    if not num:
        if fval == target:
            res.append(fstr)
        return
    
    # Try all possible next numbers
    for i in range(1, len(num) + 1):
        val_str = num[:i]
        # Check for leading zero
        if i == 1 or (i > 1 and num[0] != '0'):
            val = int(val_str)
            
            # Try addition
            dfs(num[i:], fstr + '+' + val_str, 
                fval + val, val, res)
            
            # Try subtraction
            dfs(num[i:], fstr + '-' + val_str,
                fval - val, -val, res)
            
            # Try multiplication
            dfs(num[i:], fstr + '*' + val_str,
                fval - flast + flast * val, flast * val, res)
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(4^n) | At each position, 3 operators + 1 option to continue number. n digits → 4^n possibilities |
| **Space** | O(n) | Recursion stack depth (n levels), plus result storage |

**Note**: In practice, many branches are pruned early, so actual runtime is often better.

---

## Edge Cases

### Case 1: Leading Zeros
```
num = "105", target = 5
Valid: "10-5", "1*0+5"
Invalid: "1+05" (leading zero in "05")
```

**Rule**: `i == 1 or (i > 1 and num[0] != '0')`
- Single digit "0" is valid
- Multi-digit starting with "0" is invalid

### Case 2: All Zeros
```
num = "00", target = 0
Valid: "0+0", "0-0", "0*0"
All evaluate to 0 ✅
```

### Case 3: No Solution
```
num = "3456237490", target = 9191
Result: []
(No expression evaluates to 9191)
```

### Case 4: Single Digit
```
num = "5", target = 5
Result: ["5"]
```

### Case 5: Large Numbers
```
num = "123456789", target = 45
Result: ["12+34-5+6-7+8+9"]
```

---

## Why Multiplication Formula Works

**Formula**: `fval = fval - flast + flast * val`

**Why subtract `flast`?**
- `flast` was added/subtracted in the previous step
- We need to "undo" that operation to apply multiplication correctly

**Example**: `2 + 3 * 4`
```
Step 1: "2+3"
  fval = 2 + 3 = 5
  flast = 3

Step 2: "*4"
  We want: 2 + (3 * 4) = 2 + 12 = 14
  
  Current: fval = 5 (which is 2 + 3)
  We need to replace "3" with "3 * 4"
  
  Formula: fval - flast + flast * val
          = 5 - 3 + 3 * 4
          = 2 + 12
          = 14 ✅
```

**For subtraction**: `flast = -val`
- When we subtract, we store negative value
- Multiplication still works: `fval - (-val) + (-val) * new_val`

---

## Summary

The expression add operators algorithm:
- Uses **backtracking/DFS** to try all operator placements
- Handles **operator precedence** using `flast` for multiplication
- Prevents **leading zeros** in multi-digit numbers
- Time complexity: **O(4^n)** (exponential)
- Space complexity: **O(n)** for recursion stack

**Key Insight**: Use `flast` to track the last operand. For multiplication, undo the last operation (`fval - flast`) and apply multiplication (`+ flast * val`). This correctly handles operator precedence.

---

## Related Problems

- **LeetCode 241**: Different Ways to Add Parentheses
- **LeetCode 224**: Basic Calculator
- **LeetCode 227**: Basic Calculator II
- **LeetCode 282**: Expression Add Operators (this problem)

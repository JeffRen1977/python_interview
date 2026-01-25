# Minimum Remove to Make Valid Parentheses

> **LeetCode 1249**: Given a string s of '(' , ')' and lowercase English characters, remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid. Return any valid string.

## Problem Description

Remove the minimum number of parentheses to make the string valid.

**Valid Parentheses Rules:**
- Every opening parenthesis `(` must have a corresponding closing parenthesis `)`
- Every closing parenthesis `)` must have a corresponding opening parenthesis `(`
- Parentheses must be properly nested

**Example:**
- Input: `"lee(t(c)o)de)"`
- Output: `"lee(t(c)o)de"` (remove one `)` at the end)

---

## Key Insight

**Stack-Based Approach:**
- Use a stack to track indices of unmatched parentheses
- For `(`: push index onto stack
- For `)`: if stack has matching `(`, pop it; otherwise push index (unmatched)
- After processing, stack contains indices of all unmatched parentheses
- Remove characters at those indices

**Why Stack Works:**
- Stack naturally handles nested parentheses
- Last-in-first-out matches opening and closing parentheses
- Unmatched parentheses remain in stack

---

## Algorithm Logic

```
1. Initialize stack to store indices of unmatched parentheses

2. First Pass: Process string character by character
   For each character:
     - If '(': push index onto stack
     - If ')': 
       - If stack has matching '(', pop it
       - Otherwise, push index (unmatched)
     - If other character: ignore

3. Second Pass: Build result string
   For each index in string:
     - If index is in stack (unmatched): skip it
     - Otherwise: add character to result

4. Return result string
```

---

## Detailed Example 1: Step-by-Step

**Input**: `s = "lee(t(c)o)de)"`

### Step-by-Step Execution

#### Step 1: Initialize

```
s = "lee(t(c)o)de)"
stk = deque()  (empty stack)
```

#### Step 2: First Pass - Process Each Character

**Index 0: 'l'**
```
ch = 'l'
Not '(' or ')', skip
stk = []
```

**Index 1: 'e'**
```
ch = 'e'
Not '(' or ')', skip
stk = []
```

**Index 2: 'e'**
```
ch = 'e'
Not '(' or ')', skip
stk = []
```

**Index 3: '('**
```
ch = '('
Push index 3 onto stack
stk = [3]
```

**Index 4: 't'**
```
ch = 't'
Not '(' or ')', skip
stk = [3]
```

**Index 5: '('**
```
ch = '('
Push index 5 onto stack
stk = [3, 5]
```

**Index 6: 'c'**
```
ch = 'c'
Not '(' or ')', skip
stk = [3, 5]
```

**Index 7: ')'**
```
ch = ')'
Check: stk and s[stk[-1]] == '('?
  stk[-1] = 5
  s[5] = '(' ✅
  Pop from stack
stk = [3]
```

**Index 8: 'o'**
```
ch = 'o'
Not '(' or ')', skip
stk = [3]
```

**Index 9: ')'**
```
ch = ')'
Check: stk and s[stk[-1]] == '('?
  stk[-1] = 3
  s[3] = '(' ✅
  Pop from stack
stk = []
```

**Index 10: 'd'**
```
ch = 'd'
Not '(' or ')', skip
stk = []
```

**Index 11: 'e'**
```
ch = 'e'
Not '(' or ')', skip
stk = []
```

**Index 12: ')'**
```
ch = ')'
Check: stk and s[stk[-1]] == '('?
  stk is empty ❌
  Push index 12 onto stack (unmatched)
stk = [12]
```

**After First Pass:**
```
stk = [12]  (index of unmatched ')')
```

#### Step 3: Second Pass - Build Result

```
res = ""
stk = [12]

Index 0: 'l'
  stk[0] = 12, i = 0
  0 == 12? NO
  res += 'l'  → res = "l"

Index 1: 'e'
  stk[0] = 12, i = 1
  1 == 12? NO
  res += 'e'  → res = "le"

Index 2: 'e'
  stk[0] = 12, i = 2
  2 == 12? NO
  res += 'e'  → res = "lee"

Index 3: '('
  stk[0] = 12, i = 3
  3 == 12? NO
  res += '('  → res = "lee("

Index 4: 't'
  stk[0] = 12, i = 4
  4 == 12? NO
  res += 't'  → res = "lee(t"

Index 5: '('
  stk[0] = 12, i = 5
  5 == 12? NO
  res += '('  → res = "lee(t("

Index 6: 'c'
  stk[0] = 12, i = 6
  6 == 12? NO
  res += 'c'  → res = "lee(t(c"

Index 7: ')'
  stk[0] = 12, i = 7
  7 == 12? NO
  res += ')'  → res = "lee(t(c)"

Index 8: 'o'
  stk[0] = 12, i = 8
  8 == 12? NO
  res += 'o'  → res = "lee(t(c)o"

Index 9: ')'
  stk[0] = 12, i = 9
  9 == 12? NO
  res += ')'  → res = "lee(t(c)o)"

Index 10: 'd'
  stk[0] = 12, i = 10
  10 == 12? NO
  res += 'd'  → res = "lee(t(c)o)d"

Index 11: 'e'
  stk[0] = 12, i = 11
  11 == 12? NO
  res += 'e'  → res = "lee(t(c)o)de"

Index 12: ')'
  stk[0] = 12, i = 12
  12 == 12? YES ✅
  stk.popleft()  → stk = []
  Skip this character (don't add to result)
```

**Result**: `"lee(t(c)o)de"` ✅

**Visual:**
```
Original: "lee(t(c)o)de)"
          l e e ( t ( c ) o ) d e )
Indices:  0 1 2 3 4 5 6 7 8 9 0 1 2
                             1 1 1
Remove:                      ↑
                            index 12
Result:   "lee(t(c)o)de"
```

---

## Detailed Example 2: Multiple Unmatched

**Input**: `s = "a)b(c)d"`

### Step-by-Step Execution

#### First Pass

```
Index 0: 'a' → skip, stk = []
Index 1: ')' → stk empty, push 1, stk = [1]
Index 2: 'b' → skip, stk = [1]
Index 3: '(' → push 3, stk = [1, 3]
Index 4: 'c' → skip, stk = [1, 3]
Index 5: ')' → match with stk[-1]=3, pop, stk = [1]
Index 6: 'd' → skip, stk = [1]
```

**After First Pass:**
```
stk = [1]  (unmatched ')' at index 1)
```

#### Second Pass

```
Index 0: 'a' → add, res = "a"
Index 1: ')' → in stk, skip, stk = []
Index 2: 'b' → add, res = "ab"
Index 3: '(' → add, res = "ab("
Index 4: 'c' → add, res = "ab(c"
Index 5: ')' → add, res = "ab(c)"
Index 6: 'd' → add, res = "ab(c)d"
```

**Result**: `"ab(c)d"` ✅

---

## Detailed Example 3: All Unmatched

**Input**: `s = "))(("`

### Step-by-Step Execution

#### First Pass

```
Index 0: ')' → stk empty, push 0, stk = [0]
Index 1: ')' → stk[-1]=0, s[0]=')', not '(', push 1, stk = [0, 1]
Index 2: '(' → push 2, stk = [0, 1, 2]
Index 3: '(' → push 3, stk = [0, 1, 2, 3]
```

**After First Pass:**
```
stk = [0, 1, 2, 3]  (all unmatched)
```

#### Second Pass

```
Index 0: ')' → in stk, skip, stk = [1, 2, 3]
Index 1: ')' → in stk, skip, stk = [2, 3]
Index 2: '(' → in stk, skip, stk = [3]
Index 3: '(' → in stk, skip, stk = []
```

**Result**: `""` ✅ (empty string, all parentheses removed)

---

## Detailed Example 4: Unmatched Opening

**Input**: `s = "(a(b(c)d)"`

### Step-by-Step Execution

#### First Pass

```
Index 0: '(' → push 0, stk = [0]
Index 1: 'a' → skip, stk = [0]
Index 2: '(' → push 2, stk = [0, 2]
Index 3: 'b' → skip, stk = [0, 2]
Index 4: '(' → push 4, stk = [0, 2, 4]
Index 5: 'c' → skip, stk = [0, 2, 4]
Index 6: ')' → match with stk[-1]=4, pop, stk = [0, 2]
Index 7: 'd' → skip, stk = [0, 2]
Index 8: ')' → match with stk[-1]=2, pop, stk = [0]
```

**After First Pass:**
```
stk = [0]  (unmatched '(' at index 0)
```

#### Second Pass

```
Index 0: '(' → in stk, skip, stk = []
Index 1: 'a' → add, res = "a"
Index 2: '(' → add, res = "a("
Index 3: 'b' → add, res = "a(b"
Index 4: '(' → add, res = "a(b("
Index 5: 'c' → add, res = "a(b(c"
Index 6: ')' → add, res = "a(b(c)"
Index 7: 'd' → add, res = "a(b(c)d"
Index 8: ')' → add, res = "a(b(c)d)"
```

**Result**: `"a(b(c)d)"` ✅

---

## Key Concepts

### 1. Stack for Parentheses Matching

**Why Stack?**
- Last-in-first-out (LIFO) matches nested parentheses
- Opening parentheses are pushed
- Closing parentheses pop matching opening ones
- Unmatched parentheses remain in stack

**Example:**
```
String: "(()"
Stack operations:
  '(' → push
  '(' → push
  ')' → pop (matches last '(')
Result: stack has one unmatched '('
```

### 2. Two-Pass Algorithm

**First Pass: Identify Unmatched**
- Process string left to right
- Track indices of unmatched parentheses in stack
- Matched pairs are removed from stack

**Second Pass: Build Result**
- Iterate through string indices
- Skip indices in stack (unmatched)
- Add all other characters

### 3. Why Store Indices?

**Store indices, not characters:**
- Need to know which positions to remove
- Indices allow efficient removal in second pass
- Can handle duplicate characters correctly

**Example:**
```
String: "))"
If we stored characters: stack = [')', ')']
But we need to know positions: stack = [0, 1]
```

### 4. Matching Logic

**For Closing Parenthesis:**
```python
if stk and s[stk[-1]] == '(':
    stk.pop()  # Matched pair, remove both
else:
    stk.append(i)  # Unmatched, mark for removal
```

**Why check `s[stk[-1]] == '('`?**
- Stack might have unmatched ')' from earlier
- Only match with opening '('
- Ensures correct pairing

### 5. Building Result Efficiently

**Why not use list and join?**
- Current approach builds string character by character
- Could use list and join for better performance
- But current approach is clear and correct

**Alternative:**
```python
result = []
for i in range(len(s)):
    if stk and i == stk[0]:
        stk.popleft()
    else:
        result.append(s[i])
return ''.join(result)
```

---

## Algorithm Pseudocode

```python
def minRemoveToMakeValid(s):
    # Step 1: Initialize stack for unmatched parentheses indices
    stack = deque()
    
    # Step 2: First pass - identify unmatched parentheses
    for i, char in enumerate(s):
        if char == '(':
            # Opening parenthesis: push index
            stack.append(i)
        elif char == ')':
            # Closing parenthesis: try to match
            if stack and s[stack[-1]] == '(':
                # Found matching opening: pop it
                stack.pop()
            else:
                # No matching opening: mark for removal
                stack.append(i)
    
    # Step 3: Second pass - build result, skipping unmatched indices
    result = ""
    for i in range(len(s)):
        if stack and i == stack[0]:
            # This index is unmatched: skip it
            stack.popleft()
        else:
            # Valid character: add to result
            result += s[i]
    
    return result
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(N) | N = string length. Two passes, each O(N) |
| **Space** | O(N) | Stack stores at most N indices (worst case: all unmatched) |

**Where:**
- N = length of input string

**Time Complexity:**
- First pass: O(N) - process each character once
- Second pass: O(N) - iterate through indices once
- Total: O(N)

**Space Complexity:**
- Stack: O(N) in worst case (all parentheses unmatched)
- Result string: O(N)
- Total: O(N)

---

## Edge Cases

### Case 1: Empty String
```
s = ""
Result: "" ✅
```

### Case 2: No Parentheses
```
s = "abc"
Result: "abc" ✅
```

### Case 3: All Unmatched
```
s = "))(("
Result: "" ✅
```

### Case 4: Already Valid
```
s = "()"
Result: "()" ✅
```

### Case 5: Nested Valid
```
s = "((()))"
Result: "((()))" ✅
```

### Case 6: Mixed Characters
```
s = "a(b)c)d(e"
Result: "a(b)cd(e" or "a(bc)d(e" (multiple valid solutions)
```

---

## Why This Algorithm Works

### Correctness

1. **Identifies All Unmatched:**
   - Stack tracks unmatched opening parentheses
   - Unmatched closing parentheses are added to stack
   - After first pass, stack contains all unmatched indices

2. **Removes Minimum:**
   - Only removes unmatched parentheses
   - Keeps all matched pairs
   - No unnecessary removals

3. **Maintains Order:**
   - Processes left to right
   - Preserves character order
   - Only removes unmatched parentheses

### Why Stack Works

**Stack Properties:**
- LIFO matches nested parentheses naturally
- Last opening parenthesis matches first closing one
- Perfect for parentheses matching

**Example:**
```
"(()())"
Stack trace:
  '(' → push
  '(' → push
  ')' → pop (matches second '(')
  '(' → push
  ')' → pop (matches third '(')
  ')' → pop (matches first '(')
All matched!
```

---

## Alternative Approaches

### 1. Two-Pass with Counters

**Idea**: Count opening and closing parentheses

```python
def minRemoveToMakeValid(s):
    # First pass: remove extra ')'
    first_pass = []
    open_count = 0
    for char in s:
        if char == '(':
            open_count += 1
            first_pass.append(char)
        elif char == ')':
            if open_count > 0:
                open_count -= 1
                first_pass.append(char)
            # else: skip this ')'
        else:
            first_pass.append(char)
    
    # Second pass: remove extra '(' from right
    result = []
    close_count = 0
    for char in reversed(first_pass):
        if char == ')':
            close_count += 1
            result.append(char)
        elif char == '(':
            if close_count > 0:
                close_count -= 1
                result.append(char)
            # else: skip this '('
        else:
            result.append(char)
    
    return ''.join(reversed(result))
```

**Pros:** No stack needed
**Cons:** More complex, two passes with reversal

### 2. Set-Based Approach

**Idea**: Use set to track indices to remove

```python
def minRemoveToMakeValid(s):
    stack = []
    to_remove = set()
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)
    
    to_remove.update(stack)  # Add unmatched opening
    
    return ''.join(char for i, char in enumerate(s) if i not in to_remove)
```

**Pros:** Clear logic
**Cons:** Uses set (more memory)

---

## Visual Timeline

### Example: `"lee(t(c)o)de)"`

```
Step | Index | Char | Stack State        | Action
-----|-------|------|-------------------|------------------
1    | 0     | 'l'  | []                | Skip
2    | 1     | 'e' | []                 | Skip
3    | 2     | 'e' | []                 | Skip
4    | 3     | '('  | [3]               | Push 3
5    | 4     | 't'  | [3]               | Skip
6    | 5     | '('  | [3, 5]            | Push 5
7    | 6     | 'c'  | [3, 5]            | Skip
8    | 7     | ')'  | [3]               | Pop (match)
9    | 8     | 'o'  | [3]               | Skip
10   | 9     | ')'  | []                | Pop (match)
11   | 10    | 'd'  | []                | Skip
12   | 11    | 'e'  | []                | Skip
13   | 12    | ')'  | [12]              | Push 12 (unmatched)

Result: Remove index 12 → "lee(t(c)o)de"
```

---

## Real-World Applications

1. **Code Parsing:**
   - Remove invalid parentheses from code
   - Syntax error correction

2. **Expression Evaluation:**
   - Validate mathematical expressions
   - Fix malformed expressions

3. **Text Processing:**
   - Clean up user input
   - Format validation

4. **Compiler Design:**
   - Syntax analysis
   - Error recovery

---

## Common Mistakes

### Mistake 1: Not Checking Stack Before Pop

```python
# WRONG: May pop from empty stack
if s[stk[-1]] == '(':
    stk.pop()
```

**Fix:** Check `if stk and s[stk[-1]] == '(':`

### Mistake 2: Storing Characters Instead of Indices

```python
# WRONG: Can't identify positions
if ch == '(':
    stk.append('(')
```

**Fix:** Store indices: `stk.append(i)`

### Mistake 3: Not Handling Unmatched Closing

```python
# WRONG: Only handles unmatched opening
if ch == ')':
    if stk:
        stk.pop()
    # Missing: else case to mark unmatched
```

**Fix:** Add `else: stk.append(i)` for unmatched closing

### Mistake 4: Wrong Comparison in Second Pass

```python
# WRONG: Comparing with wrong element
if i in stk:  # O(N) lookup
```

**Fix:** Use `if stk and i == stk[0]:` with popleft

---

## Summary

The minimum remove parentheses algorithm:
- Uses **stack** to track unmatched parentheses indices
- **First pass**: Identifies all unmatched parentheses
- **Second pass**: Builds result by skipping unmatched indices
- Time complexity: **O(N)**
- Space complexity: **O(N)**

**Key Insight**: Use a stack to match parentheses. Unmatched parentheses remain in the stack, and we remove characters at those indices to get a valid string.

---

## Related Problems

- **LeetCode 1249**: Minimum Remove to Make Valid Parentheses (this problem)
- **LeetCode 20**: Valid Parentheses (check if valid)
- **LeetCode 22**: Generate Parentheses (generate valid combinations)
- **LeetCode 32**: Longest Valid Parentheses (find longest valid substring)
- **LeetCode 301**: Remove Invalid Parentheses (remove minimum to make valid - all solutions)

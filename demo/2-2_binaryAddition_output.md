# Binary Addition

> **LeetCode 67**: Given two binary strings `a` and `b`, return their sum as a binary string.

## Problem Description

Add two binary numbers represented as strings and return the result as a binary string.

**Rules:**
- Binary addition: 0 + 0 = 0, 0 + 1 = 1, 1 + 1 = 10 (0 with carry 1)
- Process digits from right to left (least significant to most significant)
- Handle carry propagation
- Handle different length inputs

**Example:**
- `a = "11"`, `b = "1"`
- Result: `"100"` (3 + 1 = 4 in binary)

---

## Key Insight

**Simulate Manual Addition:**
- Start from rightmost digits (least significant)
- Add corresponding digits plus carry
- Current digit = sum % 2
- New carry = sum // 2
- Continue until all digits processed
- Add final carry if non-zero

**Negative Indexing:**
- Use Python's negative indexing to traverse from right to left
- `a[-1]` = last character, `a[-2]` = second last, etc.
- Handles different length strings elegantly

---

## Algorithm Logic

```
1. Initialize:
   - carry = 0
   - result = []
   - max_length = max(len(a), len(b))

2. For each position from right to left:
   a. Get digit from a (or 0 if out of bounds)
   b. Get digit from b (or 0 if out of bounds)
   c. Calculate: sum = digit_a + digit_b + carry
   d. Current result digit = sum % 2
   e. New carry = sum // 2
   f. Add result digit to front of result

3. If carry != 0:
   - Add carry to front of result

4. Return result as string
```

---

## Detailed Example 1: Step-by-Step

**Input**: `a = "11"`, `b = "1"`

### Visual Representation

```
Binary Addition:
   1 1    (3 in decimal)
+    1    (1 in decimal)
-------
 1 0 0    (4 in decimal)
```

### Step-by-Step Execution

#### Step 1: Initialize

```
a = "11"
b = "1"

len_a = 2
len_b = 1
max_length = max(2, 1) = 2
carry = 0
new_str = []
```

#### Step 2: Iteration 1 (Rightmost Position, i = -1)

```
i = -1

Get digits:
  element_a = int(a[-1]) = int("1") = 1  (i = -1 >= -len_a = -2? YES)
  element_b = int(b[-1]) = int("1") = 1  (i = -1 >= -len_b = -1? YES)

Calculate sum:
  add = element_a + element_b + carry
      = 1 + 1 + 0
      = 2

Calculate result digit and carry:
  value = add % 2 = 2 % 2 = 0
  carry = add // 2 = 2 // 2 = 1

Update result:
  new_str.insert(0, "0")  → new_str = ["0"]
```

**After Iteration 1:**
```
new_str = ["0"]
carry = 1
```

#### Step 3: Iteration 2 (Second Position, i = -2)

```
i = -2

Get digits:
  element_a = int(a[-2]) = int("1") = 1  (i = -2 >= -len_a = -2? YES)
  element_b = 0  (i = -2 >= -len_b = -1? NO, so use 0)

Calculate sum:
  add = element_a + element_b + carry
      = 1 + 0 + 1
      = 2

Calculate result digit and carry:
  value = add % 2 = 2 % 2 = 0
  carry = add // 2 = 2 // 2 = 1

Update result:
  new_str.insert(0, "0")  → new_str = ["0", "0"]
```

**After Iteration 2:**
```
new_str = ["0", "0"]
carry = 1
```

#### Step 4: Handle Final Carry

```
carry = 1 (non-zero)

Add carry to front:
  new_str.insert(0, "1")  → new_str = ["1", "0", "0"]
```

#### Step 5: Return Result

```
return ''.join(new_str) = "100"
```

**Result**: `"100"` ✅

**Verification**: 3 (binary "11") + 1 (binary "1") = 4 (binary "100")

---

## Detailed Example 2: Multiple Carries

**Input**: `a = "1010"`, `b = "1011"`

### Visual Representation

```
Binary Addition:
  1 0 1 0    (10 in decimal)
+ 1 0 1 1    (11 in decimal)
----------
1 0 1 0 1    (21 in decimal)
```

### Step-by-Step Execution

#### Step 1: Initialize

```
a = "1010"
b = "1011"

len_a = 4
len_b = 4
max_length = 4
carry = 0
new_str = []
```

#### Step 2: Iteration 1 (i = -1, rightmost)

```
i = -1

element_a = int(a[-1]) = int("0") = 0
element_b = int(b[-1]) = int("1") = 1

add = 0 + 1 + 0 = 1
value = 1 % 2 = 1
carry = 1 // 2 = 0

new_str = ["1"]
```

#### Step 3: Iteration 2 (i = -2)

```
i = -2

element_a = int(a[-2]) = int("1") = 1
element_b = int(b[-2]) = int("1") = 1

add = 1 + 1 + 0 = 2
value = 2 % 2 = 0
carry = 2 // 2 = 1

new_str = ["0", "1"]
```

#### Step 4: Iteration 3 (i = -3)

```
i = -3

element_a = int(a[-3]) = int("0") = 0
element_b = int(b[-3]) = int("0") = 0

add = 0 + 0 + 1 = 1  (carry from previous)
value = 1 % 2 = 1
carry = 1 // 2 = 0

new_str = ["1", "0", "1"]
```

#### Step 5: Iteration 4 (i = -4, leftmost)

```
i = -4

element_a = int(a[-4]) = int("1") = 1
element_b = int(b[-4]) = int("1") = 1

add = 1 + 1 + 0 = 2
value = 2 % 2 = 0
carry = 2 // 2 = 1

new_str = ["0", "1", "0", "1"]
```

#### Step 6: Handle Final Carry

```
carry = 1

new_str.insert(0, "1")  → new_str = ["1", "0", "1", "0", "1"]
```

**Result**: `"10101"` ✅

**Verification**: 10 + 11 = 21 in decimal, "10101" in binary

---

## Detailed Example 3: Different Lengths

**Input**: `a = "111"`, `b = "10"`

### Step-by-Step Execution

#### Initialize

```
a = "111"  (7 in decimal)
b = "10"   (2 in decimal)

len_a = 3
len_b = 2
max_length = 3
carry = 0
new_str = []
```

#### Iteration 1 (i = -1)

```
i = -1

element_a = int(a[-1]) = 1
element_b = int(b[-1]) = 0

add = 1 + 0 + 0 = 1
value = 1 % 2 = 1
carry = 1 // 2 = 0

new_str = ["1"]
```

#### Iteration 2 (i = -2)

```
i = -2

element_a = int(a[-2]) = 1
element_b = int(b[-2]) = 1

add = 1 + 1 + 0 = 2
value = 2 % 2 = 0
carry = 2 // 2 = 1

new_str = ["0", "1"]
```

#### Iteration 3 (i = -3)

```
i = -3

element_a = int(a[-3]) = 1
element_b = 0  (i = -3 >= -len_b = -2? NO, so 0)

add = 1 + 0 + 1 = 2  (carry from previous)
value = 2 % 2 = 0
carry = 2 // 2 = 1

new_str = ["0", "0", "1"]
```

#### Handle Final Carry

```
carry = 1

new_str.insert(0, "1")  → new_str = ["1", "0", "0", "1"]
```

**Result**: `"1001"` ✅

**Verification**: 7 + 2 = 9 in decimal, "1001" in binary

---

## Key Concepts

### 1. Negative Indexing in Python

**Python Negative Indices:**
- `a[-1]` = last element
- `a[-2]` = second last element
- `a[-n]` = nth element from the end

**Example:**
```python
a = "1010"
a[-1] = "0"  (rightmost)
a[-2] = "1"
a[-3] = "0"
a[-4] = "1"  (leftmost)
```

**Why Use Negative Indexing?**
- Natural for right-to-left traversal
- Handles different length strings elegantly
- No need to reverse strings

### 2. Bounds Checking

**Condition**: `i >= -len_a`

**How it works:**
- For string of length `n`, valid indices are `-1` to `-n`
- `i >= -len_a` checks if index is within bounds
- If out of bounds, use 0 (no digit at that position)

**Example:**
```python
a = "11"  (len_a = 2)
i = -1: -1 >= -2? YES → a[-1] = "1"
i = -2: -2 >= -2? YES → a[-2] = "1"
i = -3: -3 >= -2? NO → use 0
```

### 3. Binary Addition Rules

**Single Bit Addition:**
```
0 + 0 = 0  (carry 0)
0 + 1 = 1  (carry 0)
1 + 0 = 1  (carry 0)
1 + 1 = 0  (carry 1)
1 + 1 + 1 = 1  (carry 1)  (with previous carry)
```

**Mathematical:**
```
sum = a + b + carry
result_digit = sum % 2
new_carry = sum // 2
```

### 4. Carry Propagation

**How Carry Works:**
- When sum ≥ 2, we have a carry
- Carry propagates to next (left) position
- Final carry becomes most significant bit if non-zero

**Example:**
```
  1 1 1
+   1 0
------
1 0 0 1

Step by step:
  Position 0: 1 + 0 = 1, carry 0
  Position 1: 1 + 1 = 0, carry 1
  Position 2: 1 + 0 + 1 = 0, carry 1
  Position 3: 0 + 0 + 1 = 1, carry 0
```

### 5. Building Result from Right to Left

**Why insert at front?**
- We process from right to left
- But result should be left to right
- `insert(0, value)` adds to front, building result correctly

**Alternative:**
- Could append to end, then reverse
- But `insert(0, ...)` is more direct

---

## Algorithm Pseudocode

```python
def addBinary(a, b):
    len_a = len(a)
    len_b = len(b)
    max_length = max(len_a, len_b)
    carry = 0
    result = []
    
    # Process from right to left
    for i in range(-1, -max_length - 1, -1):
        # Get digits (or 0 if out of bounds)
        digit_a = int(a[i]) if i >= -len_a else 0
        digit_b = int(b[i]) if i >= -len_b else 0
        
        # Calculate sum
        total = digit_a + digit_b + carry
        
        # Current digit and new carry
        result_digit = total % 2
        carry = total // 2
        
        # Add to front of result
        result.insert(0, str(result_digit))
    
    # Handle final carry
    if carry != 0:
        result.insert(0, str(carry))
    
    return ''.join(result)
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(N) | N = max(len(a), len(b)). Process each position once |
| **Space** | O(N) | Result list stores N+1 digits in worst case |

**Where:**
- N = maximum length of input strings

**Time Complexity:**
- Loop runs N times (max_length)
- Each iteration: O(1) operations
- `insert(0, ...)` is O(N) in worst case, but we do it N times
- Total: O(N²) worst case due to `insert(0, ...)`

**Optimization Note:**
- Using `insert(0, ...)` is O(N) per call
- Better: append to end, reverse at end → O(N) total
- But current implementation is simpler and acceptable for small inputs

**Space Complexity:**
- Result list: O(N+1) in worst case (with final carry)
- Other variables: O(1)
- Total: O(N)

---

## Edge Cases

### Case 1: Different Lengths
```
a = "111"
b = "10"
Result: "1001" ✅
```

### Case 2: Both Zeros
```
a = "0"
b = "0"
Result: "0" ✅
```

### Case 3: One Zero
```
a = "0"
b = "1"
Result: "1" ✅
```

### Case 4: Final Carry
```
a = "11"
b = "1"
Result: "100" ✅ (carry propagates to new digit)
```

### Case 5: No Carry
```
a = "110"
b = "001"
Result: "111" ✅
```

### Case 6: Multiple Carries
```
a = "1111"
b = "1111"
Result: "11110" ✅
```

---

## Why This Algorithm Works

### Correctness

1. **Simulates Manual Addition:**
   - Processes digits from right to left (least to most significant)
   - Handles carry correctly at each step
   - Matches how humans add binary numbers

2. **Handles Different Lengths:**
   - Uses bounds checking to handle shorter strings
   - Missing digits treated as 0
   - Works for any length combination

3. **Carry Propagation:**
   - Carry correctly propagates to next position
   - Final carry handled separately
   - Ensures correct result

### Why Right to Left?

**Binary numbers are right-aligned:**
```
  1 0 1 0
+   1 0 1
---------
```

- Least significant digits align on the right
- Must process from right to left to handle carries correctly
- Carries propagate leftward

### Why Negative Indexing?

**Advantages:**
- Natural for right-to-left traversal
- No need to reverse strings
- Clean bounds checking
- Handles different lengths elegantly

---

## Alternative Approaches

### 1. Convert to Integer, Add, Convert Back

```python
def addBinary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]
```

**Pros:** Very simple
**Cons:** May overflow for very large numbers (Python handles this, but not in other languages)

### 2. Reverse Strings First

```python
def addBinary(a, b):
    a = a[::-1]
    b = b[::-1]
    # Process from left to right (now reversed)
    # Reverse result at end
```

**Pros:** More intuitive indexing
**Cons:** Extra reversals

### 3. Pad Shorter String

```python
def addBinary(a, b):
    # Pad shorter string with zeros
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    # Process normally
```

**Pros:** Simpler bounds checking
**Cons:** Extra padding step

---

## Common Mistakes

### Mistake 1: Wrong Index Direction

```python
# WRONG: Left to right
for i in range(len(a)):
    digit_a = int(a[i])
```

**Fix:** Use negative indexing or reverse first

### Mistake 2: Forgetting Final Carry

```python
# WRONG: Doesn't handle final carry
return ''.join(new_str)  # Missing: if carry != 0
```

**Fix:** Check and add final carry

### Mistake 3: Incorrect Bounds Check

```python
# WRONG: Doesn't handle out of bounds
element_a = int(a[i])  # IndexError if i out of bounds
```

**Fix:** Use conditional: `int(a[i]) if i >= -len_a else 0`

### Mistake 4: Wrong Carry Calculation

```python
# WRONG: Incorrect carry
carry = add - 2  # Should be add // 2
```

**Fix:** Use `carry = add // 2`

---

## Real-World Applications

1. **Computer Arithmetic:**
   - CPU binary addition
   - ALU operations

2. **Cryptography:**
   - Binary operations in encryption
   - Hash functions

3. **Network Protocols:**
   - Checksum calculations
   - Error detection

4. **Digital Signal Processing:**
   - Binary arithmetic operations
   - Bit manipulation

---

## Summary

The binary addition algorithm:
- Uses **right-to-left traversal** with negative indexing
- Handles **carry propagation** correctly
- Works with **different length inputs** using bounds checking
- Time complexity: **O(N)** where N = max length
- Space complexity: **O(N)** for result

**Key Insight**: Simulate manual binary addition by processing digits from right to left, handling carries at each step. Negative indexing makes this elegant in Python.

---

## Related Problems

- **LeetCode 67**: Add Binary (this problem)
- **LeetCode 2**: Add Two Numbers (linked list addition, similar concept)
- **LeetCode 415**: Add Strings (decimal addition, similar approach)
- **Binary Arithmetic**: Various binary operation problems

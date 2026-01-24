# Find All Anagrams in a String

> **LeetCode 438**: Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`.

## Problem Description

Find all starting positions where an anagram of string `p` appears in string `s`.

**Anagram**: A word formed by rearranging the letters of another word. For example, "abc" and "cba" are anagrams.

**Example:**
- `s = "cbaebabacd"`, `p = "abc"`
- Answer: `[0, 6]` (anagrams found at indices 0 and 6)

---

## Key Insight

Use a **sliding window** of fixed size (length of `p`) and compare character frequencies:
- Maintain a window of size `len(p)` in `s`
- Use `Counter` to track character frequencies
- If frequencies match → found an anagram!

**Strategy**: Slide a fixed-size window through `s`, maintaining character counts.

---

## Algorithm Logic

```
1. Initialize:
   - p_counter = Counter(p)  (target frequencies)
   - s_counter = Counter()   (sliding window frequencies)
   - left = 0                 (window start)
   - ans = []                 (result list)

2. For each position i in s:
   a. Add s[i] to s_counter (expand window)
   b. If window size == len(p):
      * Compare s_counter == p_counter
      * If equal → add left to ans
      * Remove s[left] from s_counter (shrink window)
      * Move left pointer

3. Return ans
```

---

## Detailed Example: Step-by-Step

**Input**: `s = "cbaebabacd"`, `p = "abc"`

### Initial Setup

```
s = "cbaebabacd"
p = "abc"

p_counter = Counter({'a': 1, 'b': 1, 'c': 1})
s_counter = Counter()  (empty)
left = 0
ans = []
np = len(p) = 3
```

### Visual Representation

```
String s:  c  b  a  e  b  a  b  a  c  d
Index:      0  1  2  3  4  5  6  7  8  9

Target p: "abc" → Counter({'a': 1, 'b': 1, 'c': 1})

We need to find all substrings of length 3 that have:
- 1 'a', 1 'b', 1 'c' (in any order)
```

### Step-by-Step Execution

| Step | i | s[i] | Window | s_counter | Window Size | Match? | Action | ans |
|------|---|------|--------|-----------|-------------|--------|--------|-----|
| 0 | 0 | 'c' | `[c]` | `{'c':1}` | 1 | No | Expand | `[]` |
| 1 | 1 | 'b' | `[c,b]` | `{'c':1,'b':1}` | 2 | No | Expand | `[]` |
| 2 | 2 | 'a' | `[c,b,a]` | `{'c':1,'b':1,'a':1}` | 3 | Yes | Shrink | `[0]` |
| 3 | 3 | 'e' | `[b,a,e]` | `{'b':1,'a':1,'e':1}` | 3 | No | Shrink | `[0]` |
| 4 | 4 | 'b' | `[a,e,b]` | `{'a':1,'e':1,'b':1}` | 3 | No | Shrink | `[0]` |
| 5 | 5 | 'a' | `[e,b,a]` | `{'e':1,'b':1,'a':1}` | 3 | No | Shrink | `[0]` |
| 6 | 6 | 'b' | `[b,a,b]` | `{'b':2,'a':1}` | 3 | No | Shrink | `[0]` |
| 7 | 7 | 'a' | `[a,b,a]` | `{'a':2,'b':1}` | 3 | No | Shrink | `[0]` |
| 8 | 8 | 'c' | `[b,a,c]` | `{'b':1,'a':1,'c':1}` | 3 | Yes | Shrink | `[0,6]` |
| 9 | 9 | 'd' | `[a,c,d]` | `{'a':1,'c':1,'d':1}` | 3 | No | Shrink | `[0,6]` |

**Final Result**: `[0, 6]` ✅

---

## Detailed Step Breakdown

### Step 0: i = 0, s[0] = 'c'

```
Add 'c' to window:
  s_counter['c'] += 1
  s_counter = {'c': 1}

Window: [c] (indices 0-0)
Window size = 0 - 0 + 1 = 1 < 3 (np)
Not full window yet → continue
```

**Visualization:**
```
s:  c  b  a  e  b  a  b  a  c  d
    [─]                          Window size: 1
    l=i
```

### Step 1: i = 1, s[1] = 'b'

```
Add 'b' to window:
  s_counter['b'] += 1
  s_counter = {'c': 1, 'b': 1}

Window: [c, b] (indices 0-1)
Window size = 1 - 0 + 1 = 2 < 3
Not full window yet → continue
```

**Visualization:**
```
s:  c  b  a  e  b  a  b  a  c  d
    [───]                        Window size: 2
    l   i
```

### Step 2: i = 2, s[2] = 'a' ✅ **FIRST MATCH!**

```
Add 'a' to window:
  s_counter['a'] += 1
  s_counter = {'c': 1, 'b': 1, 'a': 1}

Window: [c, b, a] (indices 0-2)
Window size = 2 - 0 + 1 = 3 == np ✅

Check if anagram:
  s_counter = {'c': 1, 'b': 1, 'a': 1}
  p_counter = {'a': 1, 'b': 1, 'c': 1}
  s_counter == p_counter? YES! ✅
  
  Add left (0) to ans: ans = [0]

Shrink window:
  s_counter['c'] = 1 → delete it
  s_counter = {'b': 1, 'a': 1}
  left = 0 + 1 = 1
```

**Visualization:**
```
s:  c  b  a  e  b  a  b  a  c  d
    [─────]                      Window: "cba"
    l     i                      Match! → ans = [0]
    
After shrink:
    [─────]                      Window: "bae" (next iteration)
     l    i
```

**Why it's an anagram**: "cba" contains 1 'a', 1 'b', 1 'c' → same as "abc"!

### Step 3: i = 3, s[3] = 'e'

```
Add 'e' to window:
  s_counter['e'] += 1
  s_counter = {'b': 1, 'a': 1, 'e': 1}

Window: [b, a, e] (indices 1-3)
Window size = 3 - 1 + 1 = 3 == np ✅

Check if anagram:
  s_counter = {'b': 1, 'a': 1, 'e': 1}
  p_counter = {'a': 1, 'b': 1, 'c': 1}
  s_counter == p_counter? NO (has 'e' instead of 'c')

Shrink window:
  s_counter['b'] = 1 → delete it
  s_counter = {'a': 1, 'e': 1}
  left = 1 + 1 = 2
```

**Visualization:**
```
s:  c  b  a  e  b  a  b  a  c  d
       [─────]                    Window: "bae"
       l     i                    No match
```

### Step 4: i = 4, s[4] = 'b'

```
Add 'b' to window:
  s_counter['b'] += 1
  s_counter = {'a': 1, 'e': 1, 'b': 1}

Window: [a, e, b] (indices 2-4)
Window size = 3 ✅

Check if anagram:
  s_counter = {'a': 1, 'e': 1, 'b': 1}
  p_counter = {'a': 1, 'b': 1, 'c': 1}
  s_counter == p_counter? NO (has 'e' instead of 'c')

Shrink window:
  s_counter['a'] = 1 → delete it
  s_counter = {'e': 1, 'b': 1}
  left = 2 + 1 = 3
```

### Step 5: i = 5, s[5] = 'a'

```
Add 'a' to window:
  s_counter['a'] += 1
  s_counter = {'e': 1, 'b': 1, 'a': 1}

Window: [e, b, a] (indices 3-5)
Window size = 3 ✅

Check if anagram:
  s_counter = {'e': 1, 'b': 1, 'a': 1}
  p_counter = {'a': 1, 'b': 1, 'c': 1}
  s_counter == p_counter? NO (has 'e' instead of 'c')

Shrink window:
  s_counter['e'] = 1 → delete it
  s_counter = {'b': 1, 'a': 1}
  left = 3 + 1 = 4
```

### Step 6: i = 6, s[6] = 'b'

```
Add 'b' to window:
  s_counter['b'] += 1
  s_counter = {'b': 2, 'a': 1}

Window: [b, a, b] (indices 4-6)
Window size = 3 ✅

Check if anagram:
  s_counter = {'b': 2, 'a': 1}
  p_counter = {'a': 1, 'b': 1, 'c': 1}
  s_counter == p_counter? NO (has 2 'b's, missing 'c')

Shrink window:
  s_counter['b'] = 2 → decrement to 1
  s_counter = {'b': 1, 'a': 1}
  left = 4 + 1 = 5
```

### Step 7: i = 7, s[7] = 'a'

```
Add 'a' to window:
  s_counter['a'] += 1
  s_counter = {'b': 1, 'a': 2}

Window: [a, b, a] (indices 5-7)
Window size = 3 ✅

Check if anagram:
  s_counter = {'b': 1, 'a': 2}
  p_counter = {'a': 1, 'b': 1, 'c': 1}
  s_counter == p_counter? NO (has 2 'a's, missing 'c')

Shrink window:
  s_counter['a'] = 2 → decrement to 1
  s_counter = {'b': 1, 'a': 1}
  left = 5 + 1 = 6
```

### Step 8: i = 8, s[8] = 'c' ✅ **SECOND MATCH!**

```
Add 'c' to window:
  s_counter['c'] += 1
  s_counter = {'b': 1, 'a': 1, 'c': 1}

Window: [b, a, c] (indices 6-8)
Window size = 3 ✅

Check if anagram:
  s_counter = {'b': 1, 'a': 1, 'c': 1}
  p_counter = {'a': 1, 'b': 1, 'c': 1}
  s_counter == p_counter? YES! ✅
  
  Add left (6) to ans: ans = [0, 6]

Shrink window:
  s_counter['b'] = 1 → delete it
  s_counter = {'a': 1, 'c': 1}
  left = 6 + 1 = 7
```

**Visualization:**
```
s:  c  b  a  e  b  a  b  a  c  d
                   [─────]        Window: "bac"
                   l     i       Match! → ans = [0, 6]
```

**Why it's an anagram**: "bac" contains 1 'a', 1 'b', 1 'c' → same as "abc"!

### Step 9: i = 9, s[9] = 'd'

```
Add 'd' to window:
  s_counter['d'] += 1
  s_counter = {'a': 1, 'c': 1, 'd': 1}

Window: [a, c, d] (indices 7-9)
Window size = 3 ✅

Check if anagram:
  s_counter = {'a': 1, 'c': 1, 'd': 1}
  p_counter = {'a': 1, 'b': 1, 'c': 1}
  s_counter == p_counter? NO (has 'd' instead of 'b')

Shrink window:
  s_counter['a'] = 1 → delete it
  s_counter = {'c': 1, 'd': 1}
  left = 7 + 1 = 8
```

### Final Result

```
ans = [0, 6]

Anagrams found at:
- Index 0: "cba" is an anagram of "abc"
- Index 6: "bac" is an anagram of "abc"
```

---

## Key Concepts

### 1. Fixed-Size Sliding Window

The window size is **always** `len(p)`:
- When window is smaller → expand (add characters)
- When window reaches size `len(p)` → check for anagram, then slide (remove left, add right)

### 2. Character Frequency Comparison

Two strings are anagrams if they have the **same character frequencies**:
- "abc" → `{'a': 1, 'b': 1, 'c': 1}`
- "cba" → `{'c': 1, 'b': 1, 'a': 1}`
- Same frequencies → anagrams! ✅

### 3. Efficient Counter Management

When removing a character from the window:
- If count == 1 → `del s_counter[char]` (remove key)
- If count > 1 → `s_counter[char] -= 1` (decrement)

This keeps the Counter clean and accurate.

### 4. Why Compare After Window is Full?

We only check for anagrams when `window_size == len(p)`:
- Smaller windows can't be anagrams
- Larger windows would include extra characters
- Fixed-size ensures we're comparing the right length

---

## Visual Timeline

```
String s:  c  b  a  e  b  a  b  a  c  d
Index:      0  1  2  3  4  5  6  7  8  9

Step 2:  [─────]                          "cba" → Match! ✅ (index 0)
         l     i

Step 3:     [─────]                        "bae" → No match
            l     i

Step 4:       [─────]                      "aeb" → No match
              l     i

Step 5:         [─────]                    "eba" → No match
                l     i

Step 6:           [─────]                  "bab" → No match
                  l     i

Step 7:             [─────]                "aba" → No match
                    l     i

Step 8:               [─────]              "bac" → Match! ✅ (index 6)
                      l     i

Step 9:                 [─────]            "acd" → No match
                        l     i
```

---

## Algorithm Pseudocode

```python
def findAnagrams(s, p):
    p_counter = Counter(p)      # Target frequencies
    s_counter = Counter()        # Window frequencies
    ans = []
    left = 0
    
    for i in range(len(s)):
        # Expand window: add s[i]
        s_counter[s[i]] += 1
        
        # Check if window is full
        if i - left + 1 == len(p):
            # Compare frequencies
            if s_counter == p_counter:
                ans.append(left)
            
            # Shrink window: remove s[left]
            if s_counter[s[left]] == 1:
                del s_counter[s[left]]
            else:
                s_counter[s[left]] -= 1
            left += 1
    
    return ans
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(n × m) | n = len(s), m = len(p). For each position, we compare counters (O(m) comparison) |
| **Space** | O(m) | Counter stores at most m distinct characters |

**Note**: Counter comparison is O(m) in worst case (when all characters are distinct).

---

## Edge Cases

### Case 1: No Anagrams
```
s = "af", p = "be"
Result: []
```

### Case 2: Multiple Anagrams
```
s = "abab", p = "ab"
Result: [0, 1, 2]
Explanation: "ab", "ba", "ab" are all anagrams
```

### Case 3: Single Character
```
s = "baa", p = "aa"
Result: [1]
Explanation: "aa" at index 1 is an anagram
```

### Case 4: p Longer Than s
```
s = "ab", p = "abc"
Result: []
(No window of size 3 can fit in string of length 2)
```

### Case 5: Identical Strings
```
s = "abc", p = "abc"
Result: [0]
```

---

## Why This Algorithm Works

1. **Fixed Window Size**: Always maintains a window of exactly `len(p)` characters
2. **Frequency Matching**: Two strings are anagrams iff they have the same character frequencies
3. **Sliding Efficiently**: Removes left character and adds right character in O(1) time
4. **Complete Coverage**: Every possible substring of length `len(p)` is checked exactly once

---

## Alternative Approach (Optimization)

We can optimize by tracking the number of matching characters instead of comparing entire counters:

```python
def findAnagrams_optimized(s, p):
    p_count = Counter(p)
    window_count = Counter()
    match_count = 0  # Number of characters with matching frequencies
    ans = []
    left = 0
    
    for right in range(len(s)):
        # Add right character
        window_count[s[right]] += 1
        if window_count[s[right]] == p_count[s[right]]:
            match_count += 1
        
        # Check if window is full
        if right - left + 1 == len(p):
            if match_count == len(p_count):
                ans.append(left)
            
            # Remove left character
            if window_count[s[left]] == p_count[s[left]]:
                match_count -= 1
            window_count[s[left]] -= 1
            if window_count[s[left]] == 0:
                del window_count[s[left]]
            left += 1
    
    return ans
```

This reduces comparison time from O(m) to O(1) per window, giving O(n) time complexity.

---

## Summary

The find anagrams algorithm:
- Uses **fixed-size sliding window** technique
- Maintains **character frequency counters**
- Compares frequencies when window is full
- Time complexity: **O(n × m)** (can be optimized to O(n))
- Space complexity: **O(m)**

**Key Insight**: Anagrams have the same character frequencies. Use a sliding window to check all substrings of length `len(p)`.

---

## Related Problems

- **LeetCode 567**: Permutation in String (similar problem)
- **LeetCode 76**: Minimum Window Substring
- **LeetCode 3**: Longest Substring Without Repeating Characters
- **LeetCode 438**: Find All Anagrams in a String (this problem)

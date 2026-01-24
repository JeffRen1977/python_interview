# Longest Significant Word Chain

> **Problem**: Find the longest word chain where each word in the chain can be formed by removing one character from the previous word (subtraction method) or by adding one character to the previous word (addition method). All words must be in the given dictionary.

## Problem Description

Find the longest chain of words where:
- **Subtraction Method**: Each word can be formed by removing exactly one character from the previous word
- **Addition Method**: Each word can be formed by adding exactly one character to the previous word
- All words must exist in the dictionary

**Example (Subtraction):**
- Chain: "string" → "sting" → "sing" → "sin" → "in" → "i"
- Each word is formed by removing one character from the previous word

**Example (Addition):**
- Chain: "a" → "at" → "sat" → "stat" → "state"
- Each word is formed by adding one character to the previous word

---

## Key Insight

**Two Approaches:**

1. **Subtraction Method**: Start from longer words, remove characters to form shorter words
   - Build chain backwards (longer → shorter)
   - For each word, try removing each character
   - Check if resulting word is in dictionary

2. **Addition Method**: Start from shorter words, add characters to form longer words
   - Build chain forwards (shorter → longer)
   - For each word, try adding each character at each position
   - Check if resulting word is in dictionary

**Memoization**: Cache results to avoid recalculating chain lengths for the same word.

---

## Algorithm Logic

### Subtraction Method

```
1. For each word in dictionary:
   a. Call chain_from_sub(word, all_words, 1)
   b. Track maximum chain length

2. chain_from_sub(word, all_words, chain_length):
   a. Check cache: if word processed, return cached result
   b. Try removing each character:
      - For position i: new_word = word[:i] + word[i+1:]
      - If new_word in dictionary:
         - Recursively find chain from new_word
         - Track maximum chain length
   c. Cache and return maximum chain length
```

### Addition Method

```
1. For each word in dictionary:
   a. Call chain_from_add(word, all_words, 1)
   b. Track maximum chain length

2. chain_from_add(word, all_words, chain_length):
   a. Check cache: if word processed, return cached result
   b. Try adding each character at each position:
      - For position i (0 to len(word)):
      - For each letter a-z:
         - new_word = word[:i] + a + word[i:]
         - If new_word in dictionary:
            - Recursively find chain from new_word
            - Track maximum chain length
   c. Cache and return maximum chain length
```

---

## Detailed Example: Subtraction Method

**Input**: `words = ["a", "i", "in", "sin", "sing", "sting", "string"]`

### Word Chain Visualization

```
Chain 1: string → sting → sing → sin → in → i
         (6)     (5)     (4)   (3)  (2) (1)

Chain 2: sing → sin → in → i
         (4)   (3)  (2) (1)
```

### Step-by-Step Execution

#### Step 1: Process "string"

```
Call: chain_from_sub("string", all_words, 1)
cache = {}

Try removing each character:
  Position 0: "tring" (remove 's') → Not in dictionary
  Position 1: "sring" (remove 't') → Not in dictionary
  Position 2: "sting" (remove 'r') → ✅ In dictionary!
    Call: chain_from_sub("sting", all_words, 2)
  
  Position 3: "sting" (remove 'i') → Not in dictionary
  Position 4: "strng" (remove 'i') → Not in dictionary
  Position 5: "strin" (remove 'g') → Not in dictionary
```

#### Step 2: Process "sting" (from "string")

```
Call: chain_from_sub("sting", all_words, 2)
cache = {}  (not cached yet)

Try removing each character:
  Position 0: "ting" → Not in dictionary
  Position 1: "sing" (remove 't') → ✅ In dictionary!
    Call: chain_from_sub("sing", all_words, 3)
  
  Position 2: "stng" → Not in dictionary
  Position 3: "stig" → Not in dictionary
  Position 4: "stin" → Not in dictionary
```

#### Step 3: Process "sing" (from "sting")

```
Call: chain_from_sub("sing", all_words, 3)
cache = {}

Try removing each character:
  Position 0: "ing" → Not in dictionary
  Position 1: "sng" → Not in dictionary
  Position 2: "sin" (remove 'g') → ✅ In dictionary!
    Call: chain_from_sub("sin", all_words, 4)
  
  Position 3: "sin" (remove 'g') → Already found
```

#### Step 4: Process "sin" (from "sing")

```
Call: chain_from_sub("sin", all_words, 4)
cache = {}

Try removing each character:
  Position 0: "in" (remove 's') → ✅ In dictionary!
    Call: chain_from_sub("in", all_words, 5)
  
  Position 1: "sn" → Not in dictionary
  Position 2: "si" → Not in dictionary
```

#### Step 5: Process "in" (from "sin")

```
Call: chain_from_sub("in", all_words, 5)
cache = {}

Try removing each character:
  Position 0: "n" → Not in dictionary
  Position 1: "i" (remove 'n') → ✅ In dictionary!
    Call: chain_from_sub("i", all_words, 6)
```

#### Step 6: Process "i" (from "in")

```
Call: chain_from_sub("i", all_words, 6)
cache = {}

Try removing each character:
  Position 0: "" (remove 'i') → Not in dictionary (empty string)
  
No valid subwords found
max_chain_length = 0
cache["i"] = 0
Return: 0
```

#### Step 7: Backtrack and Calculate

**Back to "in":**
```
max_chain_length = max(0, 0) = 0
cache["in"] = 0
Return: 0
```

**Back to "sin":**
```
max_chain_length = max(0, 0) = 0
cache["sin"] = 0
Return: 0
```

Wait, this doesn't seem right. Let me reconsider the algorithm logic.

Actually, I think there's an issue with the algorithm. Looking at the code more carefully:

```python
max_chain_length = 0
for i in range(len(word)):
    new_word = word[:i] + word[i + 1:]
    if new_word in all_words:
        current_chain_length = self.chain_from_sub(new_word, all_words, chain_length + 1)
        max_chain_length = max(max_chain_length, current_chain_length)
```

The issue is that `max_chain_length` starts at 0, and if no valid subword is found, it returns 0. But the word itself should count as length 1.

Let me trace through more carefully, assuming the word itself counts:

Actually, looking at the return value and how it's used:
- `chain_from_sub` is called with `chain_length=1`
- If no subwords are found, it returns 0
- But the word itself should contribute to the chain

I think the correct interpretation is:
- If a word has no valid subwords, its chain length is 1 (just itself)
- The current implementation returns 0, which seems incorrect

However, let me document it as it is and note this potential issue. Let me recalculate with the understanding that we need to count the word itself:

Actually, let me re-read the code. The `chain_length` parameter is passed but not really used correctly. Let me trace a corrected version:

**Corrected Understanding:**
- The chain length should include the current word
- If no subwords found, return 1 (the word itself)
- Otherwise, return 1 + max chain from subwords

But the code returns `max_chain_length` which starts at 0. This seems like a bug, but I'll document it as is.

Let me create a corrected trace:

---

## Corrected Example: Subtraction Method

**Assumption**: The algorithm should return the chain length including the current word. Let me trace with this understanding:

### Processing "string"

```
chain_from_sub("string", all_words, 1):
  Try removing 'r': "sting" ✅
    Call: chain_from_sub("sting", all_words, 2)
      Try removing 't': "sing" ✅
        Call: chain_from_sub("sing", all_words, 3)
          Try removing 'g': "sin" ✅
            Call: chain_from_sub("sin", all_words, 4)
              Try removing 's': "in" ✅
                Call: chain_from_sub("in", all_words, 5)
                  Try removing 'n': "i" ✅
                    Call: chain_from_sub("i", all_words, 6)
                      No valid subwords
                      Return: 0 (but should be 1?)
                  
                  max_chain_length = max(0, 0) = 0
                  Return: 0
              
              max_chain_length = max(0, 0) = 0
              Return: 0
          
          max_chain_length = max(0, 0) = 0
          Return: 0
      
      max_chain_length = max(0, 0) = 0
      Return: 0
  
  max_chain_length = max(0, 0) = 0
  Return: 0
```

This gives 0, which is clearly wrong. The chain should be length 6.

**I think the issue is**: The algorithm should return the chain length including the current word. Let me document a corrected version:

---

## Corrected Algorithm Logic

The current implementation has a bug: it returns 0 when no subwords are found, but it should return 1 (the word itself counts).

**Corrected version should be:**
```python
def chain_from_sub(self, word: str, all_words: Set[str], chain_length: int) -> int:
    if word in self.cache:
        return self.cache[word]
    
    max_chain_length = 1  # Word itself counts as length 1
    for i in range(len(word)):
        new_word = word[:i] + word[i + 1:]
        if new_word in all_words:
            current_chain_length = 1 + self.chain_from_sub(new_word, all_words, chain_length + 1)
            max_chain_length = max(max_chain_length, current_chain_length)
    
    self.cache[word] = max_chain_length
    return max_chain_length
```

But since I should document the code as it is, let me create the document explaining both the current implementation and the corrected approach.

---

## Detailed Example: Subtraction Method (Corrected Understanding)

**Input**: `words = ["a", "i", "in", "sin", "sing", "sting", "string"]`

### Corrected Trace

#### Processing "i" (Base Case)

```
chain_from_sub("i", all_words, 1):
  Try removing 'i': "" → Not in dictionary
  No valid subwords
  max_chain_length = 1  (word itself)
  cache["i"] = 1
  Return: 1
```

#### Processing "in"

```
chain_from_sub("in", all_words, 1):
  Try removing 'n': "i" ✅
    Call: chain_from_sub("i", all_words, 2)
      Returns: 1 (from cache or base case)
    current_chain_length = 1 + 1 = 2
  
  max_chain_length = max(1, 2) = 2
  cache["in"] = 2
  Return: 2
```

#### Processing "sin"

```
chain_from_sub("sin", all_words, 1):
  Try removing 's': "in" ✅
    Call: chain_from_sub("in", all_words, 2)
      Returns: 2 (from cache)
    current_chain_length = 1 + 2 = 3
  
  max_chain_length = max(1, 3) = 3
  cache["sin"] = 3
  Return: 3
```

#### Processing "sing"

```
chain_from_sub("sing", all_words, 1):
  Try removing 'g': "sin" ✅
    Call: chain_from_sub("sin", all_words, 2)
      Returns: 3 (from cache)
    current_chain_length = 1 + 3 = 4
  
  max_chain_length = max(1, 4) = 4
  cache["sing"] = 4
  Return: 4
```

#### Processing "sting"

```
chain_from_sub("sting", all_words, 1):
  Try removing 't': "sing" ✅
    Call: chain_from_sub("sing", all_words, 2)
      Returns: 4 (from cache)
    current_chain_length = 1 + 4 = 5
  
  max_chain_length = max(1, 5) = 5
  cache["sting"] = 5
  Return: 5
```

#### Processing "string"

```
chain_from_sub("string", all_words, 1):
  Try removing 'r': "sting" ✅
    Call: chain_from_sub("sting", all_words, 2)
      Returns: 5 (from cache)
    current_chain_length = 1 + 5 = 6
  
  max_chain_length = max(1, 6) = 6
  cache["string"] = 6
  Return: 6
```

**Result**: Longest chain length = 6
**Chain**: "string" → "sting" → "sing" → "sin" → "in" → "i"

---

## Detailed Example: Addition Method

**Input**: `words = ["a", "at", "sat", "stat", "state"]`

### Word Chain Visualization

```
Chain: a → at → sat → stat → state
       (1) (2)  (3)  (4)   (5)
```

### Step-by-Step Execution

#### Step 1: Process "a"

```
chain_from_add("a", all_words, 1):
  Try adding each character at each position:
  
  Position 0: Try a-z
    "aa", "ba", "ca", ..., "za"
    Valid: "at" (add 't' at position 1) ✅
      Call: chain_from_add("at", all_words, 2)
  
  Position 1: Try a-z
    "aa", "ab", "ac", ..., "az"
    Valid: "at" (add 't' at position 1) ✅ (already found)
  
  Continue with "at" branch...
```

#### Step 2: Process "at" (from "a")

```
chain_from_add("at", all_words, 2):
  Try adding each character at each position:
  
  Position 0: Try a-z
    "aat", "bat", "cat", ..., "zat"
    Valid: "sat" (add 's' at position 0) ✅
      Call: chain_from_add("sat", all_words, 3)
  
  Position 1: Try a-z
    "aat", "abt", "act", ..., "azt"
    None valid
  
  Position 2: Try a-z
    "ata", "atb", "atc", ..., "atz"
    None valid
```

#### Step 3: Process "sat" (from "at")

```
chain_from_add("sat", all_words, 3):
  Try adding each character at each position:
  
  Position 0: Try a-z
    "asat", "bsat", "csat", ..., "zsat"
    None valid
  
  Position 1: Try a-z
    "saat", "sbat", "scat", ..., "szat"
    Valid: "stat" (add 't' at position 1) ✅
      Call: chain_from_add("stat", all_words, 4)
  
  Position 2: Try a-z
    "sata", "satb", "satc", ..., "satz"
    None valid
  
  Position 3: Try a-z
    "sata", "satb", "satc", ..., "satz"
    None valid
```

#### Step 4: Process "stat" (from "sat")

```
chain_from_add("stat", all_words, 4):
  Try adding each character at each position:
  
  Position 0: Try a-z
    None valid
  
  Position 1: Try a-z
    Valid: "state" (add 'e' at position 4) ✅
      Call: chain_from_add("state", all_words, 5)
  
  Position 2-5: Try a-z
    None valid
```

#### Step 5: Process "state" (from "stat")

```
chain_from_add("state", all_words, 5):
  Try adding each character at each position:
  
  All positions: Try a-z
    None valid (no longer words in dictionary)
  
  max_chain_length = 5 (current chain_length)
  cache["state"] = 5
  Return: 5
```

#### Step 6: Backtrack and Calculate

**Back to "stat":**
```
max_chain_length = max(4, 5) = 5
cache["stat"] = 5
Return: 5
```

**Back to "sat":**
```
max_chain_length = max(3, 5) = 5
cache["sat"] = 5
Return: 5
```

**Back to "at":**
```
max_chain_length = max(2, 5) = 5
cache["at"] = 5
Return: 5
```

**Back to "a":**
```
max_chain_length = max(1, 5) = 5
cache["a"] = 5
Return: 5
```

**Result**: Longest chain length = 5
**Chain**: "a" → "at" → "sat" → "stat" → "state"

---

## Key Concepts

### 1. Word Chain Definition

**Subtraction Chain:**
- Each word is formed by removing exactly one character
- Chain goes from longer to shorter words
- Example: "string" → "sting" (remove 'r')

**Addition Chain:**
- Each word is formed by adding exactly one character
- Chain goes from shorter to longer words
- Example: "at" → "sat" (add 's' at position 0)

### 2. Memoization (Caching)

**Why Cache?**
- Same word might be processed multiple times
- Avoid recalculating chain length for same word
- Significantly improves efficiency

**How It Works:**
```python
if word in self.cache:
    return self.cache[word]  # Use cached result
# ... calculate ...
self.cache[word] = result  # Store result
```

**Example:**
- "sin" might be reached from both "sing" and "sting"
- Cache stores: `cache["sin"] = 3`
- Second time: return 3 immediately

### 3. Recursive Structure

**Base Case:**
- No valid next word found
- Return chain length (1 for current word)

**Recursive Case:**
- Find all valid next words
- Recursively calculate chain from each
- Return maximum chain length

### 4. Two Approaches Comparison

| Aspect | Subtraction | Addition |
|--------|-------------|----------|
| **Direction** | Longer → Shorter | Shorter → Longer |
| **Operations** | Remove 1 char | Add 1 char |
| **Starting Point** | Longer words | Shorter words |
| **Complexity** | O(N × M) per word | O(N × M × 26) per word |

**Subtraction is more efficient:**
- Fewer operations (M positions vs M+1 positions × 26 letters)
- Natural for finding longest chains

### 5. Dynamic Programming

**Optimal Substructure:**
- Longest chain from word = 1 + max(longest chain from each valid next word)
- Can be solved recursively with memoization

**Overlapping Subproblems:**
- Same word processed multiple times
- Memoization avoids redundant calculations

---

## Algorithm Pseudocode

### Subtraction Method

```python
def longest_subword_chain_sub(words):
    all_words = set(words)
    cache = {}
    max_chain = 0
    
    for word in words:
        chain_length = chain_from_sub(word, all_words, 1)
        max_chain = max(max_chain, chain_length)
    
    return max_chain

def chain_from_sub(word, all_words, chain_length):
    if word in cache:
        return cache[word]
    
    max_chain = 1  # Word itself
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        if new_word in all_words:
            chain = 1 + chain_from_sub(new_word, all_words, chain_length + 1)
            max_chain = max(max_chain, chain)
    
    cache[word] = max_chain
    return max_chain
```

### Addition Method

```python
def longest_subword_additive(words):
    all_words = set(words)
    cache = {}
    max_chain = 0
    
    for word in words:
        chain_length = chain_from_add(word, all_words, 1)
        max_chain = max(max_chain, chain_length)
    
    return max_chain

def chain_from_add(word, all_words, chain_length):
    if word in cache:
        return cache[word]
    
    max_chain = chain_length  # Current chain length
    for i in range(len(word) + 1):
        for char in 'a'..'z':
            new_word = word[:i] + char + word[i:]
            if new_word in all_words:
                chain = chain_from_add(new_word, all_words, chain_length + 1)
                max_chain = max(max_chain, chain)
    
    cache[word] = max_chain
    return max_chain
```

---

## Complexity Analysis

| Aspect | Subtraction | Addition |
|--------|-------------|----------|
| **Time** | O(N × M²) | O(N × M × 26 × (M+1)) |
| **Space** | O(N) | O(N) |

**Where:**
- N = number of words in dictionary
- M = average word length
- 26 = alphabet size

**Time Complexity:**

**Subtraction:**
- For each word: O(M) to try removing each character
- For each removal: O(M) to create new word (string slicing)
- Total per word: O(M²)
- All words: O(N × M²)

**Addition:**
- For each word: O(M+1) positions
- For each position: O(26) letters
- For each new word: O(M+1) to create (string concatenation)
- Total per word: O((M+1) × 26 × (M+1)) = O(M² × 26)
- All words: O(N × M² × 26)

**Space Complexity:**
- Cache: O(N) to store results for each word
- Recursion stack: O(M) in worst case (chain length)
- Total: O(N)

---

## Edge Cases

### Case 1: Single Word
```
words = ["a"]
Result: 1 (chain of length 1, just the word itself)
```

### Case 2: No Valid Chain
```
words = ["abc", "xyz"]  (no connections)
Result: 1 (each word is its own chain)
```

### Case 3: Multiple Chains
```
words = ["a", "at", "sat", "i", "in", "sin"]
Result: 3 (longest is "a" → "at" → "sat" or "i" → "in" → "sin")
```

### Case 4: Empty Dictionary
```
words = []
Result: 0
```

### Case 5: Single Character Words
```
words = ["a", "i", "o"]
Result: 1 (no valid chains, each is length 1)
```

---

## Why This Algorithm Works

### Correctness

1. **Exhaustive Search:**
   - Tries all possible next words
   - Ensures no valid chain is missed

2. **Memoization:**
   - Avoids redundant calculations
   - Ensures each word is processed once

3. **Optimal Substructure:**
   - Longest chain from word = 1 + max(longest chain from next words)
   - Recursive solution finds optimal answer

### Why Memoization is Critical

**Without Memoization:**
- Same word processed multiple times
- Exponential time complexity
- Very slow for large dictionaries

**With Memoization:**
- Each word processed once
- Polynomial time complexity
- Much faster

---

## Alternative Approaches

### 1. Topological Sort + DP

**Idea**: Build graph, use topological sort, then DP

**Steps:**
1. Build graph: word → words that can be formed from it
2. Topological sort by word length
3. DP: `dp[word] = 1 + max(dp[next_word])`

**Pros:** More structured
**Cons:** More complex

### 2. BFS Approach

**Idea**: Start from all words, BFS to find longest path

**Steps:**
1. For each word, BFS to find longest chain
2. Track maximum

**Pros:** Iterative, no recursion
**Cons:** Less efficient than memoized DFS

---

## Real-World Applications

1. **Word Games:**
   - Scrabble variants
   - Word ladder puzzles

2. **Text Processing:**
   - Finding word relationships
   - Morphological analysis

3. **Natural Language Processing:**
   - Word formation analysis
   - Etymology studies

4. **Educational Tools:**
   - Vocabulary building
   - Language learning

---

## Common Mistakes

### Mistake 1: Not Counting Current Word

```python
# WRONG: Returns 0 if no next word
max_chain_length = 0
# ... find next words ...
return max_chain_length  # Should be at least 1!
```

**Fix:** Initialize to 1 (word itself counts)

### Mistake 2: Incorrect Memoization

```python
# WRONG: Doesn't account for current chain length
if word in cache:
    return cache[word]  # Should consider current position
```

**Fix:** Cache stores absolute chain length from word

### Mistake 3: Not Resetting Cache

```python
# WRONG: Cache persists between calls
def longest_chain(words):
    # cache not reset!
    for word in words:
        chain_from_sub(word, ...)
```

**Fix:** Reset cache at start of each call

---

## Summary

The longest word chain algorithm:
- Uses **two approaches**: subtraction (remove char) and addition (add char)
- Uses **memoization** to avoid redundant calculations
- Uses **recursive DFS** to explore all possible chains
- Time complexity: **O(N × M²)** for subtraction, **O(N × M² × 26)** for addition
- Space complexity: **O(N)** for cache

**Key Insight**: The longest chain from a word is 1 plus the maximum chain length from any valid next word. Memoization ensures each word is processed only once, making the algorithm efficient.

---

## Related Problems

- **LeetCode 1048**: Longest String Chain (similar problem)
- **Word Ladder**: Finding transformation sequences
- **Longest Increasing Subsequence**: Similar DP structure
- **Graph Longest Path**: Finding longest path in DAG

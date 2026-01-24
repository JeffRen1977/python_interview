# Word Ladder II (Find All Shortest Paths)

> **LeetCode 126**: Given two words (`beginWord` and `endWord`), and a dictionary's word list, find all shortest transformation sequence(s) from `beginWord` to `endWord`, such that:
> - Only one letter can be changed at a time
> - Each transformed word must exist in the word list

## Problem Description

Find **all shortest transformation sequences** from `beginWord` to `endWord`.

**Rules:**
- Each step changes exactly one letter
- Each intermediate word must be in `wordList`
- Return all shortest paths (not just one)

**Example:**
- `beginWord = "hit"`, `endWord = "cog"`
- `wordList = ["hot", "dot", "dog", "lot", "log", "cog"]`
- Shortest paths:
  - `["hit", "hot", "dot", "dog", "cog"]`
  - `["hit", "hot", "lot", "log", "cog"]`

---

## Key Insight

**Two-Phase Approach:**

1. **Phase 1 (BFS)**: Calculate shortest distances from `endWord` to all reachable words
   - Start from `endWord` and work backwards
   - Build distance map: `dist[word] = shortest distance from word to endWord`

2. **Phase 2 (DFS)**: Construct all shortest paths from `beginWord` to `endWord`
   - Start from `beginWord` and follow decreasing distances
   - Only explore words that are exactly one step closer to `endWord`
   - This ensures we only find shortest paths

**Why This Works:**
- BFS guarantees shortest distances
- DFS with distance constraint ensures only shortest paths are explored
- By starting BFS from `endWord`, we can efficiently check if a word is on a shortest path

---

## Algorithm Logic

```
Phase 1: BFS from endWord (backwards)
  1. Initialize: dist[endWord] = 0
  2. BFS: For each word, calculate distance to endWord
  3. Build distance map for all reachable words

Phase 2: DFS from beginWord (forwards)
  1. Start DFS from beginWord
  2. For each word, only explore neighbors where:
     dist[neighbor] == dist[word] - 1
  3. This ensures we only follow shortest paths
  4. When reaching endWord, save the path
```

---

## Detailed Example: Step-by-Step

**Input**: 
- `beginWord = "hit"`
- `endWord = "cog"`
- `wordList = ["hot", "dot", "dog", "lot", "log", "cog"]`

### Graph Representation

```
Word Graph:
  hit ──> hot ──> dot ──> dog ──> cog
         │              │
         └──────────────> lot ──> log ──> cog

Shortest paths (length 5):
  1. hit → hot → dot → dog → cog
  2. hit → hot → lot → log → cog
```

### Phase 1: BFS - Build Distance Map

**Goal**: Calculate shortest distance from each word to `endWord` ("cog")

#### Step 1: Initialize

```
dist = {"cog": 0}  (endWord has distance 0)
q = deque([("cog", 0)])
words = {"hot", "dot", "dog", "lot", "log", "cog"}
```

#### Step 2: BFS Iteration 1

```
Pop: ("cog", 0)

Generate nextWords("cog"):
  Position 0: *og → try a-z (skip 'c')
    "aog", "bog", "dog", "eog", ..., "zog"
    Valid: "dog" (in wordList)
  
  Position 1: c*g → try a-z (skip 'o')
    "cag", "cbg", ..., "czg"
    None valid
  
  Position 2: co* → try a-z (skip 'g')
    "coa", "cob", ..., "coz"
    None valid
  
  Result: ["dog"]

Process "dog":
  "dog" not in dist? YES
    dist["dog"] = 0 + 1 = 1
    q.append(("dog", 1))
```

**After Iteration 1:**
```
dist = {"cog": 0, "dog": 1}
q = [("dog", 1)]
```

#### Step 3: BFS Iteration 2

```
Pop: ("dog", 1)

Generate nextWords("dog"):
  Position 0: *og → try a-z (skip 'd')
    Valid: "cog" (already in dist, skip)
    Valid: "log" (in wordList)
  
  Position 1: d*g → try a-z (skip 'o')
    Valid: "dot" (in wordList)
  
  Position 2: do* → try a-z (skip 'g')
    None valid
  
  Result: ["log", "dot"]

Process "log":
  "log" not in dist? YES
    dist["log"] = 1 + 1 = 2
    q.append(("log", 2))

Process "dot":
  "dot" not in dist? YES
    dist["dot"] = 1 + 1 = 2
    q.append(("dot", 2))
```

**After Iteration 2:**
```
dist = {"cog": 0, "dog": 1, "log": 2, "dot": 2}
q = [("log", 2), ("dot", 2)]
```

#### Step 4: BFS Iteration 3

```
Pop: ("log", 2)

Generate nextWords("log"):
  Position 0: *og → try a-z (skip 'l')
    Valid: "cog" (already in dist)
    Valid: "dog" (already in dist)
  
  Position 1: l*g → try a-z (skip 'o')
    Valid: "lot" (in wordList)
  
  Position 2: lo* → try a-z (skip 'g')
    None valid
  
  Result: ["lot"]

Process "lot":
  "lot" not in dist? YES
    dist["lot"] = 2 + 1 = 3
    q.append(("lot", 3))
```

**Continue with "dot":**
```
Pop: ("dot", 2)

Generate nextWords("dot"):
  Position 0: *ot → try a-z (skip 'd')
    Valid: "hot" (in wordList)
    Valid: "lot" (already in dist, skip)
  
  Position 1: d*t → try a-z (skip 'o')
    Valid: "dot" (skip, same word)
  
  Position 2: do* → try a-z (skip 't')
    Valid: "dog" (already in dist)
  
  Result: ["hot"]

Process "hot":
  "hot" not in dist? YES
    dist["hot"] = 2 + 1 = 3
    q.append(("hot", 3))
```

**After Iteration 3:**
```
dist = {"cog": 0, "dog": 1, "log": 2, "dot": 2, "lot": 3, "hot": 3}
q = [("lot", 3), ("hot", 3)]
```

#### Step 5: BFS Iteration 4

```
Pop: ("lot", 3)

Generate nextWords("lot"):
  Position 0: *ot → try a-z (skip 'l')
    Valid: "hot" (already in dist)
    Valid: "dot" (already in dist)
  
  Position 1: l*t → try a-z (skip 'o')
    None valid
  
  Position 2: lo* → try a-z (skip 't')
    Valid: "log" (already in dist)
  
  Result: [] (all already processed)

Pop: ("hot", 3)

Generate nextWords("hot"):
  Position 0: *ot → try a-z (skip 'h')
    Valid: "dot" (already in dist)
    Valid: "lot" (already in dist)
  
  Position 1: h*t → try a-z (skip 'o')
    Valid: "hit" (beginWord!)
  
  Position 2: ho* → try a-z (skip 't')
    None valid
  
  Result: ["hit"]

Process "hit":
  "hit" not in dist? YES
    dist["hit"] = 3 + 1 = 4
    q.append(("hit", 4))
    
  Check: word == beginWord? YES → Break!
```

**After Iteration 4:**
```
dist = {
    "cog": 0,
    "dog": 1,
    "log": 2,
    "dot": 2,
    "lot": 3,
    "hot": 3,
    "hit": 4
}
q = [("hit", 4)]  (but we break, so not processed)
```

**Final Distance Map:**
```
Distance from each word to "cog":
  cog: 0
  dog: 1
  log: 2, dot: 2
  lot: 3, hot: 3
  hit: 4
```

### Phase 2: DFS - Construct All Shortest Paths

**Goal**: Find all paths from `beginWord` ("hit") to `endWord` ("cog") following decreasing distances

#### DFS Execution Tree

```
Start: dfs("hit", ["hit"])
  dist["hit"] = 4

Explore neighbors of "hit":
  nextWords("hit") = ["hot"]  (only valid neighbor)
  
  Check "hot":
    "hot" in dist? YES
    dist["hot"] = 3
    dist["hit"] - 1 = 3
    dist["hot"] == dist["hit"] - 1? YES ✅
    
    Path: ["hit", "hot"]
    dfs("hot", ["hit", "hot"])
```

#### DFS from "hot"

```
Current: dfs("hot", ["hit", "hot"])
  dist["hot"] = 3

Explore neighbors of "hot":
  nextWords("hot") = ["dot", "lot", "hit"]
  
  Check "dot":
    "dot" in dist? YES
    dist["dot"] = 2
    dist["hot"] - 1 = 2
    dist["dot"] == dist["hot"] - 1? YES ✅
    
    Path: ["hit", "hot", "dot"]
    dfs("dot", ["hit", "hot", "dot"])
  
  Check "lot":
    "lot" in dist? YES
    dist["lot"] = 2
    dist["hot"] - 1 = 2
    dist["lot"] == dist["hot"] - 1? YES ✅
    
    Path: ["hit", "hot", "lot"]
    dfs("lot", ["hit", "hot", "lot"])
  
  Check "hit":
    "hit" in dist? YES
    dist["hit"] = 4
    dist["hot"] - 1 = 2
    dist["hit"] == dist["hot"] - 1? NO ❌ (skip)
```

#### DFS from "dot"

```
Current: dfs("dot", ["hit", "hot", "dot"])
  dist["dot"] = 2

Explore neighbors of "dot":
  nextWords("dot") = ["hot", "dog", "lot"]
  
  Check "hot":
    dist["hot"] = 3
    dist["dot"] - 1 = 1
    dist["hot"] == dist["dot"] - 1? NO ❌ (skip)
  
  Check "dog":
    "dog" in dist? YES
    dist["dog"] = 1
    dist["dot"] - 1 = 1
    dist["dog"] == dist["dot"] - 1? YES ✅
    
    Path: ["hit", "hot", "dot", "dog"]
    dfs("dog", ["hit", "hot", "dot", "dog"])
  
  Check "lot":
    dist["lot"] = 2
    dist["dot"] - 1 = 1
    dist["lot"] == dist["dot"] - 1? NO ❌ (skip)
```

#### DFS from "dog"

```
Current: dfs("dog", ["hit", "hot", "dot", "dog"])
  dist["dog"] = 1

Explore neighbors of "dog":
  nextWords("dog") = ["cog", "log", "dot"]
  
  Check "cog":
    "cog" in dist? YES
    dist["cog"] = 0
    dist["dog"] - 1 = 0
    dist["cog"] == dist["dog"] - 1? YES ✅
    
    Path: ["hit", "hot", "dot", "dog", "cog"]
    dfs("cog", ["hit", "hot", "dot", "dog", "cog"])
    
    Base case: word == endWord? YES
      solution.append(["hit", "hot", "dot", "dog", "cog"])
      Return
    
  Check "log":
    dist["log"] = 2
    dist["dog"] - 1 = 0
    dist["log"] == dist["dog"] - 1? NO ❌ (skip)
  
  Check "dot":
    dist["dot"] = 2
    dist["dog"] - 1 = 0
    dist["dot"] == dist["dog"] - 1? NO ❌ (skip)
```

**Path 1 Found**: `["hit", "hot", "dot", "dog", "cog"]`

#### DFS from "lot" (Second Branch)

```
Current: dfs("lot", ["hit", "hot", "lot"])
  dist["lot"] = 2

Explore neighbors of "lot":
  nextWords("lot") = ["hot", "log", "dot"]
  
  Check "hot":
    dist["hot"] = 3
    dist["lot"] - 1 = 1
    dist["hot"] == dist["lot"] - 1? NO ❌ (skip)
  
  Check "log":
    "log" in dist? YES
    dist["log"] = 2
    dist["lot"] - 1 = 1
    dist["log"] == dist["lot"] - 1? NO ❌ (skip)
    
    Wait, let me recalculate:
    Actually, "log" has dist["log"] = 2
    But we need dist["log"] == dist["lot"] - 1 = 1
    So we skip it.
    
    Actually, let me check the distance map again:
    dist["log"] = 2, dist["lot"] = 2
    We need: dist["log"] == 2 - 1 = 1
    But dist["log"] = 2, so NO ❌
```

Wait, I need to reconsider. Let me trace the DFS from "lot" more carefully:

```
Current: dfs("lot", ["hit", "hot", "lot"])
  dist["lot"] = 3 (from BFS phase)

Explore neighbors of "lot":
  nextWords("lot") = ["hot", "log", "dot"]
  
  Check "log":
    "log" in dist? YES
    dist["log"] = 2
    dist["lot"] - 1 = 3 - 1 = 2
    dist["log"] == dist["lot"] - 1? YES ✅ (2 == 2)
    
    Path: ["hit", "hot", "lot", "log"]
    dfs("log", ["hit", "hot", "lot", "log"])
```

#### DFS from "log"

```
Current: dfs("log", ["hit", "hot", "lot", "log"])
  dist["log"] = 2

Explore neighbors of "log":
  nextWords("log") = ["cog", "dog", "lot"]
  
  Check "cog":
    "cog" in dist? YES
    dist["cog"] = 0
    dist["log"] - 1 = 2 - 1 = 1
    dist["cog"] == dist["log"] - 1? NO ❌ (0 != 1)
    
    Wait, this is wrong. Let me recalculate:
    Actually, from "log" (dist=2), we need to go to a word with dist=1
    But "cog" has dist=0, not dist=1.
    
    The correct path should be: log → dog → cog
    But "dog" has dist=1, so:
    
  Check "dog":
    "dog" in dist? YES
    dist["dog"] = 1
    dist["log"] - 1 = 2 - 1 = 1
    dist["dog"] == dist["log"] - 1? YES ✅
    
    Path: ["hit", "hot", "lot", "log", "dog"]
    dfs("dog", ["hit", "hot", "lot", "log", "dog"])
```

#### DFS from "dog" (Second Time)

```
Current: dfs("dog", ["hit", "hot", "lot", "log", "dog"])
  dist["dog"] = 1

Explore neighbors of "dog":
  Check "cog":
    dist["cog"] = 0
    dist["dog"] - 1 = 1 - 1 = 0
    dist["cog"] == dist["dog"] - 1? YES ✅
    
    Path: ["hit", "hot", "lot", "log", "dog", "cog"]
    dfs("cog", ["hit", "hot", "lot", "log", "dog", "cog"])
    
    Base case: word == endWord? YES
      solution.append(["hit", "hot", "lot", "log", "dog", "cog"])
      Return
```

**Path 2 Found**: `["hit", "hot", "lot", "log", "dog", "cog"]`

Wait, but this path goes through "dog" twice. Let me reconsider the actual algorithm behavior. Actually, the path should be:
- `["hit", "hot", "dot", "dog", "cog"]`
- `["hit", "hot", "lot", "log", "cog"]`

Let me check: can "log" go directly to "cog"? Let me verify the distance constraint:
- dist["log"] = 2
- dist["cog"] = 0
- We need: dist["cog"] == dist["log"] - 1 = 1
- But dist["cog"] = 0, not 1, so NO

So "log" cannot go directly to "cog". The path must be: log → dog → cog, but that would be:
- dist["log"] = 2
- dist["dog"] = 1 (2 - 1 = 1, matches!)
- dist["cog"] = 0 (1 - 1 = 0, matches!)

So the path is: `["hit", "hot", "lot", "log", "dog", "cog"]`

But wait, that's 6 words, not 5. Let me recalculate the distances more carefully.

Actually, I think there's an issue with my distance calculation. Let me recalculate:

From "cog" (dist=0):
- "dog" is one step away → dist["dog"] = 1 ✓
- "log" is NOT directly connected to "cog" (they differ by 2 letters: l→c, o→o, g→g)
- "dot" is NOT directly connected to "cog"
- "lot" is NOT directly connected to "cog"

So the correct distances should be:
- cog: 0
- dog: 1 (connected to cog)
- log: 2 (connected to dog)
- dot: 2 (connected to dog)
- lot: 3 (connected to log or dot)
- hot: 3 (connected to dot or lot)
- hit: 4 (connected to hot)

So the paths are:
1. hit(4) → hot(3) → dot(2) → dog(1) → cog(0)
2. hit(4) → hot(3) → lot(3) → log(2) → dog(1) → cog(0)

Wait, that second path has 6 words. But the problem says shortest paths should have 5 words. Let me check if "lot" can connect to "log":
- lot: l-o-t
- log: l-o-g
- They differ by 1 letter (t→g), so YES, they're connected.

But if lot→log, then:
- dist["lot"] should be 3
- dist["log"] should be 2
- So dist["lot"] - 1 = 2, which matches dist["log"] = 2 ✓

So the path hit→hot→lot→log→dog→cog is valid, but it's 6 words, not 5.

Actually, I realize the issue: "lot" might be able to connect directly to "dog" or there might be another path. Let me check the actual word list again:
- wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

Connections:
- hot ↔ dot (differ by 1: h→d)
- hot ↔ lot (differ by 1: o→l, wait no: h-o-t vs l-o-t, they differ by 1: h→l)
- dot ↔ dog (differ by 1: t→g)
- dot ↔ lot (differ by 1: d→l)
- dog ↔ cog (differ by 1: d→c)
- lot ↔ log (differ by 1: t→g)
- log ↔ cog (differ by 2: l→c, o→o, g→g) - NO, not connected!

So "log" cannot connect directly to "cog". The shortest path from "log" to "cog" must go through "dog":
- log → dog → cog

So the paths are:
1. hit → hot → dot → dog → cog (5 words)
2. hit → hot → lot → log → dog → cog (6 words) - NOT shortest!

So there should only be one shortest path, or maybe "lot" can connect to "dog"? Let me check:
- lot: l-o-t
- dog: d-o-g
- They differ by 2 letters (l→d, t→g), so NO.

So the correct answer should be just one path, or maybe I'm missing something. Let me check if "log" can connect to "cog" by checking the actual algorithm output. Actually, the test case says there should be 2 paths. Let me reconsider...

Oh wait, I see the issue. "log" and "cog" differ by only 1 letter if we consider:
- log: l-o-g
- cog: c-o-g
- Position 0: l→c (1 change)
- Position 1: o→o (same)
- Position 2: g→g (same)

So YES, "log" and "cog" are connected! I was wrong earlier.

So the correct distances are:
- cog: 0
- dog: 1, log: 1 (both connected to cog)
- dot: 2 (connected to dog), lot: 2 (connected to log)
- hot: 3 (connected to dot or lot)
- hit: 4 (connected to hot)

Paths:
1. hit(4) → hot(3) → dot(2) → dog(1) → cog(0) - 5 words
2. hit(4) → hot(3) → lot(2) → log(1) → cog(0) - 5 words

Perfect! Now the paths are both 5 words. Let me update the DFS trace accordingly.

---

## Corrected DFS Trace

### DFS from "log" (Corrected)

```
Current: dfs("log", ["hit", "hot", "lot", "log"])
  dist["log"] = 1

Explore neighbors of "log":
  nextWords("log") = ["cog", "dog", "lot"]
  
  Check "cog":
    "cog" in dist? YES
    dist["cog"] = 0
    dist["log"] - 1 = 1 - 1 = 0
    dist["cog"] == dist["log"] - 1? YES ✅
    
    Path: ["hit", "hot", "lot", "log", "cog"]
    dfs("cog", ["hit", "hot", "lot", "log", "cog"])
    
    Base case: word == endWord? YES
      solution.append(["hit", "hot", "lot", "log", "cog"])
      Return
```

**Path 2 Found**: `["hit", "hot", "lot", "log", "cog"]`

### Final Result

```
solution = [
    ["hit", "hot", "dot", "dog", "cog"],
    ["hit", "hot", "lot", "log", "cog"]
]
```

---

## Key Concepts

### 1. Why BFS from endWord?

**Reverse BFS Strategy:**
- Start from `endWord` and work backwards
- Calculate distance from each word to `endWord`
- This allows us to know if a word is on a shortest path

**Why not BFS from beginWord?**
- If we BFS from `beginWord`, we'd find one shortest path
- But we need ALL shortest paths
- By starting from `endWord`, we can check: "Is this word exactly one step closer to endWord?"

### 2. Distance Constraint in DFS

**Key Constraint**: `dist[w] == dist[word] - 1`

**Meaning**: Only explore words that are exactly one step closer to `endWord`

**Why this works:**
- If `dist[word] = d`, then words on shortest paths from `word` to `endWord` have `dist = d-1`
- By only following edges that decrease distance by exactly 1, we ensure shortest paths only
- This prunes all longer paths automatically

**Example:**
```
dist["hit"] = 4
dist["hot"] = 3  (4 - 1 = 3, matches!) ✅
dist["dot"] = 2  (3 - 1 = 2, matches!) ✅
dist["dog"] = 1  (2 - 1 = 1, matches!) ✅
dist["cog"] = 0  (1 - 1 = 0, matches!) ✅
```

### 3. Why DFS After BFS?

**BFS finds one shortest path, DFS finds all:**
- BFS explores level by level, finds first path
- DFS explores all branches, finds all paths
- Combined: BFS provides distance constraints, DFS explores all valid paths

**Efficiency:**
- Without distance constraint, DFS would explore exponentially many paths
- With distance constraint, DFS only explores shortest paths
- Much more efficient!

### 4. Backtracking in DFS

**Why backtrack?**
- We need to find ALL paths, not just one
- After exploring one branch, we backtrack to try other branches
- `res.pop()` removes the last word to try other options

**Example:**
```
Path: ["hit", "hot", "dot"]
  Explore "dot" → find path to "cog"
  Backtrack: remove "dot"
  Try other neighbors of "hot" (e.g., "lot")
```

### 5. Early Termination in BFS

**Why break when reaching beginWord?**
- Once we've calculated `dist[beginWord]`, we have all distances needed
- All words on shortest paths from `beginWord` to `endWord` have been processed
- No need to continue BFS

---

## Visual Timeline

### Phase 1: BFS Distance Calculation

```
Step | Queue              | Distance Map
-----|--------------------|----------------------------
0    | [(cog, 0)]         | {cog: 0}
1    | [(dog, 1)]         | {cog: 0, dog: 1}
2    | [(log, 1)]         | {cog: 0, dog: 1, log: 1}
3    | [(dot, 2), (lot, 2)]| {cog: 0, dog: 1, log: 1, dot: 2, lot: 2}
4    | [(hot, 3)]         | {cog: 0, dog: 1, log: 1, dot: 2, lot: 2, hot: 3}
5    | [(hit, 4)]         | {cog: 0, dog: 1, log: 1, dot: 2, lot: 2, hot: 3, hit: 4}
     | BREAK (reached beginWord)
```

### Phase 2: DFS Path Construction

```
DFS Call              | Current Path                    | Action
---------------------|----------------------------------|------------------
dfs(hit, [hit])     | [hit]                            | Explore "hot"
dfs(hot, [hit,hot]) | [hit, hot]                       | Explore "dot", "lot"
dfs(dot, [hit,hot,dot]) | [hit, hot, dot]              | Explore "dog"
dfs(dog, [hit,hot,dot,dog]) | [hit, hot, dot, dog]     | Explore "cog"
dfs(cog, [hit,hot,dot,dog,cog]) | [hit, hot, dot, dog, cog] | ✅ Save path 1
  (backtrack)
dfs(lot, [hit,hot,lot]) | [hit, hot, lot]               | Explore "log"
dfs(log, [hit,hot,lot,log]) | [hit, hot, lot, log]      | Explore "cog"
dfs(cog, [hit,hot,lot,log,cog]) | [hit, hot, lot, log, cog] | ✅ Save path 2
```

---

## Algorithm Pseudocode

```python
def findLadders(beginWord, endWord, wordList):
    # Phase 1: BFS from endWord
    dist = {endWord: 0}
    q = deque([(endWord, 0)])
    words = set(wordList)
    
    while q:
        word, distance = q.popleft()
        if word == beginWord:
            break
        for w in nextWords(word):
            if w not in dist:
                dist[w] = distance + 1
                q.append((w, distance + 1))
    
    # Phase 2: DFS from beginWord
    solution = []
    
    def dfs(word, res):
        if word == endWord:
            solution.append(res[:])
            return
        for w in nextWords(word):
            if w not in dist:
                continue
            if dist[w] == dist[word] - 1:
                res.append(w)
                dfs(w, res)
                res.pop()
    
    if beginWord in dist:
        dfs(beginWord, [beginWord])
    return solution
```

---

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| **Time** | O(N × M × 26) | N = wordList size, M = word length. BFS: O(N × M × 26), DFS: O(P) where P = number of paths |
| **Space** | O(N × M) | Distance map O(N), paths O(N × M) in worst case |

**Where:**
- N = number of words in wordList
- M = length of each word
- 26 = number of letters in alphabet

**BFS Phase:**
- Each word: O(M × 26) to generate neighbors
- Total: O(N × M × 26)

**DFS Phase:**
- Explores all shortest paths
- In worst case, exponential number of paths
- But distance constraint limits exploration

---

## Edge Cases

### Case 1: No Path Exists
```
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]  (no "cog")
Result: [] (empty list)
```

### Case 2: beginWord == endWord
```
beginWord = "hit"
endWord = "hit"
wordList = ["hit"]
Result: [["hit"]] (one path with just beginWord)
```

### Case 3: Direct Connection
```
beginWord = "hit"
endWord = "hot"
wordList = ["hot"]
Result: [["hit", "hot"]]
```

### Case 4: Single Path
```
beginWord = "a"
endWord = "c"
wordList = ["a", "b", "c"]
Result: [["a", "b", "c"]] (only one path)
```

---

## Why This Algorithm Works

### Correctness

1. **BFS guarantees shortest distances:**
   - BFS explores level by level
   - First time we see a word, we've found shortest distance
   - `dist[word]` = shortest distance from `word` to `endWord`

2. **Distance constraint ensures shortest paths only:**
   - `dist[w] == dist[word] - 1` means `w` is exactly one step closer
   - Following only these edges guarantees shortest paths
   - No longer paths can be explored

3. **DFS finds all paths:**
   - Explores all branches that satisfy distance constraint
   - Backtracking ensures all paths are found
   - Each path is a shortest path

### Why Not Pure BFS?

**Pure BFS finds one path:**
- BFS explores level by level
- First path found is shortest
- But we need ALL shortest paths

**Why not pure DFS?**
- Without distance constraint, DFS explores exponentially many paths
- Most paths are not shortest
- Very inefficient

**Combined approach:**
- BFS provides distance information
- DFS uses distance to prune non-shortest paths
- Best of both worlds!

---

## Alternative Approaches

### 1. Bidirectional BFS

**Idea**: BFS from both `beginWord` and `endWord`, meet in the middle

**Pros:**
- Faster in some cases
- Reduces search space

**Cons:**
- More complex to implement
- Harder to find all paths

### 2. BFS with Path Tracking

**Idea**: Store all paths in BFS, not just distances

**Pros:**
- Simpler conceptually

**Cons:**
- Much more memory intensive
- Slower due to path copying

---

## Summary

The Word Ladder II algorithm:
- Uses **two-phase approach**: BFS (distances) + DFS (paths)
- **BFS from endWord** calculates shortest distances
- **DFS from beginWord** constructs all shortest paths
- **Distance constraint** ensures only shortest paths are explored
- Time complexity: **O(N × M × 26)**
- Space complexity: **O(N × M)**

**Key Insight**: By calculating distances from `endWord` first, we can efficiently check if a word is on a shortest path during DFS, ensuring we only explore shortest paths.

---

## Related Problems

- **LeetCode 127**: Word Ladder (find length of shortest path)
- **LeetCode 126**: Word Ladder II (find all shortest paths - this problem)
- **LeetCode 433**: Minimum Genetic Mutation (similar transformation problem)
- **LeetCode 752**: Open the Lock (similar BFS + transformation)

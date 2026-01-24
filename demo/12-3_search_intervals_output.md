# Range Table Algorithm Demo

> **Problem**: Given a list of intervals, efficiently find all intervals that contain a query point.

## Timeline Visualization

```
Point:  0  1  2  3  4  5  6  7  8  9  10 11
        ─────────────────────────────────────
[0,5]:  [────────]
[6,8]:                 [─────]
[2,9]:        [──────────────────]
[4,10]:             [─────────────────]
[3,5]:           [────]
```

---

## Step 1: Initialize with Intervals

**Input intervals:**

| Index | Interval |
|-------|----------|
| 0 | `[0, 5]` |
| 1 | `[6, 8]` |
| 2 | `[2, 9]` |
| 3 | `[4, 10]` |
| 4 | `[3, 5]` |

---

## Step 2: Create Points List from Intervals

For each interval `[start, end]`, we create **TWO** points:
- `(start, index)` → marks where interval **BEGINS**
- `(end + 1, index)` → marks where interval **ENDS** (+1 for inclusivity)

| Interval | Start Point | End Point |
|----------|-------------|-----------|
| `[0, 5]` (idx 0) | `(0, 0)` | `(6, 0)` |
| `[6, 8]` (idx 1) | `(6, 1)` | `(9, 1)` |
| `[2, 9]` (idx 2) | `(2, 2)` | `(10, 2)` |
| `[4, 10]` (idx 3) | `(4, 3)` | `(11, 3)` |
| `[3, 5]` (idx 4) | `(3, 4)` | `(6, 4)` |

**Points BEFORE sorting:**
```
[(0, 0), (6, 0), (6, 1), (9, 1), (2, 2), (10, 2), (4, 3), (11, 3), (3, 4), (6, 4)]
```

**Points AFTER sorting:**
```
[(0, 0), (2, 2), (3, 4), (4, 3), (6, 0), (6, 1), (6, 4), (9, 1), (10, 2), (11, 3)]
```

---

## Step 3: Build Range Table (Line Sweep)

### Logic
Track which intervals are "active" at each point:
- If index **NOT** in `current_range` → it's a **START** → **ADD** it
- If index **IS** in `current_range` → it's an **END** → **REMOVE** it

### Processing Each Point

| Point | Index | Action | current_range | range_table entry |
|-------|-------|--------|---------------|-------------------|
| 0 | 0 | ADD (start of interval 0) | `{0}` | `{0}` |
| 2 | 2 | ADD (start of interval 2) | `{0, 2}` | `{0, 2}` |
| 3 | 4 | ADD (start of interval 4) | `{0, 2, 4}` | `{0, 2, 4}` |
| 4 | 3 | ADD (start of interval 3) | `{0, 2, 3, 4}` | `{0, 2, 3, 4}` |
| 6 | 0 | REMOVE (end of interval 0) | `{2, 3, 4}` | `{2, 3, 4}` |
| 6 | 1 | ADD (start of interval 1) | `{1, 2, 3, 4}` | `{1, 2, 3, 4}` |
| 6 | 4 | REMOVE (end of interval 4) | `{1, 2, 3}` | `{1, 2, 3}` |
| 9 | 1 | REMOVE (end of interval 1) | `{2, 3}` | `{2, 3}` |
| 10 | 2 | REMOVE (end of interval 2) | `{3}` | `{3}` |
| 11 | 3 | REMOVE (end of interval 3) | `{}` | `{}` |

### Final Range Table

| Point | Active Indices | Active Intervals |
|-------|----------------|------------------|
| 0 | `{0}` | `[[0, 5]]` |
| 2 | `{0, 2}` | `[[0, 5], [2, 9]]` |
| 3 | `{0, 2, 4}` | `[[0, 5], [2, 9], [3, 5]]` |
| 4 | `{0, 2, 3, 4}` | `[[0, 5], [2, 9], [4, 10], [3, 5]]` |
| 6 | `{1, 2, 3}` | `[[6, 8], [2, 9], [4, 10]]` |
| 9 | `{2, 3}` | `[[2, 9], [4, 10]]` |
| 10 | `{3}` | `[[4, 10]]` |
| 11 | `{}` | `[]` |

---

## Step 4: Query Examples

### Query for Point 6

**Binary search to find largest point ≤ 6**

Points to search: `[0, 2, 3, 4, 6, 6, 6, 9, 10, 11]`

| Iteration | low | high | mid | points[mid] | Comparison | Action |
|-----------|-----|------|-----|-------------|------------|--------|
| 1 | 0 | 9 | 5 | `(6, 1)` | 6 ≤ 6 | `low = 5` |
| 2 | 5 | 9 | 7 | `(9, 1)` | 9 > 6 | `high = 6` |
| 3 | 5 | 6 | 6 | `(6, 4)` | 6 ≤ 6 | `low = 6` |

**Result:**
- Closest point ≤ 6: **6**
- Active indices: `{1, 2, 3}`
- **Intervals containing 6: `[[6, 8], [2, 9], [4, 10]]`** ✅

---

### Query for Point 0

| Iteration | low | high | mid | points[mid] | Comparison | Action |
|-----------|-----|------|-----|-------------|------------|--------|
| 1 | 0 | 9 | 5 | `(6, 1)` | 6 > 0 | `high = 4` |
| 2 | 0 | 4 | 2 | `(3, 4)` | 3 > 0 | `high = 1` |
| 3 | 0 | 1 | 1 | `(2, 2)` | 2 > 0 | `high = 0` |

**Result: `[[0, 5]]`** ✅

---

### Query for Point 3

| Iteration | low | high | mid | points[mid] | Comparison | Action |
|-----------|-----|------|-----|-------------|------------|--------|
| 1 | 0 | 9 | 5 | `(6, 1)` | 6 > 3 | `high = 4` |
| 2 | 0 | 4 | 2 | `(3, 4)` | 3 ≤ 3 | `low = 2` |
| 3 | 2 | 4 | 3 | `(4, 3)` | 4 > 3 | `high = 2` |

**Result: `[[0, 5], [2, 9], [3, 5]]`** ✅

---

### Query for Point 5

| Iteration | low | high | mid | points[mid] | Comparison | Action |
|-----------|-----|------|-----|-------------|------------|--------|
| 1 | 0 | 9 | 5 | `(6, 1)` | 6 > 5 | `high = 4` |
| 2 | 0 | 4 | 2 | `(3, 4)` | 3 ≤ 5 | `low = 2` |
| 3 | 2 | 4 | 3 | `(4, 3)` | 4 ≤ 5 | `low = 3` |
| 4 | 3 | 4 | 4 | `(6, 0)` | 6 > 5 | `high = 3` |

**Result: `[[0, 5], [2, 9], [4, 10], [3, 5]]`** ✅

---

### Query for Point 7

| Iteration | low | high | mid | points[mid] | Comparison | Action |
|-----------|-----|------|-----|-------------|------------|--------|
| 1 | 0 | 9 | 5 | `(6, 1)` | 6 ≤ 7 | `low = 5` |
| 2 | 5 | 9 | 7 | `(9, 1)` | 9 > 7 | `high = 6` |
| 3 | 5 | 6 | 6 | `(6, 4)` | 6 ≤ 7 | `low = 6` |

**Result: `[[6, 8], [2, 9], [4, 10]]`** ✅

---

### Query for Point 11

| Iteration | low | high | mid | points[mid] | Comparison | Action |
|-----------|-----|------|-----|-------------|------------|--------|
| 1 | 0 | 9 | 5 | `(6, 1)` | 6 ≤ 11 | `low = 5` |
| 2 | 5 | 9 | 7 | `(9, 1)` | 9 ≤ 11 | `low = 7` |
| 3 | 7 | 9 | 8 | `(10, 2)` | 10 ≤ 11 | `low = 8` |
| 4 | 8 | 9 | 9 | `(11, 3)` | 11 ≤ 11 | `low = 9` |

**Result: `[]`** ✅ (No intervals contain 11)

---

## Algorithm Summary

### Key Concepts

1. **Line Sweep Algorithm**
   - Convert each interval `[start, end]` into two events:
     - START event at position `start`
     - END event at position `end + 1` (to handle inclusive intervals)
   - Process events in sorted order to build a lookup table

2. **Range Table**
   - A dictionary mapping each "event point" to the set of active intervals
   - Allows O(1) lookup once we find the right point

3. **Binary Search for Queries**
   - Find the largest point that is ≤ query value
   - Use the range_table to get all intervals containing that point

### Complexity Analysis

Let `n` = number of intervals

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Creating points list | O(n) | O(n) |
| Sorting points | O(n log n) | O(1) |
| Building range table | O(n) | O(n²) worst case |
| **Total Preprocessing** | **O(n log n)** | **O(n²)** |
| **Single Query** | **O(log n)** | O(k) for result |

### Verification Table

| Query Point | Expected Intervals | Algorithm Result | Status |
|-------------|-------------------|------------------|--------|
| 0 | `[0,5]` | `[[0, 5]]` | ✅ |
| 3 | `[0,5], [2,9], [3,5]` | `[[0, 5], [2, 9], [3, 5]]` | ✅ |
| 5 | `[0,5], [2,9], [4,10], [3,5]` | `[[0, 5], [2, 9], [4, 10], [3, 5]]` | ✅ |
| 6 | `[6,8], [2,9], [4,10]` | `[[6, 8], [2, 9], [4, 10]]` | ✅ |
| 7 | `[6,8], [2,9], [4,10]` | `[[6, 8], [2, 9], [4, 10]]` | ✅ |
| 11 | None | `[]` | ✅ |

---

## Use Cases

This algorithm is useful for:
- 🕐 Finding active users at a given timestamp
- 📅 Calendar/scheduling overlap queries
- 💻 Finding which processes were running at a specific time
- 🎯 Any "stabbing query" problem (which intervals contain point X?)

---

## Source Code

```python
class RangeTable:
    def __init__(self, intervals: list[list]):
        self.intervals = intervals
        self.points = self.read_intervals()
        self.range_table = self.build_range_table()

    def read_intervals(self) -> list[tuple[int, int]]:
        points = []
        for index, interval in enumerate(self.intervals):
            points.append((interval[0], index))      # Start point
            points.append((interval[1] + 1, index))  # End point + 1
        points.sort()
        return points

    def build_range_table(self) -> dict[int, set]:
        range_table = {}
        current_range = set()
        for point, index in self.points:
            if index not in current_range:
                current_range.add(index)    # Start of interval
            else:
                current_range.remove(index) # End of interval
            range_table[point] = current_range.copy()
        return range_table

    def query(self, query_point: int) -> list[list]:
        if query_point < self.points[0][0]:
            return []
        
        # Binary search for largest point <= query_point
        low, high = 0, len(self.points) - 1
        while low < high:
            m = (low + high + 1) // 2
            if self.points[m][0] > query_point:
                high = m - 1
            else:
                low = m
        
        closest_point = self.points[low][0]
        return [self.intervals[i] for i in self.range_table[closest_point]]
```

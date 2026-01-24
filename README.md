# python_interview

This repository includes all Python code for the book "Python Interview" and various coding interview problems.

## Repository Structure

### File Organization

All algorithm files follow a consistent numbering scheme: `{category}-{number}_{algorithm_name}.py`

**Categories:**
- `2-x`: String and Array Problems
- `3-x`: String Manipulation
- `4-x`: Array Problems
- `5-x`: Greedy Algorithms
- `6-x`: Data Structures
- `8-x`: Linked Lists
- `9-x`: Trees
- `12-x`: Binary Search
- `13-x`: Two-Pointer Method
- `14-x`: Dynamic Programming
- `15-x`: Depth-First Search (DFS)
- `16-x`: Backtracking
- `17-x`: Breadth-First Search (BFS) and Graph Algorithms
- `18-x`: Union-Find
- `19-x`: Advanced Algorithms

### Documentation

Each algorithm includes detailed documentation in the `demo/` folder:
- **Demo Scripts**: Step-by-step execution examples (`*_demo.py`)
- **Markdown Documentation**: Comprehensive explanations with:
  - Problem description and key insights
  - Detailed step-by-step examples
  - Algorithm logic and pseudocode
  - Complexity analysis
  - Edge cases and common mistakes
  - Visual representations and timelines

**Example:**
- Algorithm: `12-1_mySqrt.py`
- Documentation: `demo/12-1_mySqrt_output.md`

## Super Streak Problem - Complete Implementation

This repository contains a complete Python implementation of the Super Streak counting problem, including all follow-up questions and optimizations.

### Problem Description

The Super Streak problem involves counting consecutive gaming events that meet specific criteria:

1. **Streak Rules**: A streak continues as long as events have the same `event_type` and the time gap between consecutive events is ≤ T seconds.
2. **Super Streak Criteria**: A streak qualifies as a "Super Streak" if:
   - It contains at least N actions
   - The total duration spans at least X seconds

### Files

- `count_super_streaks.py` - Main implementation with all solutions
- `count_super_streaks_test.py` - Comprehensive test cases
- `demo_super_streak.py` - Interactive demonstration
- `count_super_streaks.txt` - Original problem statement

### Solutions Implemented

#### 1. Main Solution (Single User)
- **Function**: `count_super_streaks(events, N, T, X)`
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Algorithm**: 2-pointer technique

#### 2. Multiple Users Solution
- **Function**: `count_super_streaks_multiple_users(events, N, T, X)`
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Approach**: Group events by user, then apply single-user algorithm

#### 3. Space-Optimized Multiple Users
- **Function**: `count_super_streaks_optimized(events, N, T, X)`
- **Time Complexity**: O(n)
- **Space Complexity**: O(m) where m = number of unique users
- **Approach**: State management for each user

#### 4. Time Range Queries
- **Class**: `SuperStreakTracker`
- **Preprocessing**: O(n)
- **Query Time**: O(log k) per query
- **Feature**: Binary search on sorted streak intervals

### Usage Examples

#### Basic Usage
```python
from count_super_streaks import Event, count_super_streaks

events = [
    Event(101, "jump", 10),
    Event(102, "jump", 18),
    Event(301, "collect_coin", 98),
    Event(302, "collect_coin", 105),
    Event(303, "collect_coin", 112),
    Event(304, "collect_coin", 122),
    Event(305, "collect_coin", 131),
    Event(306, "collect_coin", 140)
]

result = count_super_streaks(events, N=4, T=10, X=30)
print(f"Super streaks found: {result}")  # Output: 1
```

#### Multiple Users
```python
from count_super_streaks import MultiUserEvent, count_super_streaks_multiple_users

events = [
    MultiUserEvent(1, 101, "jump", 10),
    MultiUserEvent(1, 102, "jump", 15),
    MultiUserEvent(2, 201, "crouch", 12),
    # ... more events
]

result = count_super_streaks_multiple_users(events, N=3, T=10, X=20)
print(result)  # Output: {1: 1, 2: 1}
```

#### Time Range Queries
```python
from count_super_streaks import SuperStreakTracker

tracker = SuperStreakTracker()
tracker.process_events(events, N=3, T=10, X=20)

# Count super streaks for user 1 in time range [25, 55]
count = tracker.count_streaks_in_range(1, 25, 55)
print(f"Super streaks in range: {count}")
```

### Running the Code

#### Run Tests
```bash
python3 count_super_streaks_test.py
```

#### Run Demo
```bash
python3 demo_super_streak.py
```

#### Run Main Solution with Tests
```bash
python3 count_super_streaks.py
```

### Algorithm Details

#### Two-Pointer Approach
The main algorithm uses a two-pointer technique:
1. **Left pointer**: Marks the start of a potential streak
2. **Right pointer**: Extends the streak as long as conditions are met
3. **Streak validation**: Check if completed streak meets super streak criteria
4. **Pointer advancement**: Move to next potential streak start

#### Key Insights
- Only check for super streak criteria when a streak ends
- Handle edge case where the last streak continues until the end
- Efficiently process events without storing intermediate results (space optimization)
- Use binary search for fast time range queries

### Performance Characteristics

| Solution | Time Complexity | Space Complexity | Best Use Case |
|----------|----------------|------------------|---------------|
| Main Solution | O(n) | O(1) | Single user analysis |
| Multiple Users | O(n) | O(n) | General multi-user scenarios |
| Space Optimized | O(n) | O(m) | When events >> users |
| Time Range Queries | O(log k) per query | O(n) preprocessing | Frequent time-based queries |

Where:
- n = total number of events
- m = number of unique users
- k = number of super streaks per user

### Real-World Applications

This solution can be applied to:
- Gaming analytics and player behavior analysis
- User engagement tracking
- Performance monitoring systems
- Time-series data analysis
- Activity pattern recognition

## Getting Started

### Prerequisites

- Python 3.6+
- No external dependencies required (uses only standard library)

### Running Algorithms

Each algorithm file can be run directly:

```bash
python3 12-1_mySqrt.py
python3 17-2_curriculum.py
# etc.
```

### Reading Documentation

Detailed documentation for each algorithm is available in the `demo/` folder:

```bash
# View markdown documentation
cat demo/12-1_mySqrt_output.md
cat demo/17-2_curriculum_output.md
# etc.
```

### Contributing

When adding new algorithms:
1. Follow the numbering scheme: `{category}-{number}_{algorithm_name}.py`
2. Include a `main()` function with test cases
3. Add detailed comments explaining the algorithm
4. Create documentation in the `demo/` folder if needed

## Algorithm Categories

### Binary Search (12-x)
- `12-1_mySqrt.py` - Integer square root
- `12-2_search_rotated_array.py` - Search in rotated sorted array
- `12-3_search_intervals.py` - Interval search with range table

### Two-Pointer Method (13-x)
- `13-1_sparse_vector_product.py` - Dot product of sparse vectors
- `13-2_minimum_window_substring.py` - Minimum window substring
- `13-3_interval_intersection.py` - Interval intersection
- `13-4_maximum_consecutive_ones.py` - Maximum consecutive ones with K flips
- `13-5_find_anagrams.py` - Find all anagrams

### Dynamic Programming (14-x)
- `14-1_maxProfit.py` - Best time to buy and sell stock
- `14-2_coin_change.py` - Coin change problem
- `14-3_decoding_ways.py` - Decode ways

### Depth-First Search (15-x)
- `15-1_pacific_atlantic_currents.py` - Pacific Atlantic water flow
- `15-2_predict_winner.py` - Predict the winner (minimax)
- `15-3_expression_add_operator.py` - Expression add operators

### Backtracking (16-x)
- `16-1_sudoku_solver.py` - Sudoku solver
- `16-2_robot_vacuum.py` - Robot room cleaner

### BFS and Graph Algorithms (17-x)
- `17-1_walls_and_gates.py` - Multi-source BFS for shortest distances
- `17-2_curriculum.py` - Course schedule (topological sort)
- `17-3_bus_routes.py` - Minimum buses to destination
- `17-4_isBipartite.py` - Bipartite graph detection
- `17-5_word_ladder_II.py` - Word ladder II (all shortest paths)

### Union-Find (18-x)
- `18-1_union_find.py` - Union-Find data structure

### Advanced Algorithms (19-x)
- `19-1_FileSystem.py` - File system size calculation (DFS)
- `19-2_longest_significant_chain.py` - Longest word chain
- `19-3_NumbCircles.py` - Circle groups (connected components)

### String and Array Problems (2-x)
- `2-2_binaryAddition.py` - Binary addition
- `2-3_random_indexing.py` - Random indexing
- `2-4_next_permuation.py` - Next permutation
- `2-5_valid_decimal_numbers.py` - Valid decimal numbers

### Additional Categories
- **String Manipulation (3-x)**: Minimum remove parentheses
- **Array Problems (4-x)**: Shortest array larger than K
- **Greedy Algorithms (5-x)**: Minimum cost to hire, traffic light
- **Data Structures (6-x)**: Subarrays sum to K, LRU cache
- **Linked Lists (8-x)**: Cycle detection, intersection, deep copy
- **Trees (9-x)**: Lowest common ancestor, serialize/deserialize

## Features

- **Comprehensive Solutions**: Each algorithm includes:
  - Clean, well-commented code
  - Multiple test cases
  - Main function with examples
  - Detailed documentation

- **Educational Focus**: 
  - Step-by-step explanations
  - Complexity analysis
  - Visual representations
  - Common mistakes and edge cases

- **Production Ready**:
  - Type hints
  - Error handling
  - Edge case coverage
  - Performance optimizations

## License

This implementation is provided for educational and interview preparation purposes.

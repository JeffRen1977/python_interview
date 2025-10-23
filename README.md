# python_interview

This repository includes all Python code for the book "Python Interview" and various coding interview problems.

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

### Dependencies

- Python 3.6+
- No external dependencies required (uses only standard library)

## Other Interview Problems

This repository also contains solutions to various other coding interview problems, including:
- Binary search problems
- Tree and graph algorithms
- Dynamic programming
- String manipulation
- Array and linked list problems
- And many more!

## License

This implementation is provided for educational and interview preparation purposes.

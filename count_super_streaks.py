"""
Super Streak Problem Implementation

This module implements solutions for counting "Super Streaks" in gaming events.
A Super Streak is a sequence of consecutive events of the same type that:
1. Contains at least N actions
2. Spans at least X seconds total duration
3. Each consecutive action is within T seconds of the previous one
"""

from typing import List, Dict, Tuple
from collections import defaultdict
import bisect


class Event:
    """Represents a gaming event"""
    def __init__(self, event_id: int, event_type: str, event_time: int):
        self.event_id = event_id
        self.event_type = event_type
        self.event_time = event_time
    
    def __repr__(self):
        return f"Event({self.event_id}, '{self.event_type}', {self.event_time})"


class MultiUserEvent:
    """Represents a gaming event for multiple users"""
    def __init__(self, user_id: int, event_id: int, event_type: str, event_time: int):
        self.user_id = user_id
        self.event_id = event_id
        self.event_type = event_type
        self.event_time = event_time
    
    def __repr__(self):
        return f"MultiUserEvent({self.user_id}, {self.event_id}, '{self.event_type}', {self.event_time})"


class StreakInfo:
    """Tracks streak information for space optimization"""
    def __init__(self, event_type: str = "", start_time: int = 0, 
                 last_event_time: int = 0, count: int = 0):
        self.event_type = event_type
        self.start_time = start_time
        self.last_event_time = last_event_time
        self.count = count


def count_super_streaks(events: List[Event], N: int, T: int, X: int) -> int:
    """
    Count super streaks for a single user using 2-pointer approach.
    
    Args:
        events: List of events sorted by time
        N: Minimum number of actions in a streak
        T: Maximum time gap between consecutive events
        X: Minimum total duration of a streak
    
    Returns:
        Number of super streaks
    """
    if not events:
        return 0
    
    super_streak_count = 0
    n = len(events)
    
    # Two pointers approach
    left = 0
    
    while left < n:
        # Find the end of current streak
        right = left
        current_event_type = events[left].event_type
        streak_start_time = events[left].event_time
        
        # Extend streak as long as possible
        while right < n - 1:
            next_event = events[right + 1]
            
            # Check if next event continues the streak
            if (next_event.event_type == current_event_type and 
                next_event.event_time - events[right].event_time <= T):
                right += 1
            else:
                break
        
        # Check if current streak is a super streak
        streak_count = right - left + 1
        streak_duration = events[right].event_time - streak_start_time
        
        if streak_count >= N and streak_duration >= X:
            super_streak_count += 1
        
        # Move to next potential streak start
        left = right + 1
    
    return super_streak_count


def count_super_streaks_multiple_users(events: List[MultiUserEvent], N: int, T: int, X: int) -> Dict[int, int]:
    """
    Count super streaks for multiple users.
    
    Args:
        events: List of events (may not be sorted globally, but per user they are sorted)
        N: Minimum number of actions in a streak
        T: Maximum time gap between consecutive events
        X: Minimum total duration of a streak
    
    Returns:
        Dictionary mapping user_id to super streak count
    """
    if not events:
        return {}
    
    # Group events by user
    user_events = defaultdict(list)
    for event in events:
        user_events[event.user_id].append(event)
    
    # Count super streaks for each user
    result = {}
    for user_id, user_event_list in user_events.items():
        # Convert to single user format
        single_user_events = [Event(e.event_id, e.event_type, e.event_time) for e in user_event_list]
        result[user_id] = count_super_streaks(single_user_events, N, T, X)
    
    return result


def count_super_streaks_optimized(events: List[MultiUserEvent], N: int, T: int, X: int) -> Dict[int, int]:
    """
    Space-optimized solution for multiple users using state management.
    
    Args:
        events: List of events sorted by time
        N: Minimum number of actions in a streak
        T: Maximum time gap between consecutive events
        X: Minimum total duration of a streak
    
    Returns:
        Dictionary mapping user_id to super streak count
    """
    if not events:
        return {}
    
    # Group events by user first to ensure proper processing
    user_events = defaultdict(list)
    for event in events:
        user_events[event.user_id].append(event)
    
    user_super_streak_count = {}
    
    for user_id, user_event_list in user_events.items():
        # Sort events by time for this user
        user_event_list.sort(key=lambda x: x.event_time)
        
        streak_info = StreakInfo()
        super_streak_count = 0
        
        for event in user_event_list:
            # Check if this event continues the current streak
            if (streak_info.event_type == event.event_type and 
                event.event_time - streak_info.last_event_time <= T):
                # Continue streak
                streak_info.last_event_time = event.event_time
                streak_info.count += 1
            else:
                # Current streak ended, check if it was a super streak
                if (streak_info.count >= N and 
                    streak_info.last_event_time - streak_info.start_time >= X):
                    super_streak_count += 1
                
                # Start new streak
                streak_info.event_type = event.event_type
                streak_info.start_time = event.event_time
                streak_info.last_event_time = event.event_time
                streak_info.count = 1
        
        # Check the last streak
        if (streak_info.count >= N and 
            streak_info.last_event_time - streak_info.start_time >= X):
            super_streak_count += 1
        
        user_super_streak_count[user_id] = super_streak_count
    
    return user_super_streak_count


class SuperStreakTracker:
    """
    Class for handling time range queries on super streaks.
    This is for Follow-up Question #3.
    """
    
    def __init__(self):
        # Store super streaks for each user: {user_id: [(start_time, end_time), ...]}
        self.user_super_streaks = defaultdict(list)
    
    def process_events(self, events: List[MultiUserEvent], N: int, T: int, X: int):
        """Process events and store super streak information"""
        if not events:
            return
        
        # Group events by user
        user_events = defaultdict(list)
        for event in events:
            user_events[event.user_id].append(event)
        
        # Find super streaks for each user
        for user_id, user_event_list in user_events.items():
            self._find_super_streaks_for_user(user_id, user_event_list, N, T, X)
    
    def _find_super_streaks_for_user(self, user_id: int, events: List[MultiUserEvent], 
                                   N: int, T: int, X: int):
        """Find super streaks for a specific user"""
        if not events:
            return
        
        n = len(events)
        left = 0
        
        while left < n:
            right = left
            current_event_type = events[left].event_type
            streak_start_time = events[left].event_time
            
            # Extend streak
            while right < n - 1:
                next_event = events[right + 1]
                if (next_event.event_type == current_event_type and 
                    next_event.event_time - events[right].event_time <= T):
                    right += 1
                else:
                    break
            
            # Check if super streak
            streak_count = right - left + 1
            streak_duration = events[right].event_time - streak_start_time
            
            if streak_count >= N and streak_duration >= X:
                self.user_super_streaks[user_id].append((streak_start_time, events[right].event_time))
            
            left = right + 1
        
        # Sort streaks by start time for binary search
        self.user_super_streaks[user_id].sort()
    
    def count_streaks_in_range(self, user_id: int, time_a: int, time_b: int) -> int:
        """
        Count super streaks for a user that are entirely within the time range [time_a, time_b].
        
        Args:
            user_id: The user ID
            time_a: Start time of range
            time_b: End time of range
        
        Returns:
            Number of super streaks entirely within the time range
        """
        if user_id not in self.user_super_streaks:
            return 0
        
        streaks = self.user_super_streaks[user_id]
        count = 0
        
        # Binary search for streaks that start after time_a
        left_idx = bisect.bisect_right(streaks, (time_a, float('inf'))) - 1
        if left_idx >= 0:
            left_idx = max(0, left_idx)
        else:
            left_idx = 0
        
        # Count streaks that are entirely within the range
        for i in range(left_idx, len(streaks)):
            start_time, end_time = streaks[i]
            if start_time > time_b:
                break
            if start_time >= time_a and end_time <= time_b:
                count += 1
        
        return count


def run_test_cases():
    """Run comprehensive test cases"""
    print("=== Testing Super Streak Solutions ===\n")
    
    # Test Case 1: Main problem example
    print("Test Case 1: Main Problem Example")
    events1 = [
        Event(101, "jump", 10),
        Event(102, "jump", 18),
        Event(201, "roll", 25),
        Event(202, "roll", 30),
        Event(204, "roll", 60),
        Event(205, "roll", 68),
        Event(206, "roll", 76),
        Event(207, "roll", 85),
        Event(301, "collect_coin", 98),
        Event(302, "collect_coin", 105),
        Event(303, "collect_coin", 112),
        Event(304, "collect_coin", 122),
        Event(305, "collect_coin", 131),
        Event(306, "collect_coin", 140),
        Event(401, "use_power", 150)
    ]
    
    result1 = count_super_streaks(events1, N=4, T=10, X=30)
    print(f"Expected: 1, Got: {result1}")
    assert result1 == 1, f"Test 1 failed: expected 1, got {result1}"
    print("✓ Test Case 1 passed\n")
    
    # Test Case 2: Multiple users
    print("Test Case 2: Multiple Users")
    events2 = [
        MultiUserEvent(1, 101, "jump", 10),
        MultiUserEvent(2, 201, "crouch", 12),
        MultiUserEvent(1, 102, "jump", 15),
        MultiUserEvent(2, 202, "crouch", 18),
        MultiUserEvent(1, 103, "jump", 28),
        MultiUserEvent(2, 203, "crouch", 22),
        MultiUserEvent(1, 104, "jump", 35),
        MultiUserEvent(2, 204, "crouch", 30),
        MultiUserEvent(1, 105, "jump", 42),
        MultiUserEvent(3, 301, "roll", 20),
        MultiUserEvent(2, 205, "other", 35),
        MultiUserEvent(1, 106, "jump", 50),
        MultiUserEvent(2, 206, "crouch", 60),
        MultiUserEvent(1, 107, "run", 55),
        MultiUserEvent(2, 207, "crouch", 65),
        MultiUserEvent(2, 208, "crouch", 72),
        MultiUserEvent(2, 209, "crouch", 81),
        MultiUserEvent(2, 210, "crouch", 95),
        MultiUserEvent(3, 302, "roll", 30)
    ]
    
    result2 = count_super_streaks_multiple_users(events2, N=3, T=10, X=20)
    expected2 = {1: 1, 2: 1, 3: 0}
    print(f"Expected: {expected2}, Got: {result2}")
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print("✓ Test Case 2 passed\n")
    
    # Test Case 3: Space optimized solution
    print("Test Case 3: Space Optimized Solution")
    result3 = count_super_streaks_optimized(events2, N=3, T=10, X=20)
    print(f"Expected: {expected2}, Got: {result3}")
    assert result3 == expected2, f"Test 3 failed: expected {expected2}, got {result3}"
    print("✓ Test Case 3 passed\n")
    
    # Test Case 4: Time range queries
    print("Test Case 4: Time Range Queries")
    tracker = SuperStreakTracker()
    tracker.process_events(events2, N=3, T=10, X=20)
    
    # Query for user 1 in range [25, 55]
    count_user1 = tracker.count_streaks_in_range(1, 25, 55)
    print(f"User 1 streaks in [25, 55]: Expected 1, Got {count_user1}")
    assert count_user1 == 1, f"Test 4a failed: expected 1, got {count_user1}"
    
    # Query for user 2 in range [60, 90]
    count_user2 = tracker.count_streaks_in_range(2, 60, 90)
    print(f"User 2 streaks in [60, 90]: Expected 1, Got {count_user2}")
    assert count_user2 == 1, f"Test 4b failed: expected 1, got {count_user2}"
    
    print("✓ Test Case 4 passed\n")
    
    # Test Case 5: Edge cases
    print("Test Case 5: Edge Cases")
    
    # Empty events
    result5a = count_super_streaks([], N=4, T=10, X=30)
    assert result5a == 0, f"Test 5a failed: expected 0, got {result5a}"
    print("✓ Empty events test passed")
    
    # Single event
    single_event = [Event(1, "jump", 10)]
    result5b = count_super_streaks(single_event, N=4, T=10, X=30)
    assert result5b == 0, f"Test 5b failed: expected 0, got {result5b}"
    print("✓ Single event test passed")
    
    # Streak that meets count but not duration
    events5c = [
        Event(1, "jump", 10),
        Event(2, "jump", 12),
        Event(3, "jump", 14),
        Event(4, "jump", 16)  # Count=4, Duration=6 < X=30
    ]
    result5c = count_super_streaks(events5c, N=4, T=10, X=30)
    assert result5c == 0, f"Test 5c failed: expected 0, got {result5c}"
    print("✓ Count but not duration test passed")
    
    print("✓ All test cases passed!")


if __name__ == "__main__":
    run_test_cases()

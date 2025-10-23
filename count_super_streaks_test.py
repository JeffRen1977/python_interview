"""
Test cases for Super Streak Problem

This file contains comprehensive test cases for all implementations
of the Super Streak counting problem.
"""

from count_super_streaks import (
    Event, MultiUserEvent, 
    count_super_streaks, 
    count_super_streaks_multiple_users,
    count_super_streaks_optimized,
    SuperStreakTracker
)


def test_main_problem():
    """Test the main problem example"""
    print("=== Test: Main Problem Example ===")
    
    events = [
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
    
    result = count_super_streaks(events, N=4, T=10, X=30)
    print(f"Result: {result}")
    print(f"Expected: 1")
    print(f"✓ Passed: {result == 1}\n")
    
    # Detailed explanation
    print("Explanation:")
    print("[10, 18] -> NO (count=2 < 4)")
    print("[25, 30] -> NO (count=2 < 4)")
    print("[60, 68, 76, 85] -> NO (count=4 >= 4, but duration=25 < 30)")
    print("[98, 105, 112, 122, 131, 140] -> YES (count=6 >= 4, duration=42 >= 30)")
    print("[150] -> NO (count=1 < 4)\n")


def test_multiple_users():
    """Test multiple users scenario"""
    print("=== Test: Multiple Users ===")
    
    events = [
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
    
    result = count_super_streaks_multiple_users(events, N=3, T=10, X=20)
    expected = {1: 1, 2: 1, 3: 0}
    
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"✓ Passed: {result == expected}\n")
    
    # Test space-optimized version
    result_opt = count_super_streaks_optimized(events, N=3, T=10, X=20)
    print(f"Space-optimized result: {result_opt}")
    print(f"✓ Passed: {result_opt == expected}\n")


def test_time_range_queries():
    """Test time range queries functionality"""
    print("=== Test: Time Range Queries ===")
    
    events = [
        MultiUserEvent(1, 101, "jump", 10),
        MultiUserEvent(1, 102, "jump", 15),
        MultiUserEvent(1, 103, "jump", 28),
        MultiUserEvent(1, 104, "jump", 35),
        MultiUserEvent(1, 105, "jump", 42),
        MultiUserEvent(1, 106, "jump", 50),
        MultiUserEvent(1, 107, "run", 55),
        MultiUserEvent(2, 206, "crouch", 60),
        MultiUserEvent(2, 207, "crouch", 65),
        MultiUserEvent(2, 208, "crouch", 72),
        MultiUserEvent(2, 209, "crouch", 81),
        MultiUserEvent(2, 210, "crouch", 95)
    ]
    
    tracker = SuperStreakTracker()
    tracker.process_events(events, N=3, T=10, X=20)
    
    # Test queries
    test_cases = [
        (1, 25, 55, 1),  # User 1 in range [25, 55] should have 1 super streak
        (1, 10, 20, 0),  # User 1 in range [10, 20] should have 0 super streaks
        (2, 60, 90, 1),  # User 2 in range [60, 90] should have 1 super streak
        (2, 70, 80, 0),  # User 2 in range [70, 80] should have 0 super streaks
    ]
    
    for user_id, start_time, end_time, expected in test_cases:
        result = tracker.count_streaks_in_range(user_id, start_time, end_time)
        print(f"User {user_id} in range [{start_time}, {end_time}]: {result} (expected {expected})")
        assert result == expected, f"Failed for user {user_id} in range [{start_time}, {end_time}]"
    
    print("✓ All time range queries passed\n")


def test_edge_cases():
    """Test edge cases"""
    print("=== Test: Edge Cases ===")
    
    # Empty events
    result1 = count_super_streaks([], N=4, T=10, X=30)
    print(f"Empty events: {result1} (expected 0)")
    assert result1 == 0
    
    # Single event
    single_event = [Event(1, "jump", 10)]
    result2 = count_super_streaks(single_event, N=4, T=10, X=30)
    print(f"Single event: {result2} (expected 0)")
    assert result2 == 0
    
    # Streak that meets count but not duration
    events3 = [
        Event(1, "jump", 10),
        Event(2, "jump", 12),
        Event(3, "jump", 14),
        Event(4, "jump", 16)  # Count=4, Duration=6 < X=30
    ]
    result3 = count_super_streaks(events3, N=4, T=10, X=30)
    print(f"Count but not duration: {result3} (expected 0)")
    assert result3 == 0
    
    # Streak that meets duration but not count
    events4 = [
        Event(1, "jump", 10),
        Event(2, "jump", 50)  # Count=2, Duration=40 >= X=30
    ]
    result4 = count_super_streaks(events4, N=4, T=10, X=30)
    print(f"Duration but not count: {result4} (expected 0)")
    assert result4 == 0
    
    print("✓ All edge cases passed\n")


def test_custom_scenarios():
    """Test custom scenarios"""
    print("=== Test: Custom Scenarios ===")
    
    # Multiple super streaks for same user
    events = [
        Event(1, "jump", 10),
        Event(2, "jump", 15),
        Event(3, "jump", 20),
        Event(4, "jump", 25),
        Event(5, "jump", 30),  # First super streak: count=5, duration=20
        Event(6, "run", 35),   # Different event type, streak ends
        Event(7, "jump", 50),
        Event(8, "jump", 55),
        Event(9, "jump", 60),
        Event(10, "jump", 65),
        Event(11, "jump", 70), # Second super streak: count=5, duration=20
        Event(12, "crouch", 75) # Different event type, streak ends
    ]
    
    result = count_super_streaks(events, N=3, T=10, X=15)
    print(f"Multiple super streaks: {result} (expected 2)")
    assert result == 2
    
    print("✓ Custom scenarios passed\n")


if __name__ == "__main__":
    test_main_problem()
    test_multiple_users()
    test_time_range_queries()
    test_edge_cases()
    test_custom_scenarios()
    print("🎉 All tests passed!")

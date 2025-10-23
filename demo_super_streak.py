"""
Demonstration of Super Streak Solutions

This script shows how to use the Super Streak counting implementations
with practical examples.
"""

from count_super_streaks import (
    Event, MultiUserEvent, 
    count_super_streaks, 
    count_super_streaks_multiple_users,
    count_super_streaks_optimized,
    SuperStreakTracker
)


def demo_main_problem():
    """Demonstrate the main Super Streak problem"""
    print("🎮 Super Streak Problem Demo")
    print("=" * 50)
    
    # Define the problem parameters
    N = 4  # Minimum 4 actions in a streak
    T = 10  # Maximum 10 seconds between actions
    X = 30  # Minimum 30 seconds total duration
    
    print(f"Parameters: N={N}, T={T}, X={X}")
    print(f"Need at least {N} actions spanning at least {X} seconds")
    print(f"with gaps no more than {T} seconds between actions\n")
    
    # Sample gaming events
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
    
    print("Gaming Events:")
    for event in events:
        print(f"  {event.event_time}s: {event.event_type}")
    
    # Count super streaks
    result = count_super_streaks(events, N, T, X)
    print(f"\n🏆 Super Streaks Found: {result}")
    
    # Detailed analysis
    print("\nDetailed Analysis:")
    print("Streak 1: [10, 18] jump actions")
    print("  - Count: 2 (❌ < 4 required)")
    print("  - Duration: 8s (❌ < 30s required)")
    
    print("\nStreak 2: [25, 30] roll actions")
    print("  - Count: 2 (❌ < 4 required)")
    print("  - Duration: 5s (❌ < 30s required)")
    
    print("\nStreak 3: [60, 68, 76, 85] roll actions")
    print("  - Count: 4 (✅ >= 4 required)")
    print("  - Duration: 25s (❌ < 30s required)")
    
    print("\nStreak 4: [98, 105, 112, 122, 131, 140] collect_coin actions")
    print("  - Count: 6 (✅ >= 4 required)")
    print("  - Duration: 42s (✅ >= 30s required)")
    print("  - 🏆 SUPER STREAK!")
    
    print("\nStreak 5: [150] use_power action")
    print("  - Count: 1 (❌ < 4 required)")
    print("  - Duration: 0s (❌ < 30s required)")


def demo_multiple_users():
    """Demonstrate multiple users scenario"""
    print("\n\n👥 Multiple Users Demo")
    print("=" * 50)
    
    # Parameters
    N, T, X = 3, 10, 20
    
    print(f"Parameters: N={N}, T={T}, X={X}")
    
    # Multi-user events
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
    
    print("\nEvents by User:")
    user_events = {}
    for event in events:
        if event.user_id not in user_events:
            user_events[event.user_id] = []
        user_events[event.user_id].append(event)
    
    for user_id in sorted(user_events.keys()):
        print(f"\nUser {user_id}:")
        for event in sorted(user_events[user_id], key=lambda x: x.event_time):
            print(f"  {event.event_time}s: {event.event_type}")
    
    # Count super streaks for all users
    result = count_super_streaks_multiple_users(events, N, T, X)
    print(f"\n🏆 Super Streaks by User:")
    for user_id, count in sorted(result.items()):
        print(f"  User {user_id}: {count} super streaks")
    
    # Space-optimized version
    result_opt = count_super_streaks_optimized(events, N, T, X)
    print(f"\nSpace-optimized results: {result_opt}")


def demo_time_range_queries():
    """Demonstrate time range queries"""
    print("\n\n⏰ Time Range Queries Demo")
    print("=" * 50)
    
    # Sample events
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
    
    # Setup tracker
    tracker = SuperStreakTracker()
    tracker.process_events(events, N=3, T=10, X=20)
    
    print("Time Range Queries:")
    print("(Finding super streaks entirely within specified time ranges)")
    
    queries = [
        (1, 25, 55, "User 1's super streaks in [25, 55]"),
        (1, 10, 20, "User 1's super streaks in [10, 20]"),
        (2, 60, 90, "User 2's super streaks in [60, 90]"),
        (2, 70, 80, "User 2's super streaks in [70, 80]"),
    ]
    
    for user_id, start_time, end_time, description in queries:
        count = tracker.count_streaks_in_range(user_id, start_time, end_time)
        print(f"  {description}: {count}")


def demo_performance_comparison():
    """Demonstrate performance characteristics"""
    print("\n\n⚡ Performance Characteristics")
    print("=" * 50)
    
    print("Algorithm Complexities:")
    print("  Main Solution:")
    print("    - Time: O(n) where n = number of events")
    print("    - Space: O(1) - constant space")
    print("    - Uses 2-pointer technique")
    
    print("\n  Multiple Users (Naive):")
    print("    - Time: O(n) where n = total events")
    print("    - Space: O(n) - stores all events grouped by user")
    
    print("\n  Multiple Users (Optimized):")
    print("    - Time: O(n) where n = total events")
    print("    - Space: O(m) where m = number of unique users")
    print("    - Better when events >> users")
    
    print("\n  Time Range Queries:")
    print("    - Preprocessing: O(n)")
    print("    - Query: O(log k) where k = super streaks per user")
    print("    - Uses binary search on sorted streak intervals")


if __name__ == "__main__":
    demo_main_problem()
    demo_multiple_users()
    demo_time_range_queries()
    demo_performance_comparison()
    
    print("\n\n🎯 Summary")
    print("=" * 50)
    print("The Super Streak problem demonstrates:")
    print("✅ Efficient 2-pointer algorithms")
    print("✅ Space-time complexity tradeoffs")
    print("✅ Multi-user data processing")
    print("✅ Time range query optimization")
    print("✅ Real-world gaming analytics applications")

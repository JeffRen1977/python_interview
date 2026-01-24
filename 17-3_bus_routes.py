from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Bus Routes Problem (LeetCode 815)
    
    Problem: Find the minimum number of buses needed to travel from stop S to stop T.
    
    Key Insight:
    - Each route represents a bus that visits multiple stops
    - You can switch buses at any stop that both buses visit
    - We need to find the minimum number of bus transfers
    
    Algorithm Approach: BFS (Breadth-First Search)
    - Build a graph where stops are connected through bus routes
    - Use BFS to explore all reachable stops level by level
    - Track which bus routes have been used (to avoid revisiting)
    - When we board a bus, we can visit all stops on that route
    
    Time Complexity: O(B * S) where B = number of buses, S = average stops per bus
    Space Complexity: O(B * S) for the stop_bus mapping and BFS queue
    """
    
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        """
        Find the minimum number of buses needed to travel from stop S to stop T.
        
        Args:
            routes: List of bus routes, where each route is a list of stops
            S: Starting stop
            T: Target stop
        
        Returns:
            Minimum number of buses needed, or -1 if T is unreachable from S
        """
        # Edge case: If start and destination are the same, no buses needed
        if S == T:
            return 0

        # Step 1: Build a mapping from each stop to all bus routes that visit it
        # This allows us to quickly find which buses we can board at any given stop
        # stop_bus[stop] = list of bus route indices that visit this stop
        stop_bus = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_bus[stop].append(i)
        
        # Example: If routes = [[1, 2, 7], [3, 6, 7]]
        # stop_bus = {1: [0], 2: [0], 7: [0, 1], 3: [1], 6: [1]}
        # This means: Stop 7 is visited by both bus 0 and bus 1

        # Step 2: Initialize BFS
        # bus_visited: Tracks which bus routes we've already boarded
        #   - Once we board a bus, we visit all its stops, so we don't need to board it again
        #   - This prevents infinite loops and redundant exploration
        bus_visited = set()
        
        # queue: BFS queue containing (current_stop, number_of_buses_taken)
        #   - We start at stop S with 1 bus (we'll board a bus at S)
        #   - Each element represents a state: "We're at this stop after taking N buses"
        queue = deque([(S, 1)])

        # Step 3: BFS to explore all reachable stops
        while queue:
            # Get the current stop and number of buses taken to reach it
            stop, buses = queue.popleft()
            
            # Step 3a: Check all bus routes that pass through the current stop
            # These are the buses we can potentially board from this stop
            for bus in stop_bus[stop]:
                # Skip if we've already boarded this bus route
                # Once we board a bus, we've already explored all its stops
                if bus in bus_visited:
                    continue
                
                # Mark this bus route as visited (we're about to board it)
                bus_visited.add(bus)

                # Step 3b: Board the bus and visit all stops on this route
                # When you board a bus, you can travel to any stop on that route
                for s in routes[bus]:
                    # If we've reached the target stop, return the number of buses taken
                    if s == T:
                        return buses
                    
                    # Add this stop to the queue for further exploration
                    # We've taken one more bus to reach this stop
                    # Note: We add all stops on the route, even if we're already at one of them
                    # This is because we might reach other stops on the same route through different paths
                    queue.append((s, buses + 1))

        # Step 4: If we've exhausted all possibilities and haven't reached T, it's unreachable
        return -1


def main():
    solution = Solution()

    # Test cases
    test_cases = [
        # Basic case
        ([[1, 2, 7], [3, 6, 7]], 1, 6, 2),  # Expected output: 2

        # Edge case: Start and target are the same
        ([[1, 2, 7], [3, 6, 7]], 1, 1, 0),  # Expected output: 0

        # Case with multiple bus options but shortest path is direct
        ([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 1, 7, 3),  # Expected output: 3

        # Edge case: Destination unreachable
        ([[1, 2, 7], [3, 6, 7]], 1, 8, -1),  # Expected output: -1

        # Case with overlapping routes and multiple choices
        ([[1, 2, 7], [7, 8, 9], [8, 3, 6]], 1, 6, 3),  # Expected output: 3

        # Case with one route covering start and destination
        ([[1, 2, 3, 4, 5, 6]], 1, 6, 1),  # Expected output: 1

        # Large case with chain dependencies
        ([[i, i + 1] for i in range(100)], 0, 99, 99),  # Expected output: 99
    ]

    # Running each test case
    for i, (routes, S, T, expected) in enumerate(test_cases):
        result = solution.numBusesToDestination(routes, S, T)
        assert result == expected, f"Test case {i + 1} failed: Expected {expected}, got {result}"
        print(f"Test case {i + 1} passed")


if __name__ == "__main__":
    main()

from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        # Map each stop to the list of buses (routes) that visit that stop
        stop_bus = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_bus[stop].append(i)

        # Initialize BFS
        bus_visited = set()  # Tracks which bus routes have been taken
        queue = deque([(S, 1)])  # Queue with (current stop, number of buses taken)

        # BFS loop
        while queue:
            stop, buses = queue.popleft()
            for bus in stop_bus[stop]:  # Check all bus routes passing through current stop
                if bus in bus_visited:
                    continue
                bus_visited.add(bus)

                # Traverse each stop in the current bus route
                for s in routes[bus]:
                    if s == T:
                        return buses
                    queue.append((s, buses + 1))

        return -1  # If the target cannot be reached


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

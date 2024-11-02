from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        size = len(graph)
        colors = [None] * size  # None = unvisited, "red" and "green" for two colors

        for i in range(size):
            if colors[i] is not None:  # Node already colored
                continue

            # Start BFS from the unvisited node
            queue = deque([i])
            colors[i] = "red"  # Start coloring the first node as "red"

            while queue:
                node = queue.popleft()
                current_color = colors[node]
                next_color = "green" if current_color == "red" else "red"

                # Visit all neighbors
                for neighbor in graph[node]:
                    if colors[neighbor] is None:  # If unvisited
                        colors[neighbor] = next_color
                        queue.append(neighbor)
                    elif colors[neighbor] == current_color:  # Conflict in coloring
                        return False

        return True


def main():
    solution = Solution()

    # Test cases
    test_cases = [
        # Basic bipartite case
        ([[1, 3], [0, 2], [1, 3], [0, 2]], True),  # Expected output: True

        # Non-bipartite case
        ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),  # Expected output: False

        # Bipartite case with disconnected nodes
        ([[1], [0, 3], [3], [1, 2]], True),  # Expected output: True

        # Single node (trivially bipartite)
        ([[]], True),  # Expected output: True

        # Empty graph (no edges, so it's bipartite)
        ([], True),  # Expected output: True

        # Bipartite case with complex structure
        ([[1, 4], [0, 2, 3], [1, 5], [1, 5], [0, 5], [2, 3, 4]], True),  # Expected output: True

        # Larger bipartite case
        ([[1, 2], [0, 3], [0, 3], [1, 2]], True),  # Expected output: True
    ]

    # Running each test case
    for i, (graph, expected) in enumerate(test_cases):
        result = solution.isBipartite(graph)
        assert result == expected, f"Test case {i + 1} failed: Expected {expected}, got {result}"
        print(f"Test case {i + 1} passed")


if __name__ == "__main__":
    main()

from collections import deque
from typing import List


class Solution:
    """
    Bipartite Graph Detection (LeetCode 785)
    
    Problem: Determine if a graph is bipartite.
    
    Bipartite Graph Definition:
    - A graph is bipartite if its vertices can be divided into two disjoint sets
    - Such that every edge connects a vertex from one set to a vertex in the other set
    - In other words, no edge connects two vertices in the same set
    
    Key Insight:
    - A graph is bipartite if and only if it can be 2-colored (colored with 2 colors)
    - Such that no two adjacent vertices have the same color
    - If we find an edge connecting two vertices of the same color, the graph is NOT bipartite
    
    Algorithm Approach: BFS with Coloring
    - Use BFS to traverse the graph
    - Color each node with alternating colors (red/green)
    - If we find two adjacent nodes with the same color, return False
    - Handle disconnected components by checking all unvisited nodes
    
    Time Complexity: O(V + E) where V = vertices, E = edges
    Space Complexity: O(V) for colors array and BFS queue
    """
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Check if a graph is bipartite using BFS with 2-coloring.
        
        Args:
            graph: Adjacency list representation of the graph
                  graph[i] = list of neighbors of node i
        
        Returns:
            True if the graph is bipartite, False otherwise
        """
        size = len(graph)
        
        # Step 1: Initialize color array
        # colors[i] = None (unvisited), "red", or "green"
        # We'll use 2-coloring: adjacent nodes must have different colors
        colors = [None] * size

        # Step 2: Check each node (handles disconnected components)
        # If the graph has multiple connected components, we need to check each one
        for i in range(size):
            # Skip nodes that have already been colored (visited in a previous BFS)
            if colors[i] is not None:  # Node already colored
                continue

            # Step 3: Start BFS from this unvisited node
            # This will explore the entire connected component containing node i
            queue = deque([i])
            
            # Color the starting node as "red" (arbitrary choice)
            # All nodes at even distance from this node will be "red"
            # All nodes at odd distance will be "green"
            colors[i] = "red"  # Start coloring the first node as "red"

            # Step 4: BFS to explore the connected component
            while queue:
                # Get the current node
                node = queue.popleft()
                
                # Determine the color that neighbors should have
                # Neighbors must have the opposite color of the current node
                current_color = colors[node]
                next_color = "green" if current_color == "red" else "red"

                # Step 5: Visit all neighbors of the current node
                for neighbor in graph[node]:
                    if colors[neighbor] is None:  # If unvisited
                        # Neighbor is unvisited: color it with the opposite color
                        colors[neighbor] = next_color
                        # Add to queue to explore its neighbors later
                        queue.append(neighbor)
                    elif colors[neighbor] == current_color:  # Conflict in coloring
                        # Conflict detected: neighbor has the same color as current node
                        # This means we have an edge between two nodes of the same color
                        # Therefore, the graph is NOT bipartite
                        return False

        # Step 6: If we've processed all nodes without conflicts, the graph is bipartite
        # All edges connect nodes of different colors, which satisfies the bipartite condition
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

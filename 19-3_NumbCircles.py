import math
from typing import List, Dict, Set, Tuple
import heapq

class Circle:
    def __init__(self, x: int, y: int, r: int):
        self.x = x
        self.y = y
        self.r = r

    def __hash__(self):
        return hash((self.x, self.y, self.r))

    def __eq__(self, other):
        return isinstance(other, Circle) and self.x == other.x and self.y == other.y and self.r == other.r

class CircleGroup:
    def __init__(self):
        self.cache = {}

    def IsOverlapped(self, circle1: Circle, circle2: Circle) -> bool:
        """
        Checks if two circles overlap.
        """
        distance = math.sqrt((circle1.x - circle2.x) ** 2 + (circle1.y - circle2.y) ** 2)
        return distance <= (circle1.r + circle2.r)

    def ConstructAdjacencyDict(self, circles: List[Circle]) -> Dict[Circle, Set[Circle]]:
        """
        Constructs an adjacency list where each circle is connected to overlapping circles.
        """
        adjacency_dict = {circle: set() for circle in circles}

        for i, circle1 in enumerate(circles):
            for j in range(i + 1, len(circles)):
                circle2 = circles[j]
                if self.IsOverlapped(circle1, circle2):
                    adjacency_dict[circle1].add(circle2)
                    adjacency_dict[circle2].add(circle1)

        return adjacency_dict

    def DFS(self, node: Circle, adjacency_dict: Dict[Circle, Set[Circle]], current_group: Set[Circle]):
        """
        Recursive DFS traversal to mark all circles in the same group.
        """
        if node in current_group:
            return
        current_group.add(node)

        for neighbor in adjacency_dict[node]:
            self.DFS(neighbor, adjacency_dict, current_group)

    def IsSingleGroup(self, circles: List[Circle]) -> bool:
        """
        Checks if all circles form a single group.
        """
        if not circles:
            return True

        visited = set()
        adjacency_dict = self.ConstructAdjacencyDict(circles)
        self.DFS(circles[0], adjacency_dict, visited)

        return len(visited) == len(circles)

    def CountGroups(self, circles: List[Circle]) -> int:
        """
        Counts the number of distinct groups of circles.
        """
        visited = set()
        adjacency_dict = self.ConstructAdjacencyDict(circles)
        total_groups = 0

        for circle in circles:
            if circle not in visited:
                current_group = set()
                self.DFS(circle, adjacency_dict, current_group)
                visited.update(current_group)
                total_groups += 1

        return total_groups

    def GetTopKGroups(self, circles: List[Circle], top_k: int) -> List[List[Circle]]:
        """
        Returns the k largest groups of circles.
        """
        visited = set()
        size_and_groups = []
        adjacency_dict = self.ConstructAdjacencyDict(circles)

        for circle in circles:
            if circle not in visited:
                current_group = set()
                self.DFS(circle, adjacency_dict, current_group)
                size_and_groups.append((len(current_group), current_group))
                visited.update(current_group)

        largest_groups = heapq.nlargest(top_k, size_and_groups, key=lambda x: x[0])
        return [list(group) for _, group in largest_groups]

def main():
    # Sample circles
    circles = [
        Circle(0, 0, 1),
        Circle(2, 2, 1),
        Circle(4, 4, 1),
        Circle(6, 6, 1),
        Circle(1, 1, 2),
        Circle(5, 5, 2)
    ]

    cg = CircleGroup()

    # Test if all circles are in a single group
    print("Are all circles in a single group?", cg.IsSingleGroup(circles))

    # Test counting the total number of groups
    print("Total number of groups:", cg.CountGroups(circles))

    # Test finding the top k largest groups
    k = 2
    top_k_groups = cg.GetTopKGroups(circles, k)
    for i, group in enumerate(top_k_groups, start=1):
        print(f"Group {i}: {[f'({c.x},{c.y},{c.r})' for c in group]}")

if __name__ == "__main__":
    main()

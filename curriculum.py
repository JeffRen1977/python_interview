from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True

        # Initialize adjacency list and in-degree array
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build the graph and in-degree array
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # Initialize the queue with courses that have no prerequisites
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = len(q)  # Start count with number of courses with no prerequisites

        # Process the queue using BFS
        while q:
            current_course = q.popleft()
            for next_course in adj[current_course]:
                indegree[next_course] -= 1  # Reduce the in-degree for each neighboring course
                if indegree[next_course] == 0:  # If in-degree is 0, add it to the queue
                    q.append(next_course)
                    count += 1  # Increase the count of courses that can be taken

        # If count matches numCourses, all courses can be finished
        return count == numCourses


def main():
    solution = Solution()

    # Test cases
    test_cases = [
        # Basic cases
        (2, [[1, 0]], True),  # Possible to finish: Course 1 depends on course 0.
        (2, [[1, 0], [0, 1]], False),  # Impossible to finish: Circular dependency between course 0 and course 1.
        (3, [[1, 0], [2, 1]], True),  # Possible to finish: Chain dependency 0 -> 1 -> 2.

        # Edge cases
        (1, [], True),  # Only one course, no prerequisites, possible to finish.
        (5, [], True),  # Multiple courses, no prerequisites, all are independent.
        (0, [], True),  # No courses, trivially possible to "finish".

        # More complex cases
        (4, [[1, 0], [2, 1], [3, 2]], True),  # Chain of dependencies, possible to finish.
        (4, [[1, 0], [2, 1], [3, 2], [1, 3]], False),  # Circular dependency introduced.

        # Larger input with no cycles
        (6, [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3]], True),

        # Larger input with a cycle
        (6, [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [0, 5]], False),
    ]

    # Running each test case
    for i, (numCourses, prerequisites, expected) in enumerate(test_cases):
        result = solution.canFinish(numCourses, prerequisites)
        assert result == expected, f"Test case {i + 1} failed: Expected {expected}, got {result}"
        print(f"Test case {i + 1} passed")


if __name__ == "__main__":
    main()

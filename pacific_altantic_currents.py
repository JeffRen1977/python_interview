from typing import List, Set, Tuple

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        R, C = len(matrix), len(matrix[0])
        pacific, atlantic = set(), set()

        def dfs(r: int, c: int, seen: Set[Tuple[int, int]]):
            if (r, c) in seen:
                return
            seen.add((r, c))
            for nr, nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                # Check boundaries and flow condition
                if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] >= matrix[r][c]:
                    dfs(nr, nc, seen)

        # Start DFS from cells touching the Pacific Ocean (top and left edges)
        for r in range(R):
            dfs(r, 0, pacific)  # left edge
        for c in range(C):
            dfs(0, c, pacific)  # top edge

        # Start DFS from cells touching the Atlantic Ocean (bottom and right edges)
        for r in range(R):
            dfs(r, C - 1, atlantic)  # right edge
        for c in range(C):
            dfs(R - 1, c, atlantic)  # bottom edge

        # Intersection of cells that can reach both oceans
        return list(pacific & atlantic)
def main():
    solution = Solution()
    matrix = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    result = solution.pacificAtlantic(matrix)
    print(result)  # Expected output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

if __name__ == "__main__":
    main()

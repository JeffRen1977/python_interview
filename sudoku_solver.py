class Solution(object):
    def isValid(self, board, x, y, rows, cols, digit):
        # Detect columns
        for j in range(cols):
            if board[x][j] == digit:
                return False

        # Detect rows
        for i in range(rows):
            if board[i][y] == digit:
                return False

        # Detect 3x3 blocks
        boundary_x = x - x % 3
        boundary_y = y - y % 3

        for i in range(boundary_x, boundary_x + 3):
            for j in range(boundary_y, boundary_y + 3):
                if board[i][j] == digit:
                    return False

        return True

    def emptySlots(self, board, rows, cols):
        empty = []

        # Record empty cell coordinates
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '.':
                    empty.append((i, j))

        return empty

    def DFS(self, board, empty, start, N, rows, cols):
        # N is the number of empty slots
        if start >= N:
            return True

        # Get the coordinates of the current space position
        x = empty[start][0]
        y = empty[start][1]

        # Try all digits from 1 to 9
        for k in range(1, 10):
            # Check whether the current value meets the requirements
            if self.isValid(board, x, y, rows, cols, str(k)):
                board[x][y] = str(k)  # Assign value
                if self.DFS(board, empty, start + 1, N, rows, cols):
                    return True
                # Backtrack
                board[x][y] = '.'

        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        empty = self.emptySlots(board, rows, cols)
        self.DFS(board, empty, 0, len(empty), rows, cols)


# Example Usage
if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    solution = Solution()
    solution.solveSudoku(board)
    for row in board:
        print(row)

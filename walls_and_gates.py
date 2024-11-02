from collections import deque


def farthest_positions(board):
    if not board or not board[0]:
        return []

    rows, cols = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque()

    # Initialize queue with positions of cats and set distances
    distance = [[float('inf')] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:  # Cat found
                queue.append((r, c))
                distance[r][c] = 0  # Distance to itself is 0

    # Perform BFS from all cats
    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if board[nx][ny] == 0 and distance[nx][ny] == float('inf'):
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

    # Find the maximum distance and corresponding positions
    max_distance = -1
    result = []

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 0:  # Only check empty spaces
                if distance[r][c] > max_distance:
                    max_distance = distance[r][c]
                    result = [(r, c)]
                elif distance[r][c] == max_distance:
                    result.append((r, c))

    return result


# Example Usage
board = [
    [0, -1, 1, 0],
    [0, 0, 0, -1],
    [0, -1, 0, -1],
    [1, -1, 0, 0]
]

farthest_spots = farthest_positions(board)
print(f"The positions farthest from the cats are: {farthest_spots}")

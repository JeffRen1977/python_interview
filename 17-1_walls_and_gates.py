from collections import deque


def farthest_positions(board):
    """
    Find the positions that are farthest from all cats (represented by 1) in the board.
    
    This function uses Multi-Source BFS (Breadth-First Search) starting from all cat positions
    simultaneously to calculate the shortest distance from any cat to each empty cell.
    Then it finds the empty cells with the maximum distance.
    
    Board representation:
    - 0: Empty space (can be traversed)
    - 1: Cat position (source for BFS)
    - -1: Wall/obstacle (cannot be traversed)
    
    Args:
        board: 2D list representing the room
              - board[i][j] = 0: empty space
              - board[i][j] = 1: cat position
              - board[i][j] = -1: wall/obstacle
    
    Returns:
        List of tuples (row, col) representing positions farthest from all cats.
        If multiple positions have the same maximum distance, all are returned.
    """
    # Edge case: empty board
    if not board or not board[0]:
        return []

    # Get board dimensions
    rows, cols = len(board), len(board[0])
    
    # Define 4-directional movement: Up, Down, Left, Right
    # Each tuple represents (delta_row, delta_column)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    # Queue for BFS traversal
    # Will contain positions to explore, starting with all cat positions
    queue = deque()

    # Initialize distance matrix
    # distance[i][j] = shortest distance from any cat to cell (i, j)
    # Initially set to infinity (unreachable) for all cells
    distance = [[float('inf')] * cols for _ in range(rows)]

    # Step 1: Find all cat positions and initialize BFS
    # Multi-source BFS: Start BFS from ALL cat positions simultaneously
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:  # Cat found at position (r, c)
                # Add cat position to queue as starting point for BFS
                queue.append((r, c))
                # Distance from cat to itself is 0
                distance[r][c] = 0

    # Step 2: Perform Multi-Source BFS
    # This calculates the shortest distance from ANY cat to each empty cell
    # BFS guarantees we find the shortest path (minimum number of steps)
    while queue:
        # Get the next position to process
        x, y = queue.popleft()

        # Explore all 4 neighboring cells
        for dx, dy in directions:
            # Calculate neighbor position
            nx, ny = x + dx, y + dy

            # Check if neighbor is within board boundaries
            if 0 <= nx < rows and 0 <= ny < cols:
                # Check if neighbor is:
                # 1. An empty space (0) - can be traversed
                # 2. Not yet visited (distance still infinity) - ensures shortest path
                if board[nx][ny] == 0 and distance[nx][ny] == float('inf'):
                    # Update distance: one step further from the current cell
                    # Since we're doing BFS, this is guaranteed to be the shortest distance
                    distance[nx][ny] = distance[x][y] + 1
                    # Add neighbor to queue for further exploration
                    queue.append((nx, ny))
                    # Note: We skip walls (-1) and already visited cells

    # Step 3: Find positions with maximum distance
    # After BFS, distance[i][j] contains shortest distance from any cat to (i,j)
    # We want to find empty cells with the maximum such distance
    max_distance = -1  # Track the maximum distance found
    result = []        # List to store positions with maximum distance

    # Scan through all cells in the board
    for r in range(rows):
        for c in range(cols):
            # Only consider empty spaces (0), ignore walls (-1) and cats (1)
            if board[r][c] == 0:
                # If this cell has a greater distance than current maximum
                if distance[r][c] > max_distance:
                    # Update maximum distance
                    max_distance = distance[r][c]
                    # Reset result list with this new farthest position
                    result = [(r, c)]
                # If this cell has the same distance as current maximum
                elif distance[r][c] == max_distance:
                    # Add this position to result (multiple positions can be equally far)
                    result.append((r, c))

    # Return all positions that are farthest from any cat
    # Note: If no empty cells are reachable, max_distance will be -1 and result will be []
    return result


# Example Usage
if __name__ == "__main__":
    # Example board:
    # - 0: Empty space
    # - 1: Cat position
    # - -1: Wall/obstacle
    #
    # Board layout:
    #   0  -1   1   0
    #   0   0   0  -1
    #   0  -1   0  -1
    #   1  -1   0   0
    #
    # Cats are at positions: (0, 2) and (3, 0)
    # We need to find empty cells (0) that are farthest from these cats
    board = [
        [0, -1, 1, 0],
        [0, 0, 0, -1],
        [0, -1, 0, -1],
        [1, -1, 0, 0]
    ]

    # Find positions farthest from all cats
    farthest_spots = farthest_positions(board)
    print(f"The positions farthest from the cats are: {farthest_spots}")
    print(f"These positions have the maximum shortest distance from any cat.")

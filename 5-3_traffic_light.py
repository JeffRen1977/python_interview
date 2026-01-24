import heapq


def earliest_arrival_time(city_map):
    rows = len(city_map)
    cols = len(city_map[0])

    # Priority queue to store (time, row, col)
    pq = [(city_map[0][0], 0, 0)]

    # To keep track of the minimum time to reach each cell
    min_time = [[float('inf')] * cols for _ in range(rows)]
    min_time[0][0] = city_map[0][0]

    # Directions (right, down)
    directions = [(0, 1), (1, 0)]

    while pq:
        time, r, c = heapq.heappop(pq)

        # If we reach the bottom-right corner, return the time
        if r == rows - 1 and c == cols - 1:
            return time

        # Explore the next cells in the right and down directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                # Wait until the traffic light turns green
                next_time = max(time, city_map[nr][nc])

                # If we found a faster time to reach this cell, update it and add to the queue
                if next_time < min_time[nr][nc]:
                    min_time[nr][nc] = next_time
                    heapq.heappush(pq, (next_time, nr, nc))

    # If we can't reach the destination
    return -1


# Sample input
city_map = [
    [1, 2, 0, 3],
    [4, 6, 5, 1],
    [9, 2, 5, 7],
    [5, 4, 2, 2]
]

# Output the earliest arrival time
print(earliest_arrival_time(city_map))  # Expected Output: 5

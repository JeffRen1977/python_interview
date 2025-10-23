
class RangeTable:
    def __init__(self, intervals: list[list]):
        # Step 1: Initialize with the list of intervals.
        # Each interval is assumed to be inclusive on both ends.
        self.intervals = intervals
        self.points = self.read_intervals()  # Sort all interval start and end points
        self.range_table = self.build_range_table()  # Build a lookup table for query points

    def read_intervals(self) -> list[tuple[int, int]]:
        points = []
        # Step 2: For each interval, store both the start and end points along with index.
        # We increment end points by 1 because intervals are inclusive, and we treat [start, end] as inclusive ranges.
        for index, interval in enumerate(self.intervals):
            points.append((interval[0], index))  # Store start point with index
            points.append((interval[1] + 1, index))  # Store end point + 1 to manage inclusivity

        points.sort()  # Sort points based on the interval boundaries
        return points

    def build_range_table(self) -> dict[int, set]:
        range_table = {}  # Dictionary to store ranges for each point
        current_range = set()  # Set of indices that represent the intervals covering the current point

        # Step 3: Loop over each point (sorted) and build the lookup table.
        # Add or remove intervals from the 'current_range' set as points are processed.
        for point, index in self.points:
            if index not in current_range:
                current_range.add(index)  # Add interval to current range (start of interval)
            else:
                current_range.remove(index)  # Remove interval from range (end of interval)

            # Create a copy of the current set and associate it with the point
            range_table[point] = current_range.copy()  # Copy is required since sets are mutable

        return range_table

    def query(self, query_point: int) -> list[list]:
        # If the query point is smaller than the smallest interval's start point, no intervals contain it.
        if query_point < self.points[0][0]:
            return []

        # Step 4: Use binary search to find the closest point in the range table.
        low = 0
        high = len(self.points) - 1

        # Perform binary search for the query point
        while low < high:
            m = (low + high + 1) // 2
            if self.points[m][0] > query_point:
                high = m - 1  # Narrow the range to the left
            else:
                low = m  # Move towards the right

        # Step 5: After the binary search, `low` points to the closest point <= query_point
        closest_point = self.points[low][0]

        # Step 6: Return the intervals (based on original indices) that contain the query point
        return [self.intervals[i] for i in self.range_table[closest_point]]


def main():
    # Example input list of intervals (each represents a user's usage)
    intervals = [
        [0, 5],
        [6, 8],
        [2, 9],
        [4, 10],
        [3, 5]
    ]

    # Query timestamp
    query_timestamp = 6

    # Initialize the RangeTable with the given intervals
    range_table = RangeTable(intervals)

    # Perform the query
    result = range_table.query(query_timestamp)

    # Print the result (should print indices of intervals covering the query_timestamp)
    print(f"Users active at timestamp {query_timestamp}: {result}")


if __name__ == "__main__":
    main()

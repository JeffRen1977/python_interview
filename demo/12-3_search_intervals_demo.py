
class RangeTableDemo:
    def __init__(self, intervals: list[list]):
        print("=" * 60)
        print("STEP 1: Initialize with intervals")
        print("=" * 60)
        print(f"Input intervals:")
        for i, interval in enumerate(intervals):
            print(f"  Index {i}: {interval}")
        
        self.intervals = intervals
        self.points = self.read_intervals()
        self.range_table = self.build_range_table()

    def read_intervals(self) -> list[tuple[int, int]]:
        print("\n" + "=" * 60)
        print("STEP 2: Create points list from intervals")
        print("=" * 60)
        print("For each interval [start, end], we create TWO points:")
        print("  - (start, index)     → marks where interval BEGINS")
        print("  - (end + 1, index)   → marks where interval ENDS (+1 for inclusivity)")
        print()
        
        points = []
        for index, interval in enumerate(self.intervals):
            start_point = (interval[0], index)
            end_point = (interval[1] + 1, index)
            points.append(start_point)
            points.append(end_point)
            print(f"  Interval {index} {interval}:")
            print(f"    → Start point: {start_point}")
            print(f"    → End point:   {end_point}")

        print(f"\nPoints BEFORE sorting: {points}")
        points.sort()
        print(f"Points AFTER sorting:  {points}")
        return points

    def build_range_table(self) -> dict[int, set]:
        print("\n" + "=" * 60)
        print("STEP 3: Build range table by sweeping through sorted points")
        print("=" * 60)
        print("Logic: Track which intervals are 'active' at each point")
        print("  - If index NOT in current_range → it's a START → ADD it")
        print("  - If index IN current_range → it's an END → REMOVE it")
        print()
        
        range_table = {}
        current_range = set()

        for point, index in self.points:
            print(f"Processing point ({point}, index={index}):")
            if index not in current_range:
                print(f"  → Index {index} NOT in current_range, so this is START of interval {index}")
                print(f"  → ADD index {index} to current_range")
                current_range.add(index)
            else:
                print(f"  → Index {index} IS in current_range, so this is END of interval {index}")
                print(f"  → REMOVE index {index} from current_range")
                current_range.remove(index)

            range_table[point] = current_range.copy()
            print(f"  → current_range = {current_range}")
            print(f"  → range_table[{point}] = {range_table[point]}")
            print()

        print("Final range_table:")
        for pt, indices in sorted(range_table.items()):
            intervals_at_point = [self.intervals[i] for i in indices]
            print(f"  Point {pt}: indices {indices} → intervals {intervals_at_point}")
        
        return range_table

    def query(self, query_point: int) -> list[list]:
        print("\n" + "=" * 60)
        print(f"STEP 4: Query for point {query_point}")
        print("=" * 60)
        
        # Edge case: query point is before all intervals
        if query_point < self.points[0][0]:
            print(f"Query point {query_point} < smallest point {self.points[0][0]}")
            print("Result: No intervals contain this point")
            return []

        print(f"Binary search to find largest point <= {query_point}")
        print(f"Points to search: {[p[0] for p in self.points]}")
        
        low = 0
        high = len(self.points) - 1
        iteration = 0

        while low < high:
            iteration += 1
            m = (low + high + 1) // 2
            print(f"\n  Iteration {iteration}:")
            print(f"    low={low}, high={high}, mid={m}")
            print(f"    points[{m}] = {self.points[m]}, value = {self.points[m][0]}")
            
            if self.points[m][0] > query_point:
                print(f"    {self.points[m][0]} > {query_point}, so search LEFT: high = {m - 1}")
                high = m - 1
            else:
                print(f"    {self.points[m][0]} <= {query_point}, so search RIGHT: low = {m}")
                low = m

        closest_point = self.points[low][0]
        print(f"\nBinary search complete!")
        print(f"  Closest point <= {query_point} is: {closest_point}")
        print(f"  Active interval indices at point {closest_point}: {self.range_table[closest_point]}")

        result = [self.intervals[i] for i in self.range_table[closest_point]]
        print(f"\n" + "=" * 60)
        print(f"RESULT: Intervals containing {query_point}:")
        print(f"=" * 60)
        for i in self.range_table[closest_point]:
            print(f"  Index {i}: {self.intervals[i]}")
        
        return result


def main():
    print("╔" + "═" * 58 + "╗")
    print("║" + " RANGE TABLE ALGORITHM DEMO ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")
    print()
    
    # Example input list of intervals
    intervals = [
        [0, 5],    # index 0
        [6, 8],    # index 1
        [2, 9],    # index 2
        [4, 10],   # index 3
        [3, 5]     # index 4
    ]

    # Visualize the intervals on a timeline
    print("TIMELINE VISUALIZATION:")
    print("  Point:  0  1  2  3  4  5  6  7  8  9  10 11")
    print("  " + "-" * 40)
    print("  [0,5]:  [--------]")
    print("  [6,8]:                 [-----]")
    print("  [2,9]:        [------------------]")
    print("  [4,10]:             [-----------------]")
    print("  [3,5]:           [----]")
    print()

    # Initialize the RangeTable with the given intervals
    range_table = RangeTableDemo(intervals)

    # Query timestamp
    query_timestamp = 6
    result = range_table.query(query_timestamp)

    print(f"\nFinal answer: {result}")
    
    # Additional queries to demonstrate
    print("\n" + "=" * 60)
    print("ADDITIONAL QUERY EXAMPLES")
    print("=" * 60)
    
    for q in [0, 3, 5, 7, 11]:
        print(f"\nQuery({q}):")
        result = range_table.query(q)
        print(f"  → {result}")


if __name__ == "__main__":
    main()

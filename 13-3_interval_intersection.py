from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        Find the intersection of two lists of closed intervals.
        
        Each list of intervals is pairwise disjoint and in sorted order.
        
        Args:
            A: First list of intervals, each interval is [start, end]
            B: Second list of intervals, each interval is [start, end]
        
        Returns:
            List of intersection intervals, each interval is [start, end]
        """
        ans = []
        i = j = 0
        
        while i < len(A) and j < len(B):
            # Check if A[i] intersects with B[j]
            # lo - Starting point of the intersection
            # hi - End point of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            
            if lo <= hi:
                # There is an intersection
                ans.append([lo, hi])
            
            # Remove the interval with the smaller endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        
        return ans


def main():
    sol = Solution()
    
    # Example 1: Basic intersection
    A1 = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B1 = [[1, 5], [8, 12], [15, 24], [25, 26]]
    result1 = sol.intervalIntersection(A1, B1)
    print(f"Example 1:")
    print(f"  A = {A1}")
    print(f"  B = {B1}")
    print(f"  Intersection: {result1}")
    print(f"  Expected: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]")
    print()
    
    # Example 2: No intersection
    A2 = [[1, 3], [5, 9]]
    B2 = [[4, 4], [10, 11]]
    result2 = sol.intervalIntersection(A2, B2)
    print(f"Example 2:")
    print(f"  A = {A2}")
    print(f"  B = {B2}")
    print(f"  Intersection: {result2}")
    print(f"  Expected: []")
    print()
    
    # Example 3: Complete overlap
    A3 = [[1, 7]]
    B3 = [[3, 10]]
    result3 = sol.intervalIntersection(A3, B3)
    print(f"Example 3:")
    print(f"  A = {A3}")
    print(f"  B = {B3}")
    print(f"  Intersection: {result3}")
    print(f"  Expected: [[3, 7]]")
    print()
    
    # Example 4: Single point intersection
    A4 = [[1, 2], [5, 6]]
    B4 = [[2, 3], [4, 5]]
    result4 = sol.intervalIntersection(A4, B4)
    print(f"Example 4:")
    print(f"  A = {A4}")
    print(f"  B = {B4}")
    print(f"  Intersection: {result4}")
    print(f"  Expected: [[2, 2], [5, 5]]")
    print()
    
    # Example 5: One list is empty
    A5 = [[1, 2], [3, 4]]
    B5 = []
    result5 = sol.intervalIntersection(A5, B5)
    print(f"Example 5:")
    print(f"  A = {A5}")
    print(f"  B = {B5}")
    print(f"  Intersection: {result5}")
    print(f"  Expected: []")
    print()


if __name__ == "__main__":
    main()

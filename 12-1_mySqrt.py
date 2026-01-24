class Solution:
    def mySqrt(self, x: int) -> int:
        # If the number is 0, the square root is 0.
        if x == 0:
            return 0
        
        # If the number is 1, the square root is 1.
        if x == 1:
            return 1 
        
        # Initialize the left boundary of the binary search to 0.
        left = 0
        
        # Initialize the right boundary of the binary search to the given number 'x'.
        right = x
        
        # 'value' will store the closest integer square root found.
        value = -1
        
        # Start binary search until left surpasses right.
        while left <= right:
            # Find the midpoint between left and right.
            mid = (left + right) // 2 
            
            # If the square of 'mid' is greater than 'x', move the search to the left.
            if mid * mid > x: 
                value = mid  # Store the current mid as a candidate value.
                right = mid - 1  # Adjust the right boundary to mid-1 to search smaller values.
            else: 
                # If 'mid' squared is less than or equal to 'x', move the search to the right.
                left = mid + 1 
        
        # Check if the current candidate value's square exceeds 'x'.
        if value * value > x:
            return value - 1  # If so, return one less than the candidate value.
        
        return value  # Otherwise, return the candidate value.


def main():
    sol = Solution()

    # Example 1: Perfect square
    x1 = 4
    result1 = sol.mySqrt(x1)
    print(f"sqrt({x1}) = {result1}")  # Expected: 2
    print(f"Verification: {result1}² = {result1 * result1}")
    print()

    # Example 2: Non-perfect square
    x2 = 8
    result2 = sol.mySqrt(x2)
    print(f"sqrt({x2}) = {result2}")  # Expected: 2 (since 2²=4 < 8 < 3²=9)
    print(f"Verification: {result2}² = {result2 * result2} <= {x2} < {(result2 + 1) ** 2}")
    print()

    # Example 3: Large number
    x3 = 100
    result3 = sol.mySqrt(x3)
    print(f"sqrt({x3}) = {result3}")  # Expected: 10
    print(f"Verification: {result3}² = {result3 * result3}")
    print()

    # Example 4: Edge case - 0
    x4 = 0
    result4 = sol.mySqrt(x4)
    print(f"sqrt({x4}) = {result4}")  # Expected: 0
    print()

    # Example 5: Edge case - 1
    x5 = 1
    result5 = sol.mySqrt(x5)
    print(f"sqrt({x5}) = {result5}")  # Expected: 1
    print()

    # Example 6: Large non-perfect square
    x6 = 2147395599
    result6 = sol.mySqrt(x6)
    print(f"sqrt({x6}) = {result6}")
    print(f"Verification: {result6}² = {result6 * result6} <= {x6} < {(result6 + 1) ** 2}")
    print()


if __name__ == "__main__":
    main()

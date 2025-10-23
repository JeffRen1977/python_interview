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

from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        """
        Find the maximum number of consecutive 1's after flipping at most K zeros.
        
        Args:
            A: Binary array (0s and 1s)
            K: Maximum number of zeros that can be flipped to 1
        
        Returns:
            Maximum length of consecutive 1's (with at most K flips)
        """
        # Initialize the maximum length of consecutive ones
        max_len = -1
        
        # Define two pointers (left and right) to represent the sliding window
        left, right = 0, 0
        
        # Define the variable to count the number of zeros encountered (i.e., flips)
        flip = 0
        
        # Iterate through the array using the right pointer
        for right, item in enumerate(A):
            # If we encounter a zero, we increment the flip count
            if item == 0:
                flip += 1
            
            # If the number of zeros (flips) exceeds K, move the left pointer
            while flip > K:
                # When the left pointer encounters a zero, decrement the flip count
                if A[left] == 0:
                    flip -= 1
                
                # Move the left pointer to shrink the window
                left += 1
            
            # Update the maximum length of the valid window (right - left + 1)
            max_len = max(max_len, right - left + 1)
        
        # Return the maximum length of the consecutive ones (with at most K flips)
        return max_len


def main():
    sol = Solution()
    
    # Example 1: Basic case
    A1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    K1 = 2
    result1 = sol.longestOnes(A1, K1)
    print(f"Example 1:")
    print(f"  A = {A1}")
    print(f"  K = {K1}")
    print(f"  Result: {result1}")
    print(f"  Expected: 6 (flip two zeros in the middle)")
    print()
    
    # Example 2: All ones
    A2 = [1, 1, 1, 1, 1]
    K2 = 0
    result2 = sol.longestOnes(A2, K2)
    print(f"Example 2:")
    print(f"  A = {A2}")
    print(f"  K = {K2}")
    print(f"  Result: {result2}")
    print(f"  Expected: 5")
    print()
    
    # Example 3: All zeros with K flips
    A3 = [0, 0, 0, 0]
    K3 = 2
    result3 = sol.longestOnes(A3, K3)
    print(f"Example 3:")
    print(f"  A = {A3}")
    print(f"  K = {K3}")
    print(f"  Result: {result3}")
    print(f"  Expected: 2 (can flip 2 zeros)")
    print()
    
    # Example 4: Mixed with K=1
    A4 = [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]
    K4 = 1
    result4 = sol.longestOnes(A4, K4)
    print(f"Example 4:")
    print(f"  A = {A4}")
    print(f"  K = {K4}")
    print(f"  Result: {result4}")
    print(f"  Expected: 6 (flip one zero to get consecutive ones)")
    print()
    
    # Example 5: K is larger than number of zeros
    A5 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0]
    K5 = 5
    result5 = sol.longestOnes(A5, K5)
    print(f"Example 5:")
    print(f"  A = {A5}")
    print(f"  K = {K5}")
    print(f"  Result: {result5}")
    print(f"  Expected: 10 (can flip all zeros)")
    print()
    
    # Example 6: Single element
    A6 = [0]
    K6 = 1
    result6 = sol.longestOnes(A6, K6)
    print(f"Example 6:")
    print(f"  A = {A6}")
    print(f"  K = {K6}")
    print(f"  Result: {result6}")
    print(f"  Expected: 1 (flip the zero)")
    print()


if __name__ == "__main__":
    main()

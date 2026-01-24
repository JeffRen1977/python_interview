from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Find all starting indices of anagrams of string p in string s.
        
        An anagram is a word formed by rearranging the letters of another word.
        
        Args:
            s: The string to search in
            p: The target string to find anagrams of
        
        Returns:
            List of starting indices where anagrams of p are found in s
        """
        # Use Counter to store the frequency of characters in the target string p
        p_counter = Counter(p)
        
        # Define a counter for the sliding window in the string s
        s_counter = Counter()
        
        # List to store the result (starting indices of anagrams)
        ans = []
        
        # Length of string p and s
        np = len(p)
        ns = len(s)
        
        # Use the sliding window technique with left and right pointers
        left = 0  # This will represent the left pointer of the window
        
        # Iterate over the string s using the right pointer
        for i in range(ns):
            # Add the character at the right pointer to the sliding window's counter
            s_counter[s[i]] += 1
            
            # If the current window size equals the length of p
            if i - left + 1 == np:
                # Compare the frequency counters of s (current window) and p
                if s_counter == p_counter:
                    # If they are equal, add the starting index (left pointer) to the result
                    ans.append(left)
                
                # Before moving the left pointer, adjust the s_counter for the character at left
                if s_counter[s[left]] == 1:
                    # If there is only one instance of the left character, remove it
                    del s_counter[s[left]]
                else:
                    # Otherwise, decrement the count of the left character
                    s_counter[s[left]] -= 1
                
                # Move the left pointer to the right, shrinking the window
                left += 1
        
        # Return the result containing all the starting indices of p's anagrams in s
        return ans


def main():
    sol = Solution()
    
    # Example 1: Basic case
    s1 = "cbaebabacd"
    p1 = "abc"
    result1 = sol.findAnagrams(s1, p1)
    print(f"Example 1:")
    print(f"  s = '{s1}'")
    print(f"  p = '{p1}'")
    print(f"  Result: {result1}")
    print(f"  Expected: [0, 6]")
    print(f"  Explanation: 'cba' at index 0 and 'bac' at index 6 are anagrams of 'abc'")
    print()
    
    # Example 2: Multiple anagrams
    s2 = "abab"
    p2 = "ab"
    result2 = sol.findAnagrams(s2, p2)
    print(f"Example 2:")
    print(f"  s = '{s2}'")
    print(f"  p = '{p2}'")
    print(f"  Result: {result2}")
    print(f"  Expected: [0, 1, 2]")
    print(f"  Explanation: 'ab' at index 0, 'ba' at index 1, and 'ab' at index 2 are anagrams")
    print()
    
    # Example 3: No anagrams
    s3 = "af"
    p3 = "be"
    result3 = sol.findAnagrams(s3, p3)
    print(f"Example 3:")
    print(f"  s = '{s3}'")
    print(f"  p = '{p3}'")
    print(f"  Result: {result3}")
    print(f"  Expected: []")
    print()
    
    # Example 4: Single character
    s4 = "baa"
    p4 = "aa"
    result4 = sol.findAnagrams(s4, p4)
    print(f"Example 4:")
    print(f"  s = '{s4}'")
    print(f"  p = '{p4}'")
    print(f"  Result: {result4}")
    print(f"  Expected: [1]")
    print(f"  Explanation: 'aa' at index 1 is an anagram of 'aa'")
    print()
    
    # Example 5: Longer strings
    s5 = "eidbaooo"
    p5 = "ab"
    result5 = sol.findAnagrams(s5, p5)
    print(f"Example 5:")
    print(f"  s = '{s5}'")
    print(f"  p = '{p5}'")
    print(f"  Result: {result5}")
    print(f"  Expected: [3]")
    print(f"  Explanation: 'ba' at index 3 is an anagram of 'ab'")
    print()


if __name__ == "__main__":
    main()

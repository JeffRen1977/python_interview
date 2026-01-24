from collections import deque
from typing import List
import string

class Solution:
    """
    Word Ladder II (LeetCode 126)
    
    Problem: Find all shortest transformation sequences from beginWord to endWord.
    Each transformation must change exactly one letter, and each intermediate word
    must exist in wordList.
    
    Key Insight: Two-Phase Approach
    1. Phase 1 (BFS): Calculate shortest distances from endWord to all reachable words
       - Start from endWord and work backwards
       - Build a distance map: dist[word] = shortest distance from word to endWord
    2. Phase 2 (DFS): Construct all shortest paths from beginWord to endWord
       - Start from beginWord and follow decreasing distances
       - Only explore words that are exactly one step closer to endWord
       - This ensures we only find shortest paths
    
    Why This Works:
    - BFS guarantees we find shortest distances
    - DFS with distance constraint ensures we only explore shortest paths
    - By starting BFS from endWord, we can efficiently check if a word is on a shortest path
    
    Time Complexity: O(N × M × 26) where N = wordList size, M = word length
    Space Complexity: O(N × M) for distance map and paths
    """
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        Find all shortest transformation sequences from beginWord to endWord.
        
        Args:
            beginWord: Starting word
            endWord: Target word
            wordList: List of valid intermediate words
        
        Returns:
            List of all shortest transformation sequences (paths)
        """
        # Step 1: Initialize distance map and BFS queue
        # dist[word] = shortest distance from word to endWord
        # We start from endWord, so endWord has distance 0
        dist = {endWord: 0}
        
        # BFS queue: (word, distance_from_endWord)
        # We'll explore backwards from endWord to find distances
        q = deque([(endWord, 0)])
        
        # Convert wordList to set for O(1) lookup
        words = set(wordList)

        # Step 2: Helper function to generate all valid next words
        # A valid next word differs by exactly one letter from the current word
        def nextWords(word):
            """
            Generate all words that differ by exactly one letter from word.
            These are the words we can transform to in one step.
            
            Args:
                word: Current word
            
            Returns:
                List of valid next words (in wordList or beginWord)
            """
            result = []
            # Try changing each position in the word
            for i in range(len(word)):
                # Try each possible letter at position i
                for c in string.ascii_lowercase:
                    # Skip if the letter is the same (no change)
                    if c == word[i]:
                        continue
                    # Create new word by replacing character at position i
                    w = word[:i] + c + word[i + 1:]
                    # Check if this word is valid (in wordList or is beginWord)
                    if w in words or w == beginWord:
                        result.append(w)
            return result

        # Step 3: BFS Phase - Calculate shortest distances from endWord
        # We work backwards from endWord to find the shortest distance
        # from each word to endWord
        while q:
            word, distance = q.popleft()
            
            # Early termination: If we've reached beginWord, we have all distances we need
            # All words on shortest paths from beginWord to endWord have been processed
            if word == beginWord:
                break
            
            # Explore all words that can be reached from current word
            for w in nextWords(word):
                # If we haven't seen this word before, it's at distance + 1
                if w not in dist:
                    dist[w] = distance + 1
                    q.append((w, distance + 1))
        
        # Note: If beginWord is not in dist, there's no path from beginWord to endWord
        # The DFS phase will naturally return an empty list in this case

        # Step 4: Initialize solution list to store all shortest paths
        solution = []

        # Step 5: DFS Phase - Construct all shortest paths from beginWord to endWord
        # We use DFS to explore all possible paths, but only follow edges that
        # decrease the distance to endWord (ensuring shortest paths only)
        def dfs(word, res):
            """
            Recursively construct all shortest paths from word to endWord.
            
            Args:
                word: Current word in the path
                res: Current path (list of words visited so far)
            """
            # Base case: We've reached the endWord
            if word == endWord:
                # Add a copy of the current path to solutions
                # We use res[:] to create a copy, not a reference
                solution.append(res[:])
                return
            
            # Explore all possible next words
            for w in nextWords(word):
                # Skip if this word is not reachable (not in distance map)
                # This means it's not on any path from beginWord to endWord
                if w not in dist:
                    continue
                
                # Key constraint: Only consider words that are exactly one step closer
                # to endWord. This ensures we only explore shortest paths.
                # dist[w] == dist[word] - 1 means w is one step closer to endWord
                if dist[w] == dist[word] - 1:  # only consider next distance word
                    # Add this word to current path
                    res.append(w)
                    # Recursively explore from this word
                    dfs(w, res)
                    # Backtrack: remove this word to try other paths
                    res.pop()

        # Step 6: Start DFS from beginWord
        # Only proceed if beginWord is reachable (in distance map)
        # If beginWord is not in dist, there's no path, and DFS won't find anything
        if beginWord in dist:
            dfs(beginWord, [beginWord])
        
        return solution
def main():
    solution = Solution()

    # Test case 1: Expected output with multiple shortest paths
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    output1 = solution.findLadders(beginWord1, endWord1, wordList1)
    print("Test case 1:")
    print(f"Input: beginWord = '{beginWord1}', endWord = '{endWord1}', wordList = {wordList1}")
    print("Output:", output1)
    print()

    # Test case 2: No valid transformation path (endWord not in wordList)
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    output2 = solution.findLadders(beginWord2, endWord2, wordList2)
    print("Test case 2:")
    print(f"Input: beginWord = '{beginWord2}', endWord = '{endWord2}', wordList = {wordList2}")
    print("Output:", output2)
    print()

    # Test case 3: Only one transformation needed
    beginWord3 = "hit"
    endWord3 = "hot"
    wordList3 = ["hot"]
    output3 = solution.findLadders(beginWord3, endWord3, wordList3)
    print("Test case 3:")
    print(f"Input: beginWord = '{beginWord3}', endWord = '{endWord3}', wordList = {wordList3}")
    print("Output:", output3)
    print()

    # Test case 4: Larger wordList with multiple shortest paths
    beginWord4 = "a"
    endWord4 = "c"
    wordList4 = ["a", "b", "c"]
    output4 = solution.findLadders(beginWord4, endWord4, wordList4)
    print("Test case 4:")
    print(f"Input: beginWord = '{beginWord4}', endWord = '{endWord4}', wordList = {wordList4}")
    print("Output:", output4)
    print()

    # Test case 5: Edge case with no transformations needed (beginWord equals endWord)
    beginWord5 = "hit"
    endWord5 = "hit"
    wordList5 = ["hit"]
    output5 = solution.findLadders(beginWord5, endWord5, wordList5)
    print("Test case 5:")
    print(f"Input: beginWord = '{beginWord5}', endWord = '{endWord5}', wordList = {wordList5}")
    print("Output:", output5)
    print()

if __name__ == "__main__":
    main()

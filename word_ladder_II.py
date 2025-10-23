from collections import deque
from typing import List
import string

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Establish distances from each word to endWord
        dist = {endWord: 0}
        q = deque([(endWord, 0)])
        words = set(wordList)

        # Helper function to generate all possible next words differing by one letter
        def nextWords(word):
            result = []
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    if c == word[i]:
                        continue
                    w = word[:i] + c + word[i + 1:]
                    if w in words or w == beginWord:
                        result.append(w)
            return result

        # BFS to build distances from endWord
        while q:
            word, distance = q.popleft()
            if word == beginWord:
                break
            for w in nextWords(word):
                if w not in dist:
                    dist[w] = distance + 1
                    q.append((w, distance + 1))

        solution = []

        # DFS to construct paths based on BFS distances
        def dfs(word, res):
            if word == endWord:
                solution.append(res[:])
                return
            for w in nextWords(word):
                if w not in dist:
                    continue
                if dist[w] == dist[word] - 1:  # only consider next distance word
                    res.append(w)
                    dfs(w, res)
                    res.pop()

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

from typing import List, Set, Dict
import string

class LongestWordChain:
    def __init__(self):
        self.cache = {}

    def chain_from_sub(self, word: str, all_words: Set[str], chain_length: int) -> int:
        """
        Recursive function to find the longest chain using the subtraction method.
        Removes one character at a time from the word and checks if the resulting word is in the dictionary.
        Uses memoization to avoid recalculating results for the same word.

        :param word: The current word being processed
        :param all_words: Set of valid words (dictionary)
        :param chain_length: Current length of the chain
        :return: Maximum chain length for the given word
        """
        if word in self.cache:
            return self.cache[word] + chain_length - 1

        max_chain_length = 0
        for i in range(len(word)):
            new_word = word[:i] + word[i + 1:]
            if new_word in all_words:
                current_chain_length = self.chain_from_sub(new_word, all_words, chain_length + 1)
                max_chain_length = max(max_chain_length, current_chain_length)

        self.cache[word] = max_chain_length
        return max_chain_length

    def longest_subword_chain_sub(self, words: List[str]) -> int:
        """
        Finds the longest significant word chain using the subtraction approach.

        :param words: List of words in the dictionary
        :return: Length of the longest chain
        """
        all_words = set(words)
        max_chain_length = 0
        self.cache = {}

        for word in words:
            current_chain_length = self.chain_from_sub(word, all_words, 1)
            max_chain_length = max(max_chain_length, current_chain_length)

        return max_chain_length

    def chain_from_add(self, word: str, all_words: Set[str], chain_length: int) -> int:
        """
        Recursive function to find the longest chain using the addition method.
        Adds each character in every position in the word and checks if the resulting word is in the dictionary.

        :param word: The current word being processed
        :param all_words: Set of valid words (dictionary)
        :param chain_length: Current length of the chain
        :return: Maximum chain length for the given word
        """
        if word in self.cache:
            return self.cache[word] + chain_length - 1

        max_chain_length = chain_length
        for i in range(len(word) + 1):
            for a in string.ascii_lowercase:
                new_word = word[:i] + a + word[i:]
                if new_word in all_words:
                    current_chain_length = self.chain_from_add(new_word, all_words, chain_length + 1)
                    max_chain_length = max(max_chain_length, current_chain_length)

        self.cache[word] = max_chain_length
        return max_chain_length

    def longest_subword_additive(self, words: List[str]) -> int:
        """
        Finds the longest significant word chain using the addition approach.

        :param words: List of words in the dictionary
        :return: Length of the longest chain
        """
        all_words = set(words)
        max_chain_length = 0
        self.cache = {}

        for word in words:
            current_chain_length = self.chain_from_add(word, all_words, 1)
            max_chain_length = max(max_chain_length, current_chain_length)

        return max_chain_length
def main():
    # Sample word list with possible word chains
    words = ["a", "i", "in", "sin", "sing", "sting", "string", "staring", "starling", "at", "sat", "stat", "state", "estate", "restate", "restated", "restarted"]

    # Instantiate the class
    lsw = LongestWordChain()

    # Test subtraction method
    longest_chain_sub = lsw.longest_subword_chain_sub(words)
    print("Longest chain length using subtraction method:", longest_chain_sub)

    # Test addition method
    longest_chain_add = lsw.longest_subword_additive(words)
    print("Longest chain length using addition method:", longest_chain_add)

# Run the main function
if __name__ == "__main__":
    main()

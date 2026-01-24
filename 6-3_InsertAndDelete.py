import random
from collections import defaultdict
from typing import List


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []  # List to store elements
        self.table = {}  # Dictionary to store the index of each element in the list

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.table:
            return False  # Value already exists in the set
        # Insert value into the list and store its index in the table
        self.data.append(val)
        self.table[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.table:
            return False  # Value not found in the set
        # Get the index of the element to remove and the last element in the list
        removed_idx = self.table[val]
        last_idx = len(self.data) - 1
        last_element = self.data[last_idx]

        # Move the last element to the place of the element to be removed
        self.data[removed_idx] = last_element
        self.table[last_element] = removed_idx

        # Remove the last element from the list and delete the element from the table
        self.data.pop()
        del self.table[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.data) - 1)  # Generate a random index
        return self.data[idx]

def main():
    # Create an instance of RandomizedSet
    randomized_set = RandomizedSet()

    # Test Case 1: Insertions
    print("Insert 1:", randomized_set.insert(1))  # Expected: True
    print("Insert 2:", randomized_set.insert(2))  # Expected: True
    print("Insert 3:", randomized_set.insert(3))  # Expected: True
    print("Insert 2 (again):", randomized_set.insert(2))  # Expected: False (already exists)

    # Test Case 2: Removals
    print("Remove 2:", randomized_set.remove(2))  # Expected: True
    print("Remove 2 (again):", randomized_set.remove(2))  # Expected: False (already removed)

    # Test Case 3: GetRandom
    print("Random Element:", randomized_set.getRandom())  # Should return a random element from [1, 3]

    # Test Case 4: Edge Case - Single Element
    print("Remove 3:", randomized_set.remove(3))  # Expected: True
    print("Random Element with one element left (1):", randomized_set.getRandom())  # Expected: 1

    # Test Case 5: Empty after Removal
    print("Remove 1:", randomized_set.remove(1))  # Expected: True
    # At this point, the set should be empty; inserting new elements should work as expected
    print("Insert 4:", randomized_set.insert(4))  # Expected: True
    print("Random Element:", randomized_set.getRandom())  # Expected: 4

main()


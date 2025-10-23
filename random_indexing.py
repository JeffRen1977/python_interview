import collections
import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        # Define one hash map, which stores the index position of each element
        self.nums = collections.defaultdict(list)
        # Iterate each element in the array
        for index, ele in enumerate(nums):
            # For each element, add the corresponding index position in the hash map.
            self.nums[ele].append(index)

    def pick(self, target: int) -> int:
        # Call python function random.choice()
        return random.choice(self.nums[target])


# Functionality to select K items randomly from a stream
def printArray(stream, n):
    for i in range(n):
        print(stream[i], end=" ")
    print()


def selectKItems(stream, n, k):
    # Reservoir [] is the output array. Initialize it with the first k elements of stream[].
    reservoir = [0] * k
    for i in range(k):
        reservoir[i] = stream[i]

    # Iterate the Nth element after k+1 elements.
    for i in range(k, n):
        # Pick up a random index between [0, i+1].
        j = random.randrange(i + 1)
        # If random index is less than k, the elements present in the index are replaced with new ones in the stream
        if j < k:
            reservoir[j] = stream[i]

    print("Following are k randomly selected items:")
    printArray(reservoir, k)


# Main Functions
if __name__ == "__main__":
    # Test the Solution class
    nums = [1, 2, 3, 3, 3]
    solution = Solution(nums)

    # Testing pick method
    print("Picking index for target 3 (should return 2, 3, or 4):")
    for _ in range(5):
        print(solution.pick(3))

    print("Picking index for target 1 (should return 0):")
    print(solution.pick(1))

    # Test reservoir sampling
    stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(stream)
    k = 5
    selectKItems(stream, n, k)

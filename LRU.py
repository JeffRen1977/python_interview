from collections import deque


class LRUCache:
    def __init__(self, capacity: int) -> None:
        """
        Initialize the LRUCache with a given capacity.
        """
        self.capacity = capacity  # Maximum number of items the cache can hold
        self.list = deque(maxlen=capacity)  # Doubly-ended queue to keep track of usage order
        self.items = {}  # Dictionary to store key-value pairs for constant-time access

    def get(self, key: int) -> int:
        """
        Retrieve the value of the key if it exists in the cache; otherwise, return -1.
        If the key exists, it is moved to the end to mark it as recently used.
        """
        if key not in self.items:
            return -1  # Key not found in cache

        # Remove the key from its current position in the list and append it to the end
        self.list.remove(key)
        self.list.append(key)

        return self.items[key]  # Return the value associated with the key

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the value for the given key.
        If the cache reaches its capacity, the least recently used item is removed.
        """
        if key in self.items:
            # If the key is already in the cache, update its value and move it to the end
            self.list.remove(key)
            self.list.append(key)
            self.items[key] = value
            return

        # If the cache is at full capacity, remove the least recently used item
        if len(self.items) == self.capacity:
            lru_key = self.list.popleft()  # Remove the least recently used item (first item in the list)
            del self.items[lru_key]  # Delete it from the hash table

        # Add the new key-value pair to the cache and list
        self.list.append(key)
        self.items[key] = value


def main():
    # Initialize the LRUCache with a capacity of 2
    cache = LRUCache(2)

    # Perform operations as described in the example
    cache.put(1, 1)  # Cache: {1:1}
    cache.put(2, 2)  # Cache: {1:1, 2:2}

    # Get the value for key 1; expect 1
    print("Get 1:", cache.get(1))  # Returns 1; Cache: {2:2, 1:1}

    # Insert key 3 with value 3; evicts key 2
    cache.put(3, 3)  # Cache: {1:1, 3:3}

    # Get the value for key 2; expect -1 as it was evicted
    print("Get 2:", cache.get(2))  # Returns -1 (not found)

    # Insert key 4 with value 4; evicts key 1
    cache.put(4, 4)  # Cache: {3:3, 4:4}

    # Get the value for key 1; expect -1 as it was evicted
    print("Get 1:", cache.get(1))  # Returns -1 (not found)

    # Get the value for key 3; expect 3
    print("Get 3:", cache.get(3))  # Returns 3; Cache: {4:4, 3:3}

    # Get the value for key 4; expect 4
    print("Get 4:", cache.get(4))  # Returns 4; Cache: {3:3, 4:4}


main()

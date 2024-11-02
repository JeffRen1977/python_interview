class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to k.
        """
        self.data = [0] * k
        self.head = 0
        self.tail = 0
        self.size = 0  # Tracks the current number of elements in the queue
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        """
        Inserts elements into a circular queue. If the operation succeeds, true is returned.
        """
        if self.isFull():
            return False
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Deletes an element from the loop queue. If the operation succeeds, true is returned.
        """
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the top item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.data[(self.tail - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Check if the recurrence queue is empty.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Check if the recurring queue is full.
        """
        return self.size == self.capacity


def main():
    queue = MyCircularQueue(3)
    print(queue.enQueue(1))    # Expected: True
    print(queue.enQueue(2))    # Expected: True
    print(queue.enQueue(3))    # Expected: True
    print(queue.enQueue(4))    # Expected: False (Queue is full)
    print(queue.Rear())        # Expected: 3
    print(queue.isFull())      # Expected: True
    print(queue.deQueue())     # Expected: True
    print(queue.enQueue(4))    # Expected: True
    print(queue.Rear())        # Expected: 4

    # Additional test cases
    print(queue.Front())       # Expected: 2
    print(queue.deQueue())     # Expected: True
    print(queue.deQueue())     # Expected: True
    print(queue.isEmpty())     # Expected: False
    print(queue.deQueue())     # Expected: True
    print(queue.isEmpty())     # Expected: True
    print(queue.deQueue())     # Expected: False (Queue is already empty)

if __name__ == "__main__":
    main()

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next  # Move slow pointer by 1 step
            fast = fast.next.next  # Move fast pointer by 2 steps
            if slow == fast:  # Check if they meet
                return True  # Cycle detected
        return False  # No cycle detected


def test_hasCycle():
    # Helper function to create a cycle in the linked list
    def createLinkedListWithCycle(values, pos):
        head = ListNode(values[0])
        current = head
        cycle_node = None

        # Creating the linked list
        for i in range(1, len(values)):
            new_node = ListNode(values[i])
            current.next = new_node
            current = new_node
            if i == pos:
                cycle_node = new_node

        # Creating the cycle
        if cycle_node:
            current.next = cycle_node

        return head

    # Test Case 1: Cycle exists
    head = createLinkedListWithCycle([3, 2, 0, -4], 1)
    solution = Solution()
    assert solution.hasCycle(head) == True, "Test Case 1 Failed"

    # Test Case 2: No cycle
    head = createLinkedListWithCycle([1, 2, 3, 4], -1)
    assert solution.hasCycle(head) == False, "Test Case 2 Failed"

    # Test Case 3: Single node with a cycle
    head = createLinkedListWithCycle([1], 0)
    assert solution.hasCycle(head) == False, "Test Case 3 Failed"

    # Test Case 4: Single node without a cycle
    head = createLinkedListWithCycle([1], -1)
    assert solution.hasCycle(head) == False, "Test Case 4 Failed"

    print("All test cases passed!")


# Run the test function
test_hasCycle()

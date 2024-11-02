class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Hash table to store the mapping from original nodes to their copies
        table = {}

        # Create the copy of the head node
        table[head] = Node(head.val)

        # Initialize the current node pointer
        curr = head

        # Iterate through the list and copy the nodes
        while curr:
            copy = table[curr]

            # Copy the next pointer
            if curr.next is not None:
                if curr.next not in table:
                    table[curr.next] = Node(curr.next.val)
                copy.next = table[curr.next]

            # Copy the random pointer
            if curr.random is not None:
                if curr.random not in table:
                    table[curr.random] = Node(curr.random.val)
                copy.random = table[curr.random]

            # Move to the next node in the original list
            curr = curr.next

        # Return the copied head node
        return table[head]


def test_copyRandomList():
    # Helper function to create a linked list with random pointers
    def create_linked_list_with_random_pointers(values, random_indices):
        if not values:
            return None

        nodes = [Node(val) for val in values]
        head = nodes[0]

        # Set the next pointers
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        # Set the random pointers
        for i, random_index in enumerate(random_indices):
            nodes[i].random = nodes[random_index] if random_index is not None else None

        return head

    # Helper function to compare two linked lists with random pointers
    def compare_linked_lists(head1, head2):
        while head1 and head2:
            if head1.val != head2.val or (head1.random and head2.random and head1.random.val != head2.random.val):
                return False
            if (head1.random is None) != (head2.random is None):  # one random is None and the other is not
                return False
            head1 = head1.next
            head2 = head2.next
        return head1 is None and head2 is None

    solution = Solution()

    # Test Case 1: Standard Case
    head = create_linked_list_with_random_pointers([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
    copied_head = solution.copyRandomList(head)
    assert compare_linked_lists(head, copied_head), "Test Case 1 Failed"

    # Test Case 2: Single Node with random pointer to itself
    head = create_linked_list_with_random_pointers([7], [0])
    copied_head = solution.copyRandomList(head)
    assert compare_linked_lists(head, copied_head), "Test Case 2 Failed"

    # Test Case 3: Empty List
    head = None
    copied_head = solution.copyRandomList(head)
    assert copied_head == None, "Test Case 3 Failed"

    # Test Case 4: All random pointers as None
    head = create_linked_list_with_random_pointers([1, 2, 3, 4], [None, None, None, None])
    copied_head = solution.copyRandomList(head)
    assert compare_linked_lists(head, copied_head), "Test Case 4 Failed"

    print("All test cases passed!")


# Run the test function
test_copyRandomList()

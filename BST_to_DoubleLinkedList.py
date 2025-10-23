class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        # Step 1: Perform in-order traversal and collect nodes in a list
        res = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node)
            inorder(node.right)

        inorder(root)  # Start in-order traversal from the root

        # Step 2: Link nodes to form a circular doubly linked list
        for i in range(len(res) - 1):
            res[i].right = res[i + 1]  # Point current node's right to next node
            res[i + 1].left = res[i]  # Point next node's left to current node

        # Step 3: Connect the head and tail to form a circular list
        res[-1].right = res[0]  # Last node's right points to the first node
        res[0].left = res[-1]  # First node's left points to the last node

        return res[0]  # Return the head of the circular doubly linked list


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_doubly_linked_list(head):
    # Helper function to print the doubly linked list in a circular manner
    if not head:
        return "Empty list"
    result = []
    current = head
    while True:
        result.append(current.val)
        current = current.right
        if current == head:
            break
    return " <-> ".join(map(str, result))


def test_tree_to_doubly_list():
    # Create a BST
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    # Initialize Solution
    solution = Solution()

    # Convert BST to sorted circular doubly linked list
    head = solution.treeToDoublyList(root)

    # Print the result in a circular linked list format
    print("Doubly Linked List:", print_doubly_linked_list(head))


# Run the test function
test_tree_to_doubly_list()

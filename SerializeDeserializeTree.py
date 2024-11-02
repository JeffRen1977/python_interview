class Codec:
    def dfs(self, s):
        # Pop the first element in the list
        first = s.pop(0)

        # If it's "#", it represents a NULL node, so return None
        if first == "#":
            return None

        # Create a new TreeNode with the current value
        root = TreeNode(int(first))

        # Recursively set the left and right children
        root.left = self.dfs(s)
        root.right = self.dfs(s)

        return root

    def serialize(self, root):
        # Base case for a null node
        if root is None:
            return "#,"

        # Convert the root value to a string and recursively serialize left and right children
        return str(root.val) + "," + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        # Split the serialized data into a list of node values
        s = data.split(',')

        # Start the DFS deserialization process
        root = self.dfs(s)

        return root


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def test_codec():
    # Create a binary tree
    #       1
    #      / \
    #     2   3
    #        / \
    #       4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Initialize Codec
    codec = Codec()

    # Test Serialization
    serialized = codec.serialize(root)
    print("Serialized Tree:", serialized)  # Expected: "1,2,#,#,3,4,#,#,5,#,#"

    # Test Deserialization
    deserialized_root = codec.deserialize(serialized)

    # Helper function to validate the tree structure by serializing again
    serialized_again = codec.serialize(deserialized_root)
    print("Serialized Again after Deserialization:", serialized_again)

    # Check if the serialized string before and after deserialization is the same
    assert serialized == serialized_again, "Error: The tree structure does not match after deserialization."
    print("The tree structure is preserved after deserialization.")


# Run the test function
test_codec()

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case: If root is None, return None (no ancestor found here)
        if root is None:
            return None

        # If the current node is either p or q, we return this node
        if root is p or root is q:
            return root

        # Recursively search the left subtree for p or q
        left = self.lowestCommonAncestor(root.left, p, q)

        # Recursively search the right subtree for p or q
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, it means p and q are found in
        # different subtrees, so root is their lowest common ancestor
        if left and right:
            return root

        # If only one side (left or right) is non-null, return that side's result
        # This indicates that both p and q are found on the same side
        elif left:
            return left
        else:
            return right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def test_lowest_common_ancestor():
    # Create nodes for the binary tree
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    # Create an instance of the Solution class
    solution = Solution()

    # Test Case 1: LCA of nodes 5 and 1 should be 3
    p, q = root.left, root.right  # Nodes 5 and 1
    lca = solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 3, f"Expected LCA: 3, Got: {lca.val}"
    print(f"LCA of {p.val} and {q.val} is {lca.val}")

    # Test Case 2: LCA of nodes 5 and 4 should be 5
    p, q = root.left, root.left.right.right  # Nodes 5 and 4
    lca = solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 5, f"Expected LCA: 5, Got: {lca.val}"
    print(f"LCA of {p.val} and {q.val} is {lca.val}")

    # Test Case 3: LCA of nodes 7 and 8 should be 3
    p, q = root.left.right.left, root.right.right  # Nodes 7 and 8
    lca = solution.lowestCommonAncestor(root, p, q)
    assert lca.val == 3, f"Expected LCA: 3, Got: {lca.val}"
    print(f"LCA of {p.val} and {q.val} is {lca.val}")


# Run the test function
test_lowest_common_ancestor()

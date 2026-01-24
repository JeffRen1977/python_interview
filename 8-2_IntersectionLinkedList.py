
    # Definition for singly-linked list.
class ListNode(object):
      def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes_in_listA = set()

        # Traverse the first linked list and store each node in the set
        while headA:
            nodes_in_listA.add(headA)
            headA = headA.next

        # Traverse the second linked list to find the intersection
        while headB:
            if headB in nodes_in_listA:
                return headB  # Found the intersection node
            headB = headB.next

        return None  # No intersection found


def test_getIntersectionNode():
    # Helper function to create linked lists with intersection
    def create_linked_lists_with_intersection(intersection_val, listA_vals, listB_vals):
        intersect_node = None
        headA = ListNode(0)
        currentA = headA

        # Create the first list
        for val in listA_vals:
            new_node = ListNode(val)
            currentA.next = new_node
            currentA = new_node
            if val == intersection_val:
                intersect_node = new_node

        headB = ListNode(0)
        currentB = headB

        # Create the second list
        for val in listB_vals:
            if val == intersection_val:
                currentB.next = intersect_node
                break
            new_node = ListNode(val)
            currentB.next = new_node
            currentB = new_node

        return headA.next, headB.next, intersect_node

    solution = Solution()

    # Test Case 1: Lists intersect
    headA, headB, intersect_node = create_linked_lists_with_intersection(8, [4, 1, 8, 4, 5], [5, 0, 1, 8, 4, 5])
    assert solution.getIntersectionNode(headA, headB) == intersect_node, "Test Case 1 Failed"

    # Test Case 2: No intersection
    headA, headB, _ = create_linked_lists_with_intersection(-1, [1, 2, 3], [4, 5, 6])
    assert solution.getIntersectionNode(headA, headB) == None, "Test Case 2 Failed"

    # Test Case 3: One list is empty
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headB = None
    assert solution.getIntersectionNode(headA, headB) == None, "Test Case 3 Failed"

    # Test Case 4: Same list
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headB = headA
    assert solution.getIntersectionNode(headA, headB) == headA, "Test Case 4 Failed"

    print("All test cases passed!")


# Run the test function
test_getIntersectionNode()

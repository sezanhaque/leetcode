import sys
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Imagine the following example:
            1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3
        the list with loop. Idea is to use two pointers,
        one is slow and one is fast, let us do several steps:

        1.  At the beginning, both of them at number 1.
        2.  Next step, slow pointer at 2 and fast at 3.
        3.  Next step, slow pointer at 3 and fast at 5.
        4.  Next step, slow pointer at 4 and fast at 3.
        5.  Next step, slow pointer at 5 and fast is also 5,
            so we have the same element, and we return True.

        If we do not have looped we will never have equal elements, if we have looped,
        because slow pointer moves with speed 1 and fast with speed 2, fast pointer will always gain slow one.

        Complexity:
            Time complexity is O(n),
            Space complexity is O(1).
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        sys.getrefcount(head):

            1 ref comes from the calling of this function itself according to the documentation
            2 Refs from the object being created, compiled and stored for optimization
            1 ref from a node A's next
            1 ref comes from another node B's next [if this happens, then there is a cycle]
        """
        while head:
            if sys.getrefcount(head) > 4:
                return True

            head = head.next

        return False

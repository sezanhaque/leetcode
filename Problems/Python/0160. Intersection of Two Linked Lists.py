from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        1.  Store all the elements of headA in a hashset
        2.  Iterate through the headB and check for the first match and then return it.

        Time - O(n+m)
        Space - O(n)
        """
        seen = set()
        curr = headA

        while curr:
            seen.add(curr)
            curr = curr.next

        curr = headB
        while curr:
            if curr in seen:
                return curr
            curr = curr.next

        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Two Pointers approach

        We will initialize two pointers which is pointing to head of each Linked_List.
        Then we will make these pointers run through both the Linked Lists n + m length.
        By doing so, we will hit an intersection point.

        Time - O(n+m)
        Space - O(1)
        """
        one, two = headA, headB

        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next

        return one

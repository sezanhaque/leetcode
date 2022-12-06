# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        START WITH BASIC EVEN AND ODD POSITIONS,
        FOR NEXT ODD APPEND EVENS NEXT AND FOR
        NEXT EVEN APPEND ODDS NEXT
        """

        if not head:
            return head

        odd, even = head, head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head


# 1 -> 2 -> 3 -> 4 -> 5
input = ListNode(
    1,
    ListNode(
        2,
        ListNode(
            3,
            ListNode(4, ListNode(5)),
        ),
    ),
)

print(Solution.oddEvenList(0, input))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        print("Current:", curr.val)
        next = curr.next
        print("Next:", next.val)
        curr.next = prev
        prev = curr
        print("prev:", prev.val)
        curr = next
        print("curr:", curr.val)
    return prev


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
reverseList(0, input)

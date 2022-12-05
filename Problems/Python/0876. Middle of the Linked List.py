# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Linked List
    def middleNode(self, head: list[ListNode]) -> list[ListNode]:
        res = head
        length = 0

        while head:
            head = head.next
            length += 1
        mid = length >> 1

        while mid:
            res = res.next
            mid -= 1

        return res

    def middleNode(self, head: list[ListNode]) -> list[ListNode]:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
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

print(Solution.middleNode(0, input))

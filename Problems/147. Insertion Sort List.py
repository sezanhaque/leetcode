# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(-1)
        curr = head

        while curr:
            curr_next = curr.next
            prv, nxt = dummy, dummy.next

            while nxt:
                if nxt.val > curr.val:
                    break
                prv = nxt
                nxt = nxt.next

            curr.next = nxt
            prv.next = curr
            curr = curr_next

        return dummy.next
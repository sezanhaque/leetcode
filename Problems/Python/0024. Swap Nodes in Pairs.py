from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev, curr, res = None, head, head.next

        while curr and curr.next:
            adj = curr.next

            if prev:
                prev.next = adj

            # swap nodes
            curr.next, adj.next = adj.next, curr

            # go to next nodes
            prev, curr = curr, curr.next

        return res or head

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head = [1,2,3,4]
        # res = [2,1,4,3]
        
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # dummy -> 2, 1 -> 3
            prev.next, curr.next = curr.next, curr.next.next

            # 2 -> 1
            prev.next.next = curr

            # prev = 1, curr = 3
            prev, curr = curr, curr.next

        return dummy.next

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Initial State
        There are 2 pointers named fast and slow pointing to the first node of the Linked List.

    Phase 1
        Move fast k-1 times. Now fast points to the kth node from the beginning.
        Marked this node first.

    Phase 2
        Move fast and slow together until fast points to the last node.
        Now slow points to the kth node from the end.
    """

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Initial State
        slow, fast = head, head

        # Phase 1
        for _ in range(k - 1):
            fast = fast.next
        first = fast

        # Phase 2
        while fast.next:
            slow, fast = slow.next, fast.next

        # Last
        first.val, slow.val = slow.val, first.val

        return head


linkedlist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
obj = Solution()
node = obj.swapNodes(linkedlist, 2)
while node:
    print(node.val)
    node = node.next

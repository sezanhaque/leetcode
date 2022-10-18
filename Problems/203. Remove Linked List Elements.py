class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(self, head: ListNode, val: int) -> ListNode:
    curr = head
    prev = None
    while curr:
        if curr.val != val:
            prev = curr
            curr = curr.next
        else:
            if prev:
                prev.next = curr.next
            else:
                head = curr.next
            curr = curr.next
    return head


# 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
input = ListNode(
    1,
    ListNode(
        2,
        ListNode(
            6,
            ListNode(3, ListNode(4, ListNode(5, ListNode(6)))),
        ),
    ),
)

# 7 -> 7 -> 7 -> 7
input_2 = ListNode(
    7,
    ListNode(
        7,
        ListNode(
            7,
            ListNode(7, ListNode(7)),
        ),
    ),
)
# 1 -> 2 -> 2 -> 1
input_3 = ListNode(
    1,
    ListNode(
        2,
        ListNode(
            2,
            ListNode(1),
        ),
    ),
)
# removeElements(0, input, 6)
# removeElements(0, input_2, 7)
# removeElements(0, input_3, 2)

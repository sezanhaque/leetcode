# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    if left == right:
        return head

    prev = None
    curr = head
    while curr:
        prev = curr
        print("prev:", prev.val)
        print("curr:", curr.val)
        while curr.next and left <= curr.next.val <= right:
            print("left <= curr.val <= right: ", left, curr.next.val, right)
            # prev = curr
            # curr = curr.next
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            continue
        curr = curr.next

    if curr:
        print("curr:", curr.val)
    # print(curr.val)
    # for _ in range(left - 1):
    #     prev = curr
    #     curr = curr.next

    # while curr:
    #     if curr.val <= left:
    #         # prev = curr
    #         # curr = curr.next
    #         next = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next
    #     elif curr.val <= right:
    #         curr = curr.next
    # print(curr.val)


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
reverseBetween(0, input, 2, 4)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(self, head: ListNode) -> ListNode:
    """
    This solution sort the Linked list perfectly but it occurs "Time limit exceeded" error.
    """
    curr = head
    while curr:
        index = curr.next
        while index:
            if curr.val > index.val:
                curr.val, index.val = index.val, curr.val
            index = index.next
        curr = curr.next

    # print("*" * 20)
    # while head:
    #     print(head.val)
    #     head = head.next
    return head


def sortList(self, head: ListNode) -> ListNode:
    curr = head
    new_list = []
    while curr:
        new_list.append(curr.val)
        curr = curr.next
    new_list.sort()
    curr = head
    for i in range(len(new_list)):
        curr.val = new_list[i]
        curr = curr.next
    # print("*" * 20)
    # while head:
    #     print(head.val)
    #     head = head.next
    return head


# 4 -> 2 -> 1 -> 3
input = ListNode(
    4,
    ListNode(
        2,
        ListNode(
            1,
            ListNode(3),
        ),
    ),
)
input2 = ListNode()

input3 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))

# print(sortList(0, input))
# print(sortList(0, input2))
print(sortList(0, input3))

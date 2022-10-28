class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    """Iteration"""

    # create dummy node so we can compare the first node in each list
    head = ListNode(0)

    # initialise current node pointer
    curr = head

    # while the lists are valid
    while list1 and list2:
        # if the value in list1 is less than the value in list2
        if list1.val < list2.val:
            # the next node in the list will be the list1 node
            curr.next = list1
            # move the list1 pointer to the next node
            list1 = list1.next

        # if not then the next node in the list will be the list2 node
        else:
            curr.next = list2
            list2 = list2.next
        # move the current pointer to the next node
        curr = curr.next

    # if list1 node is valid but not list2 node add the rest of the nodes from list1
    # if list2 node is valid but not list1 node add the rest of the nodes from list2
    curr.next = list1 or list2

    return head.next


def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    """Recursion"""
    if list1 and list2:
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1.next = mergeTwoLists(0, list1.next, list2)
    return list1 or list2


l1 = ListNode(
    0,
    ListNode(
        3,
        ListNode(7, ListNode(11, ListNode(15))),
    ),
)
l2 = ListNode(
    1,
    ListNode(
        2,
        ListNode(
            4,
            ListNode(6, ListNode(8, ListNode(10, ListNode(12)))),
        ),
    ),
)

print(mergeTwoLists(0, l1, l2))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value):
        self.size += 1
        newNode = ListNode(value)
        if not self.head:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.val)
            currentNode = currentNode.next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # print(divmod(18, 10))
    carry = 0
    head = ListNode(0)
    current = head
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        current.next = ListNode(carry % 10)
        current = current.next
        carry //= 10

    # for printing purpose
    head = head.next
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)
    # for printing purpose

    # return head.next


l1 = ListNode(
    9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
)
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

addTwoNumbers(0, l1, l2)

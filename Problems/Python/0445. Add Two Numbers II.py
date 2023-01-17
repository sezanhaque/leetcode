from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1, str2 = "", ""

        while l1:
            str1 += str(l1.val)
            l1 = l1.next

        while l2:
            str2 += str(l2.val)
            l2 = l2.next

        sums = str(int(str1) + int(str2))
        res = head = ListNode(0)

        for char in sums:
            res.next = ListNode(int(char))
            res = res.next

        return head.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1, st2 = [], []
        while l1:
            st1.append(l1.val)
            l1 = l1.next

        while l2:
            st2.append(l2.val)
            l2 = l2.next

        carry, head = 0, None

        while st1 or st2 or carry:
            d1, d2 = 0, 0
            d1 = st1.pop() if st1 else 0
            d2 = st2.pop() if st2 else 0
            carry, digit = divmod(d1 + d2 + carry, 10)
            head_new = ListNode(digit)
            head_new.next = head
            head = head_new

        return head


linkedlist = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
linkedlist2 = ListNode(5, ListNode(6, ListNode(4)))

obj = Solution()
node = obj.addTwoNumbers(linkedlist, linkedlist2)
while node:
    print(node.val)
    node = node.next

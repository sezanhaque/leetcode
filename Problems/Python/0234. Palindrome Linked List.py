# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(self, head: ListNode) -> bool:
    string_head = ""
    while head:
        string_head += str(head.val)
        head = head.next
    return string_head == string_head[::-1]


input = ListNode(
    1,
    ListNode(
        2,
        ListNode(
            2,
            ListNode(1),
        ),
    ),
)
print(isPalindrome(0, input))

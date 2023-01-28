from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def toArray(self, head: ListNode, arr: List) -> List:
        # convert a linked list to an array
        while head:
            arr.append(head.val)
            head = head.next
        return arr

    def arrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # same as LeetCode Problem 108

        if not nums:
            return None

        mid = len(nums) >> 1

        return TreeNode(val=nums[mid], left=self.arrayToBST(nums[:mid]),
                        right=self.arrayToBST(nums[mid + 1:]))

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.arrayToBST(self.toArray(head, []))

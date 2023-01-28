from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    As the list is sorted, so the middle element will be the root of a binary tree.
    So we will divide and go to left and right and again divide them.
    """

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) >> 1

        return TreeNode(val=nums[mid], left=self.sortedArrayToBST(nums[:mid]),
                        right=self.sortedArrayToBST(nums[mid + 1:]))


nums = [-10, -3, 0, 5, 9]
obj = Solution()
print(obj.sortedArrayToBST(nums))

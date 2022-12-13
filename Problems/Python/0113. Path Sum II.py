# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        self.res = []
        self.findPath(root, targetSum, [])
        return self.res

    def findPath(self, root: Optional[TreeNode], targetSum: int, arr: list[int]):
        if not root:
            return

        arr.append(root.val)

        # If there is no child node and current sum == current root value
        # it means we have found our ans, so append it to res and return
        if not root.left and not root.right and targetSum == root.val:
            self.res.append(arr)
            return

        targetSum -= root.val
        self.findPath(root.left, targetSum, arr[:])
        self.findPath(root.right, targetSum, arr[:])

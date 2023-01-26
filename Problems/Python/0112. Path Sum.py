# Definition for a binary tree node.
from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # If there is no child node and current sum == current root value
        # it means we have found our ans, so return True
        if not root.left and not root.right and root.val == targetSum:
            return True

        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )


root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
targetSum = 22
obj = Solution()
print(obj.hasPathSum(BinaryTree(root).root_node, targetSum))

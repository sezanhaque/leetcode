# Definition for a binary tree node.
from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaf(node) -> list[int]:
            if not node:
                return []

            if not node.left and not node.right:
                return [node.val]

            return getLeaf(node.left) + getLeaf(node.right)

        return getLeaf(root1) == getLeaf(root2)


root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
obj = Solution()
print(obj.leafSimilar(BinaryTree(root1).root_node, BinaryTree(root2).root_node))

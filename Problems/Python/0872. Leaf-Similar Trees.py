# Definition for a binary tree node.
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

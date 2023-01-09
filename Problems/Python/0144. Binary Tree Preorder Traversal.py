# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def DFS(node: TreeNode) -> None:
            if not node:
                return

            # Visit root first, then the left subtree, then the right subtree.
            res.append(node.val)
            DFS(node.left)
            DFS(node.right)

        DFS(root)

        return res

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are null then return True
        if not p and not q:
            return True

        # If anyone is null then return False
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        # traverse from left to right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

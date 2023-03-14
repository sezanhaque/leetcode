# Definition for a binary tree node.
from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


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


p, q = [1, 2, 3], [1, 2, 3]
obj = Solution()
print(obj.isSameTree(BinaryTree(p).root_node, BinaryTree(q).root_node))

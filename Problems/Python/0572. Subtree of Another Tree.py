from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # This is the solution of LeetCode Problem 100: Same Tree
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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def DFS(node: TreeNode) -> bool:
            if not node:
                return False

            if self.isSameTree(node, subRoot):
                return True

            return DFS(node.left) or DFS(node.right)

        return DFS(root)


root, subRoot = [3, 4, 5, 1, 2], [4, 1, 2]
obj = Solution()
print(obj.isSubtree(BinaryTree(root).root_node, BinaryTree(subRoot).root_node))

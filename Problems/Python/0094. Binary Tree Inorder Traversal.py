from typing import Optional, List

# Definition for a binary tree node.
from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    In inorder, the order should be
        left -> root -> right
    """

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def DFS(node: TreeNode):
            if node:
                DFS(node.left)
                res.append(node.val)
                DFS(node.right)

        DFS(root)
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if root is None else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


root = [1, None, 2, 3]
obj = Solution()
print(obj.inorderTraversal(BinaryTree(root).root_node))

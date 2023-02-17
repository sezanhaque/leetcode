from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        if root.left is None and root.right is None:
            return str(root.val)

        # pre-order traversal
        res = str(root.val)
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        res += "(" + left + ")"
        if right != "":
            res += "(" + right + ")"

        return res


root = [1, 2, 3, 4]
obj = Solution()
print(obj.tree2str(BinaryTree(root).root_node))

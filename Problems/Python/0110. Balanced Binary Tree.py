from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.balance = True

    def DFS(self, node: TreeNode):
        if not node:
            return 0

        left, right = self.DFS(node.left), self.DFS(node.right)

        if abs(left - right) > 1:
            self.balance = False

        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.DFS(root)
        return self.balance


root = [3, 9, 20, None, None, 15, 7]
obj = Solution()
print(obj.isBalanced(BinaryTree(root).root_node))

from typing import Optional, List

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    In postorder, the order should be
        left -> right -> root
    """

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if root is None else self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [
            root.val]


root = [1, None, 2, 3]
obj = Solution()
print(obj.postorderTraversal(BinaryTree(root).root_node))

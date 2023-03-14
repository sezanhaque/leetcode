from typing import Optional, List

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


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

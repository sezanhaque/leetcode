from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
        if not root:
            return True
        if not low < root.val < high:
            return False
        return self.isValidBST(root.left, low, root.val) and \
               self.isValidBST(root.right, root.val, high)


root = [2, 1, 3]
root2 = [5, 1, 4, None, None, 3, 6]

obj = Solution()
print(obj.isValidBST(BinaryTree(root).root_node))
print(obj.isValidBST(BinaryTree(root2).root_node))

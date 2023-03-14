from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # if we have left & right then get the min from them
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

        # else get the min from one of them
        return 1 + self.minDepth(root.left or root.right)


root = [3, 9, 20, None, None, 15, 7]
obj = Solution()
print(obj.minDepth(BinaryTree(root).root_node))

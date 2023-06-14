from typing import List, Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = self.inorder(root)
        return min(nums[i + 1] - nums[i] for i in range(len(nums) - 1))

    def inorder(self, root: TreeNode) -> List[int]:
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []


root = [1, 0, 48, None, None, 12, 49]
obj = Solution()
print(obj.getMinimumDifference(BinaryTree(root).root_node))

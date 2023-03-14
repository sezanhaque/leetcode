from typing import Optional
from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def DFS(curr: TreeNode, num: int) -> int:
            # if there is no node
            if not curr:
                return 0

            num = num * 10 + curr.val

            # if this is a leaf node
            if not curr.left and not curr.right:
                return num

            return DFS(curr.left, num) + DFS(curr.right, num)

        return DFS(root, 0)


obj = Solution()
root = [4, 9, 0, 5, 1]
print(obj.sumNumbers(BinaryTree(root).root_node))

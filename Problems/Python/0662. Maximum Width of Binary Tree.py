from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import TreeNode, BinaryTree


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        queue = [(root, 0)]

        while queue:
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            temp = []

            for node, level in queue:
                if node.left:
                    temp.append((node.left, 2 * level))
                if node.right:
                    temp.append((node.right, 2 * level + 1))

            queue = temp

        return res


root = [1, 3, 2, 5, 3, None, 9]
obj = Solution()
print(obj.widthOfBinaryTree(BinaryTree(root).root_node))

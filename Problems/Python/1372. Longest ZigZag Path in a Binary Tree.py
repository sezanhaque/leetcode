from typing import Optional, List

from Data_Structures_Algorithms.Tree.BinaryTree import TreeNode, BinaryTree


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def DFS(node: TreeNode) -> List:
            if not node:
                return [-1, -1, -1]

            left_subtree, right_subtree = DFS(node.left), DFS(node.right)

            # left_subtree[1] + 1 => right node of left subtree
            # right_subtree[0] + 1 => left node of right subtree
            # max(left_subtree[1] + 1, right_subtree[0] + 1, left_subtree[2], right_subtree[2])
            # => max between both of them with max length of zigzag path found so far

            return [
                left_subtree[1] + 1,
                right_subtree[0] + 1,
                max(left_subtree[1] + 1, right_subtree[0] + 1, left_subtree[2], right_subtree[2])
            ]

        return DFS(root)[-1]


root = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1]
obj = Solution()
print(obj.longestZigZag(BinaryTree(root).root_node))

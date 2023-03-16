from collections import deque
from typing import Optional, List

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()

            if node:
                # entry new list for current level
                if level == len(res):
                    res.append([])

                res[level].append(node.val)
                queue.extend([(node.left, level + 1), (node.right, level + 1)])

        return res[::-1]


obj = Solution()
root = [3, 9, 20, None, None, 15, 7]
obj.levelOrderBottom(BinaryTree(root).root_node)

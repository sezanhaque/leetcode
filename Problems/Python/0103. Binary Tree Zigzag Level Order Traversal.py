from collections import deque
from typing import Optional, List

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root] if root else [])

        while queue:
            level = []

            for idx in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level = reversed(level) if len(res) & 1 else level
            res.append(level)

        return res


root = [3, 9, 20, None, None, 15, 7]
obj = Solution()
print(obj.zigzagLevelOrder(BinaryTree(root).root_node))

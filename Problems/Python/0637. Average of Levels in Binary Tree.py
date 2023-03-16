from collections import deque
from typing import Optional, List

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        res = []

        while queue:
            level, sums = len(queue), 0

            # loop through every node of the level
            # and add their value to sums
            # then divide the sums by level
            for _ in range(len(queue)):
                node = queue.popleft()
                sums += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(sums / level)

        return res


obj = Solution()
root = [3, 9, 20, None, None, 15, 7]
obj.averageOfLevels(BinaryTree(root).root_node)

from collections import deque
from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    """
    If we find any node after any empty node then
    the tree will not be a complete binary tree.
    """

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                queue.extend([node.left, node.right])
            else:
                # we have found an empty node
                while queue:
                    # now checking if there is
                    # any node, if so then return False
                    if queue.popleft():
                        return False

        return True


obj = Solution()
root = [1, 2, 3, 4, 5, 6]
print(obj.isCompleteTree(BinaryTree(root).root_node))

from collections import deque
from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([(root.left, root.right), ])

        while queue:
            node1, node2 = queue.popleft()

            # if both of them are None
            # continue
            if not node1 and not node2:
                continue

            # if either of them are None
            # return False
            if not node1 or not node2:
                return False

            # if their values are not same
            # return False
            if node1.val != node2.val:
                return False

            # to create mirror effect we are traversing from
            # left to right and right to left and compare their values
            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isSame(root.left, root.right)

    def isSame(self, leftRoot: TreeNode, rightRoot: TreeNode) -> bool:
        if not leftRoot and not rightRoot:
            return True

        if not leftRoot or not rightRoot:
            return False

        if leftRoot.val != rightRoot.val:
            return False

        return self.isSame(leftRoot.left, rightRoot.right) and self.isSame(leftRoot.right, rightRoot.left)


root = [1, 2, 2, 3, 4, 4, 3]
obj = Solution()
print(obj.isSymmetric(BinaryTree(root).root_node))

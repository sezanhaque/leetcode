from collections import deque
from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    # DFS Recursive
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

    # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        if root:
            queue.append(root)

        level = 0

        while queue:
            for idx in range(len(queue)):
                node: TreeNode = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return level


root = [3, 9, 20, None, None, 15, 7]
obj = Solution()
print(obj.maxDepth(BinaryTree(root).root_node))

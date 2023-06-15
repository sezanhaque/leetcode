from collections import deque
from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # BFS

        level = maxLevel = 0
        maxSum = -float('inf')

        queue = deque()
        queue.append(root)

        while queue:
            level += 1
            currSum = 0

            for _ in range(len(queue)):
                node: TreeNode = queue.popleft()
                currSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if maxSum < currSum:
                maxSum, maxLevel = currSum, level

        return maxLevel


root = [989, None, 10250, 98693, -89388, None, None, None, -32127]
obj = Solution()
print(obj.maxLevelSum(BinaryTree(root).root_node))

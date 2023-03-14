from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def __init__(self):
        # stores the maximum diameter calculated
        self.diameter = 0

    def DFS(self, node: Optional[TreeNode]) -> int:
        """
        This function needs to do the following:
            1. Calculate the maximum depth of the left and right sides of the given node
            2. Determine the diameter at the given node and check if its the maximum
        """
        if not node:
            return 0

        # Calculate maximum depth
        left, right = self.DFS(node.left), self.DFS(node.right)

        # Calculate diameter
        self.diameter = max(self.diameter, left + right)

        # Make sure the parent node(s) get the correct depth from this node
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.DFS(root)
        return self.diameter


root = [1, 2, 3, 4, 5]
obj = Solution()
print(obj.diameterOfBinaryTree(BinaryTree(root).root_node))

from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def DFS(node_1: TreeNode, node_2: TreeNode, level: int) -> None:
            if node_1 is None or node_2 is None:
                return

            # when the level is odd, swap the values
            if level & 1:
                node_1.val, node_2.val = node_2.val, node_1.val

            # The key to using dfs is to pass in the left of node1 and right of node2.
            # And then, pass in the right of node1 and left of node 2.
            # These two nodes (node1.left and node2.right) or (node1.right and node2.left)
            DFS(node_1.left, node_2.right, level + 1)
            DFS(node_1.right, node_2.left, level + 1)

        DFS(root.left, root.right, 1)

        return root


root = [2, 3, 5, 8, 13, 21, 34]
obj = Solution()
tree = BinaryTree(root)
tree.root_node = obj.reverseOddLevels(tree.root_node)
tree.print_recursive(tree.root_node)

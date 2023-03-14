from typing import Optional, List

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    """
    In preorder, the order should be
        root -> left -> right
    """

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def DFS(node: TreeNode) -> None:
            if not node:
                return

            # Visit root first, then the left subtree, then the right subtree.
            res.append(node.val)
            DFS(node.left)
            DFS(node.right)

        DFS(root)

        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if root is None else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(
            root.right)


root = [1, None, 2, 3]
obj = Solution()
print(obj.preorderTraversal(BinaryTree(root).root_node))

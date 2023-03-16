from typing import Optional, List

from Data_Structures_Algorithms.Tree.BinaryTree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: idx for idx, val in enumerate(inorder)}

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            root = TreeNode(preorder.pop(0))

            idx = inorder_idx[root.val]

            root.left = helper(left, idx - 1)
            root.right = helper(idx + 1, right)

            return root

        return helper(0, len(inorder) - 1)


obj = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
obj.buildTree(preorder, inorder)

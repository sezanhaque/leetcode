from typing import Optional, List

from Data_Structures_Algorithms.Tree.BinaryTree import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: idx for idx, val in enumerate(inorder)}

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # always current root will be the last
            # value of the postorder list
            root = TreeNode(postorder.pop())

            idx = inorder_idx[root.val]

            # first build right tree using postorder
            root.right = helper(idx + 1, right)
            # secondly build left tree
            root.left = helper(left, idx - 1)

            return root

        return helper(0, len(inorder) - 1)


obj = Solution()
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
obj.buildTree(inorder, postorder)

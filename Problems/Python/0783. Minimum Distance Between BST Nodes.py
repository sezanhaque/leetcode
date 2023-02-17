from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    In a sorted array, difference between 2 adjacent values will be minimum.
    So, we should only check 2 adjacent values and traverse.

    A binary search tree is also sorted if we traverse in-order.

    In-order traversal: left -> node -> right
    """

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, res = float('-inf'), float('inf')

        def DFS(curr_node: TreeNode):
            nonlocal prev, res

            if curr_node:
                DFS(curr_node.left)

                res = min(res, curr_node.val - prev)
                prev = curr_node.val

                DFS(curr_node.right)

        DFS(root)

        return res


root = [4, 2, 6, 1, 3]
obj = Solution()
print(obj.minDiffInBST(BinaryTree(root).root_node))

from typing import Optional

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        # When value is less than low, everything on it's left doesn't matter,
        # so only return the sum from its right children
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)

        # Same thing for high.
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)

        # The current value is in the range, so return the sum of its left, right and own value
        return (
                root.val
                + self.rangeSumBST(root.left, low, high)
                + self.rangeSumBST(root.right, low, high)
        )


root = [10, 5, 15, 3, 7, None, 18]
obj = Solution()
print(obj.rangeSumBST(BinaryTree(root).root_node, 7, 15))

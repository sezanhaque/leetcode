from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Here what we need to do is just use definition of inverted tree.
    We go from top to bottom of our tree and if we reached the leaf, we do not do anything.
    If current subtree is not a leaf, we recursively call our function for both its children,
    first inverting them.

    Complexity is O(h), where h is the height of our tree.
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

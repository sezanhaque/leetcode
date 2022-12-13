from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = -inf
        self.helper(root)
        return self.maxPath

    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Get the max path from left side
        left = max(self.helper(root.left), 0)

        # Get the max path from right side
        right = max(self.helper(root.right), 0)

        # Update the maxPath with current sub tree paths (left + root + right)
        # it is a rounded path, so we are not returning it, just updating with maxPath
        self.maxPath = max(self.maxPath, left + right + root.val)

        # We are returning only current root value with left or right max value
        return root.val + max(left, right)

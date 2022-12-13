# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.maxProd = treeSum = 0

        def totalSum(root: TreeNode) -> int:
            if not root:
                return 0

            # If we divide a tree into left and right
            # and we have the total tree sum
            # then the right sum will be total sum - left sum
            subTreeSum = root.val + totalSum(root.left) + totalSum(root.right)
            self.maxProd = max(self.maxProd, subTreeSum * (treeSum - subTreeSum))

            return subTreeSum

        treeSum = totalSum(root)
        totalSum(root)

        return self.maxProd % (10**9 + 7)

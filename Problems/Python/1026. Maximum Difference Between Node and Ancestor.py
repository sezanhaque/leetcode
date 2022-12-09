# Definition for a binary tree node.
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Time Complexity : O(N)
Space Complexity : O(H)
For all of these solutions
"""


class Solution:
    def maxAncestorDiff(self, root):
        """
        Solution - I (PostOrder DFS - Bottom-up Approach)

        We need to find the Maximum Absolute Difference (MAB) |a - b| where a is an ancestor of b.

        The MAB for a given ancestor a can be either a - minChild or maxChild - a and we will
        consider the maximum amongst it. Taking absolute difference between any other child value
        would always give a lesser value. So, we solve this problem recursively using DFS as follows -

        Recurse the left and right subtree and find the minimum and maximum value of child in both these subtree.
        Let curMin be minimum of all children and curMax be maximum of all children. The final ans will be updated
        as max of ans, a - curMin and curMax - a, where a is current root's value

        Finally the recursive call will return the minimum and maximum value amongst all child nodes including
        root to the above level.

        In this approach, since we are first recursing down the subtree and then updating ans by considering
        the root's value, it can be said as a Post-order Bottom-up DFS approach.

        In the below code, I have updated curMin & curMax by also taking root's value. It just avoids writing
        extra conditions for leaf nodes and also doesn't affect ans if we update curMin by including root or not.
        """
        self.ans = 0

        def dfs(root):
            if not root:
                return inf, -inf
            leftMin, leftMax = dfs(root.left)
            rightMin, rightMax = dfs(root.right)
            curMin, curMax = min(root.val, leftMin, rightMin), max(
                root.val, leftMax, rightMax
            )
            self.ans = max(self.ans, root.val - curMin, curMax - root.val)
            return curMin, curMax

        dfs(root)
        return self.ans


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]):
        """
        Solution - II (PreOrder DFS - Top-Down Approach)

        We can solve it using a slightly different DFS approach as well.
        The problem can be interpreted as finding maximum absolute difference
        between a node and any of its ancestor nodes (we did the other way around in above approach).
        Thus, this approach can be stated as -

        Maintain two variables curMin and curMax denoting minimum and maximum of ancestors nodes till now.
        Each recursive call, ans will be updated as max of ans, b - curMin and curMax - b, where b is current node's value.
        We update curMin and curMax by including current node's value (as it will be ancestor for following nodes) and
        recurse for left and right subtree.

        In this approach, since we are updating ans and curMin / curMax first by current node's value and then recursing
        down the subtree, we can call this approach as Pre-order Top-down DFS approach.
        """
        self.ans = 0

        def dfs(root, curMin, curMax):
            if root:
                self.ans = max(self.ans, abs(root.val - curMin), abs(curMax - root.val))
                curMin, curMax = min(curMin, root.val), max(curMax, root.val)
                dfs(root.left, curMin, curMax)
                dfs(root.right, curMin, curMax)

        dfs(root, root.val, root.val)
        return self.ans


class Solution:
    def maxAncestorDiff(self, root, curMin=inf, curMax=-inf):
        """
        *** Fast ***
        Solution - III (Slightly Optimized DFS)

        We can optimize the above approach by reducing the number of updating
        that we perform for ans. We were going down each root-to-leaf path
        and updating ans as maximum absolute difference between current
        node and min/max ancestors till now.

        Instead of updating it in each recursive call, we can simply maintain
        min and max values all the way down a path and finally return difference
        between max and min nodes. Each time, we will return the maximum of
        difference returned from both left and right paths. For a given path,
        one must be ancestor and other must be child node and thus this approach
        would give the correct answer while minimizing the number of comparisons
        and updating.
        """
        if not root:
            return curMax - curMin
        curMin, curMax = min(curMin, root.val), max(curMax, root.val)
        return max(
            self.maxAncestorDiff(root.left, curMin, curMax),
            self.maxAncestorDiff(root.right, curMin, curMax),
        )

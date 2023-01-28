class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # recursion
        if not root:
            return 0

        return 1 + max((self.maxDepth(node) for node in root.children), default=0)

    def maxDepth(self, root: 'Node') -> int:
        # DFS
        if not root:
            return 0

        depth, level = 1, 0

        def DFS(node: 'Node', depth: int):
            nonlocal level

            if not node.children:
                level = max(level, depth)

            if node.children:
                for child in node.children:
                    DFS(child, depth + 1)

        DFS(root, depth)
        return level

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    """
    Preorder traversal:
        root -> left -> right
    """
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        res = []

        def DFS(currNode: 'Node'):
            res.append(currNode.val)
            for child in currNode.children:
                DFS(child)

        DFS(root)
        return res

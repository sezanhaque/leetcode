from typing import List

from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    """
    Post order traverse:
        left -> right -> root
    """

    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        res = []

        def DFS(currNode: 'Node'):
            for child in currNode.children:
                DFS(child)
            res.append(currNode.val)

        DFS(root)
        return res

from typing import List
from Data_Structures_Algorithms.Helper.Messages import MESSAGE


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.val


class BinaryTree:
    """
    Generate a binary tree from list.

    This will build in BFS way.
    From root -> left -> right
    """

    def __init__(self, elements: List):
        if elements:
            self.root_node = TreeNode(elements[0])
            nodes = [self.root_node]

            for idx, num in enumerate(elements[1:]):
                if num is None:
                    continue

                parent_node = nodes[idx >> 1]
                is_left = (not idx & 1)
                node = TreeNode(val=num)

                if is_left:
                    parent_node.left = node
                else:
                    parent_node.right = node

                nodes.append(node)
        else:
            raise Exception(MESSAGE.empty.value)

    def __repr__(self):
        self.print_recursive(self.root_node)

    def print_recursive(self, tree: TreeNode, level=0, prefix="root"):
        print(f"{level * '  '}{prefix:5s}: val={tree.val}")

        if tree.left:
            self.print_recursive(tree.left, level + 1, "left")
        if tree.right:
            self.print_recursive(tree.right, level + 1, "right")


# root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
# obj = BinaryTree(root)
# obj.__repr__()

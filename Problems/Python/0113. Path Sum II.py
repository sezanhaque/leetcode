from typing import Optional
from Data_Structures_Algorithms.Tree.BinaryTree import BinaryTree, TreeNode


class Solution:
    def __init__(self):
        self.res = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        self.findPath(root, targetSum, [])
        return self.res

    def findPath(self, root: Optional[TreeNode], targetSum: int, arr: list[int]):
        if not root:
            return

        arr.append(root.val)

        # If there is no child node and current sum == current root value
        # it means we have found our ans, so append it to res and return
        if not root.left and not root.right and targetSum == root.val:
            self.res.append(arr)
            return

        targetSum -= root.val
        self.findPath(root.left, targetSum, arr[:])
        self.findPath(root.right, targetSum, arr[:])


if __name__ == "__main__":
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    targetSum = 22
    obj = Solution()
    print(obj.pathSum(BinaryTree(root).root_node, targetSum))

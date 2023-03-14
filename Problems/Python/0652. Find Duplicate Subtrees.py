from collections import defaultdict
from typing import Optional, List
from Data_Structures_Algorithms.Tree.BinaryTree import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def DFS(node: TreeNode):
            if not node:
                return "null"

            string = ",".join([str(node.val), DFS(node.left), DFS(node.right)])

            # if current occurrence is already 1
            # it means we have a duplicate
            if len(sub_trees[string]) == 1:
                res.append(node)

            sub_trees[string].append(node)
            return string

        sub_trees = defaultdict(list)
        res = []
        DFS(root)
        return res

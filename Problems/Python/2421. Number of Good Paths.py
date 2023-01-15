from collections import Counter
from typing import List


class Solution:
    """
    Intuition
        1.  All single node are considered as a good path.

        2.  Take a look at the biggest value maxv
            If the number of nodes with the biggest value maxv is k,
            then good path starting with value maxv is k*(k-1)/2,
            any pair can build up a good path.
            And these nodes will cut the tree into small trees.

    Explanation
        We do the "cutting" process reversely by union-find.

        Firstly we initialize result res = length,
        we union the edge with small values v.

        Then the nodes of value v on one side,
        can pair up with the nodes of value v on the other side.

        We union one node into the other by union action,
        and also the count of nodes with value v.

        We're repeatedly doing union action for all edges until we build up the whole tree.

    Complexity
        Time O(union-find(n))
        Space O(union-find(n))
    """

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        res = length = len(vals)

        # to track which node is parent of which in union find
        parents = list(range(length))

        count = [Counter({vals[i]: 1}) for i in range(length)]
        edges = sorted([max(vals[i], vals[j]), i, j] for i, j in edges)

        def find(x: int) -> int:
            """
            Find the parent of a node in Union find
            """
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        for v, i, j in edges:
            parent_i, parent_j = find(i), find(j)
            count_j, count_i = count[parent_i][v], count[parent_j][v]
            res += count_i * count_j
            parents[parent_j] = parent_i
            count[parent_i] = Counter({v: count_i + count_j})

        return res


obj = Solution()
print(obj.numberOfGoodPaths(vals=[1, 3, 2, 1, 3], edges=[[0, 1], [0, 2], [2, 3], [2, 4]]))

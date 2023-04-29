from collections import defaultdict
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * n
        ans = [0] * n

        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + n - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans


obj = Solution()
print(obj.sumOfDistancesInTree(n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))

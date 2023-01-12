from collections import defaultdict, Counter
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(list[int])
        res = [0] * n

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def DFS(curr: int, parent: int) -> Counter:
            count = Counter()

            for child in adj[curr]:
                if child != parent:
                    count += DFS(child, curr)

            count[labels[curr]] += 1
            res[curr] = count[labels[curr]]

            return count

        DFS(0, -1)
        return res


obj = Solution()
# print(obj.countSubTrees(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], labels="abaedcd"))
print(obj.countSubTrees(n=4, edges=[[0, 1], [1, 2], [0, 3]], labels="bbbb"))
# print(obj.countSubTrees(n=5, edges=[[0, 1], [0, 2], [1, 3], [0, 4]], labels="aabab"))

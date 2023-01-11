from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list[int])

        # adjacent list from undirected graph
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def DFS(curr: int, parent: int) -> int:
            time = 0

            for child in adj[curr]:
                if child == parent:
                    continue

                time_from_child = DFS(child, curr)

                if time_from_child > 0 or hasApple[child]:
                    time += time_from_child + 2

            return time

        return DFS(0, -1)


obj = Solution()
print(obj.minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                  hasApple=[False, False, True, False, True, True, False]))

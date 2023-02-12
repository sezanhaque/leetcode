import math
from collections import defaultdict
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # create an adjacent list for undirected graph
        adj = defaultdict(list)
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)

        res = 0

        def DFS(curr_node: int, parent: int) -> int:
            nonlocal res
            passengers = 0

            for child in adj[curr_node]:
                if child != parent:
                    curr_passengers = DFS(child, curr_node)
                    passengers += curr_passengers
                    res += int(math.ceil(curr_passengers / seats))

            return passengers + 1

        DFS(0, -1)

        return res


obj = Solution()
print(obj.minimumFuelCost(roads=[[0, 1], [0, 2], [0, 3]], seats=5))

from collections import defaultdict
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # we need minimum n - 1 edges to connect n components
        if len(connections) < n - 1:
            return -1

        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        num_of_connections = 0

        def DFS(node: int) -> None:
            visited.add(node)

            # traverse each neighbor vertex of current node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    DFS(neighbor)

        # loop from 0 to nth node to check
        # how many vertex we can visit
        for node in range(n):
            if node not in visited:
                num_of_connections += 1
                DFS(node)

        return num_of_connections - 1


obj = Solution()
print(obj.makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]))

from collections import defaultdict, deque
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for a, b, distance in roads:
            graph[a][b] = graph[b][a] = distance

        min_score = float('inf')
        visited = set()
        queue = deque([1])

        while queue:
            node = queue.popleft()

            for adj, score in graph[node].items():
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)
                min_score = min(min_score, score)

        return min_score


obj = Solution()
print(obj.minScore(n=4, roads=[[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))

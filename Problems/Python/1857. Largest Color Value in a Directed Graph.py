from collections import defaultdict
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        def DFS(node: int):
            if node in path:
                return float('inf')
            if node in visited:
                return 0

            visited.add(node)
            path.add(node)

            # map a -> 0, b -> 1......z -> 25
            color_idx = ord(colors[node]) - ord('a')
            count[node][color_idx] = 1

            for neighbor in adj[node]:
                if DFS(neighbor) == float('inf'):
                    return float('inf')

                for char in range(26):
                    count[node][char] = max(count[node][char], (1 if char == color_idx else 0) + count[neighbor][char])

            path.remove(node)
            return max(count[node])

        n, res = len(colors), 0
        visited, path = set(), set()

        # map count[node][color] -> max freq color
        count = [[0] * 26 for _ in range(n)]

        for i in range(n):
            res = max(res, DFS(i))

        return -1 if res == float('inf') else res


obj = Solution()
print(obj.largestPathValue(colors="abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]]))

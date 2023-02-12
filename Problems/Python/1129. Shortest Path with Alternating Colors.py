from collections import defaultdict, deque
from typing import List


class Solution:
    # BFS
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1 for _ in range(n)]

        red = defaultdict(list)
        blue = defaultdict(list)

        for src, dst in redEdges:
            red[src].append(dst)

        for src, dst in blueEdges:
            blue[src].append(dst)

        queue = deque()
        # node, length, prev_edge_color
        queue.append([0, 0, None])

        visited = set()
        # node, edge_color
        visited.add((0, None))

        while queue:
            node, length, prev_edge_color = queue.popleft()

            if res[node] == -1:
                res[node] = length

            # if prev color is Blue
            # then go to Red neighbor
            if prev_edge_color != "RED":
                for neighbor in red[node]:
                    if (neighbor, "RED") not in visited:
                        visited.add((neighbor, "RED"))
                        queue.append([neighbor, length + 1, "RED"])

            # if prev color is Red
            # then go to Blue neighbor
            if prev_edge_color != "BLUE":
                for neighbor in blue[node]:
                    if (neighbor, "BLUE") not in visited:
                        visited.add((neighbor, "BLUE"))
                        queue.append([neighbor, length + 1, "BLUE"])

        return res


obj = Solution()
print(obj.shortestAlternatingPaths(n=3, redEdges=[[0, 1], [1, 2]], blueEdges=[]))

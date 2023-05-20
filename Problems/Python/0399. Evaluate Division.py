from collections import defaultdict, deque
from itertools import permutations
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Map a -> list of [b, a/b]
        adj = defaultdict(list)
        for idx, equ in enumerate(equations):
            a, b = equ
            adj[a].append([b, values[idx]])
            adj[b].append([a, 1 / values[idx]])

        def BFS(src: str, target: str) -> int:
            if src not in adj or target not in adj:
                return -1

            queue, visited = deque(), set()
            queue.append([src, 1])
            visited.add(src)

            while queue:
                node, w = queue.popleft()
                if node == target:
                    return w

                for nei, weight in adj[node]:
                    if nei not in visited:
                        queue.append([nei, w * weight])
                        visited.add(nei)

            return -1

        return [BFS(q[0], q[1]) for q in queries]

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build the graph
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 / val

        def DFS(x: str, y: str, graph: defaultdict, visited: set):
            visited.add(x)
            for n in graph[x]:
                if n == y:
                    return graph[x][n]
                elif n not in visited:
                    val = DFS(n, y, graph, visited)
                    if val != -1.0:
                        return graph[x][n] * val
            return -1.0

        # Answer the queries
        res = []
        for x, y in queries:
            if x not in graph or y not in graph:
                res.append(-1.0)
            elif x == y:
                res.append(1.0)
            else:
                visited = set()
                res.append(DFS(x, y, graph, visited))
        return res

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        quot = defaultdict(dict)

        for (num, den), val in zip(equations, values):
            quot[num][num] = quot[den][den] = 1.0
            quot[num][den] = val
            quot[den][num] = 1 / val

        for k, i, j in permutations(quot, 3):
            if k in quot[i] and j in quot[k]:
                quot[i][j] = quot[i][k] * quot[k][j]

        return [quot[num].get(den, -1.0) for num, den in queries]


obj = Solution()
print(obj.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                       queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))

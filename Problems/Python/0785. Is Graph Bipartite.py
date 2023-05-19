from collections import deque


class Solution:
    def isBipartite(self, graph):
        n, colored = len(graph), {}

        for i in range(n):
            if i not in colored and graph[i]:
                colored[i] = 1
                queue = deque([i])

                while queue:
                    cur = queue.popleft()
                    for nb in graph[cur]:
                        if nb not in colored:
                            colored[nb] = -colored[cur]
                            queue.append(nb)
                        elif colored[nb] == colored[cur]:
                            return False
        return True


obj = Solution()
print(obj.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))

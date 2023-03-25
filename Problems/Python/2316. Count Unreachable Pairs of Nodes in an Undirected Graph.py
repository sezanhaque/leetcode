from collections import defaultdict, deque
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # check from current node
        # how many nodes we can reach
        def DFS(node: int) -> int:
            # if we visited already then
            # we need not visit it again
            if node in visited:
                return 0

            visited.add(node)
            res = 1

            # DFS the neighbors of current node
            for neighbor in graph[node]:
                res += DFS(neighbor)

            return res

        def BFS(node: int):
            queue = deque([node])
            res = 0

            while queue:
                curr_node = queue.popleft()
                if curr_node in visited:
                    continue

                res += 1
                visited.add(curr_node)
                for _ in graph[curr_node]:
                    queue.append(_)

            return res

        # 4, 2, 1
        components = []
        # 7
        total_sum = 0

        for node in range(n):
            total_reach = DFS(node)
            if total_reach:
                total_sum += total_reach
                components.append(total_reach)

        # Get the pair of components
        # 4 * 1 + 4 * 2 + 1 * 2 = 14
        # 4 ( 1 + 2 ) + 1 * 2 = 14

        # how many pairs we can make
        # with current num
        # to find out the total number of pairs, we know:
        # n * (n - 1) // 2
        # sum((total_sum - num) * num) // 2
        return sum((total_sum - num) * num for num in components) >> 1

    # Short version
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def DFS(node: int) -> int:
            visited.add(node)
            return sum(DFS(neighbor) for neighbor in graph[node] if neighbor not in visited) + 1

        return sum((lambda x: (n - x) * x)(DFS(num)) for num in range(n) if num not in visited) >> 1


obj = Solution()
print(obj.countPairs(n=7, edges=[[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))

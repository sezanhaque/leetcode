from collections import defaultdict, deque
from typing import List
from functools import cache

class Solution:
    """
    There is a bidirectional graph, which means we can traverse from a to b and b to vertices.

    Solution: DFS

        1.  First we create a hashmap "graph" to store the edges from a vertex.

        2.  Use a boolean array "visited" to track visited nodes.

        3.  Start the search from node "source".

            *   If source == destination then we have found our path.
                return True.
            *   If source not in visited, make it visited and traverse its all nodes.
    """

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # to store edges
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # track visited nodes
        visited = [False] * n

        @cache
        def dfs(curr_node: int) -> bool:
            # we have found our path
            if curr_node == destination:
                return True

            # if current node is not visited
            # make it true and traverse its nodes
            if not visited[curr_node]:
                visited[curr_node] = True

                for node in graph[curr_node]:
                    if dfs(node):
                        return True

            return False

        return dfs(source)


obj = Solution()

print(obj.validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))



class Solution:
    """
    There is a bidirectional graph, which means we can traverse from a to b and b to vertices.

    Solution: BFS

        1.  First we create a hashmap "graph" to store the edges from a vertex.

        2.  Use a boolean array "visited" to track visited nodes.

        3.  Initialize an empty queue (queue) to store the nodes to be visited.

        4.  If queue has value then get the first node and make it visited.

        5.  Go to the neighbours of current nodes and add them to queue
            and make them visited.

        6.  Repeat it until we have found the destination.
    """

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # to store all edges in the graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # track visited nodes
        visited = [False] * n
        visited[source] = True

        queue = deque([source])

        while queue:
            curr_node = queue.popleft()

            if curr_node == destination:
                return True

            # For all the neighbours of the current node,
            # if we haven't visited it before, make it visited
            # and add it to queue
            for node in graph[curr_node]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)

        return False


obj = Solution()

print(obj.validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))
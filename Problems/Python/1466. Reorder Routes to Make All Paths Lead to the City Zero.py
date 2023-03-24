from collections import defaultdict, deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # DFS Solution
        # how many roads need to change to reach city 0
        changes = 0

        roads = set()
        neighbors = defaultdict(list)
        for a, b in connections:
            roads.add((a, b))
            neighbors[a].append(b)
            neighbors[b].append(a)

        def DFS(city: int, neighbor: int) -> None:
            nonlocal changes

            # if neighbor -> city path is as same as
            # city -> neighbor path in roads then
            # we need to change its direction

            # Ex: If you neighbor: 0 & city: 4
            # and we have 4 -> 0 in roads
            # then we need to change it into
            # 0 -> 4 direction
            changes += (neighbor, city) in roads

            # check every neighbor of current city
            # if they are connected to 0 or not
            for new_neighbor in neighbors[city]:
                if new_neighbor != neighbor:
                    DFS(new_neighbor, city)

        DFS(0, -1)
        return changes

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # BFS Solution
        # how many roads need to change to reach child 0
        changes = 0

        roads = set()
        neighbors = defaultdict(list)
        for a, b in connections:
            roads.add((a, b))
            neighbors[a].append(b)
            neighbors[b].append(a)

        queue = deque([0])
        visited = {0}

        while queue:
            city = queue.popleft()

            for neighbor in neighbors[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    changes += (city, neighbor) in roads
                    queue.append(neighbor)

        return changes


obj = Solution()
print(obj.minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))

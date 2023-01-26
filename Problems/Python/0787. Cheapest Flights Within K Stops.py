from collections import defaultdict, deque
from math import inf
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for source, destination, cost in flights:
            adj[source].append([destination, cost])

        queue = deque([(src, 0)])
        minCost = [inf for _ in range(n)]
        steps = 0

        while queue and steps <= k:
            # iterate through every neighbor of current city
            for _ in range(len(queue)):
                # get the city and cost
                city, cost = queue.popleft()
                # find the neighbor of current city from adj list
                for neighbor, price in adj[city]:
                    if price + cost >= minCost[neighbor]:
                        continue

                    minCost[neighbor] = price + cost
                    queue.append((neighbor, minCost[neighbor]))

            steps += 1

        return minCost[dst] if minCost[dst] != inf else -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Bellman-ford algorithm

        O(k*E)T O(V)S
        """
        # by default, we are initializing every cost as inf
        cost = defaultdict(lambda: inf)

        # starting cost is 0
        cost[src] = 0

        for _ in range(k + 1):
            # create a copy of current cost
            _cost = cost.copy()
            for source, destination, price in flights:
                if _cost[destination] > cost[source] + price:
                    _cost[destination] = cost[source] + price

            # update the modified cost
            cost = _cost

        return cost[dst] if cost[dst] != inf else -1


obj = Solution()
print(
    obj.findCheapestPrice(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0, dst=3,
                          k=1))

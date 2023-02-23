import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # track affordable projects
        max_profit = []
        min_capital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_capital)

        for _ in range(k):
            # while project capital is less than or equal to
            # our current capital
            while min_capital and min_capital[0][0] <= w:
                # pop the minimum cost project
                c, p = heapq.heappop(min_capital)

                # add the min cost project to max profit
                # by default in python heap is min heap
                # to use it as max heap we are multiplying
                # with -1
                heapq.heappush(max_profit, -1 * p)

            if not max_profit:
                break
            
            # pop the max profit and add it
            w += -1 * heapq.heappop(max_profit)

        return w


obj = Solution()
print(obj.findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))

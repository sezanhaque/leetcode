from typing import List


class Solution:
    """
    If we iterate from end of the list then we can decide for idx
    which one is min between next 2 indexes

    By this way we can reach first of the index and min cost will
    be between 0, 1 index
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for idx in range(len(cost) - 3, -1, -1):
            cost[idx] += min(cost[idx + 1], cost[idx + 2])

        return min(cost[0], cost[1])


obj = Solution()
print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

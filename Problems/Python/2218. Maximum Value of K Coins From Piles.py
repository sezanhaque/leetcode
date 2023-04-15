from functools import cache
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def DP(i: int, pile: int):
            if pile == 0 or i == len(piles):
                return 0

            res, cur = DP(i + 1, pile), 0

            for j in range(min(len(piles[i]), pile)):
                cur += piles[i][j]
                res = max(res, cur + DP(i + 1, pile - j - 1))

            return res

        return DP(0, k)


obj = Solution()
print(obj.maxValueOfCoins(piles=[[1, 100, 3], [7, 8, 9]], k=2))

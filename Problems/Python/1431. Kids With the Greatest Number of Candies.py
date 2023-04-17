from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)
        max_candy = max(candies)

        for idx, candy in enumerate(candies):
            if candy + extraCandies >= max_candy:
                res[idx] = True

        return res

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [(candy + extraCandies) >= max_candy for candy in candies]


obj = Solution()
print(obj.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))

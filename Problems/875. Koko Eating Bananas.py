from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Binary Search
        """
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) >> 1

            if sum(ceil(pile / mid) for pile in piles) > h:
                left = mid + 1
            else:
                right = mid
        return left


print(Solution.minEatingSpeed(0, [3, 6, 7, 11], 8))  # 4
print(Solution.minEatingSpeed(0, [30, 11, 23, 4, 20], 5))  # 30

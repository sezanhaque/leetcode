from itertools import accumulate
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        res = prefix = 0

        for num in sorted(nums, reverse=True):
            prefix += num
            res += prefix > 0

        return res


class Solution2:
    def maxScore(self, nums: List[int]) -> int:
        return sum(num > 0 for num in accumulate(sorted(nums, reverse=True)))


obj = Solution()
obj2 = Solution2()
print(obj.maxScore([2, -1, 0, 1, -3, 3, -3]))
print(obj2.maxScore([-2, -3, 0]))

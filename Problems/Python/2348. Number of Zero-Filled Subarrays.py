from itertools import groupby
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0

        for num, group in groupby(nums):
            if not num:
                n = len(list(group))
                res += (n * (n + 1)) >> 1

        return res

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = count = 0

        for num in nums:
            if num:
                count = 0
            else:
                count += 1
            res += count

        return res


obj = Solution()
print(obj.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]))

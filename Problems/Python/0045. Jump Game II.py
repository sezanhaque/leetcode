from math import inf
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = left = right = 0

        while right < len(nums) - 1:
            tmp = 0
            for i in range(left, right + 1):
                tmp = max(tmp, i + nums[i])
            left, right = right + 1, tmp
            res += 1

        return res


obj = Solution()
print(obj.jump([2, 3, 1, 1, 4]))

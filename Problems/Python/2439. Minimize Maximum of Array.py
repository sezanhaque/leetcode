from typing import List
from itertools import accumulate


class Solution:
    """
    To get ceil, we are using (num + idx) // (idx + 1)
    also we can use math.ceil(num / idx)
    """
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total_sum = res = 0

        for idx, num in enumerate(nums):
            total_sum += num
            res = max(res, (total_sum + idx) // (idx + 1))

        return int(res)

    def minimizeArrayValue(self, nums: List[int]) -> int:
        return max((num + idx) // (idx + 1) for idx, num in enumerate(accumulate(nums)))


obj = Solution()
print(obj.minimizeArrayValue([3, 7, 1, 6]))

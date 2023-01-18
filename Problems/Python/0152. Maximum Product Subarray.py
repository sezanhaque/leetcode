from math import inf
from typing import List


class Solution:
    """
    Kadane's algorithm
    """

    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix, maxProduct = 0, 0, -inf

        for idx in range(len(nums)):
            prefix = (prefix or 1) * nums[idx]
            suffix = (suffix or 1) * nums[~idx]
            maxProduct = max(maxProduct, prefix, suffix)

        return maxProduct


obj = Solution()
print(obj.maxProduct([2, 3, -2, 4]))  # 6
print(obj.maxProduct([-2, 0, -1]))  # 0
print(obj.maxProduct([-3, -1, -1]))  # 3
print(obj.maxProduct([0, 2]))  # 2
print(obj.maxProduct([3, -1, 4]))  # 4
print(obj.maxProduct([-2, 3, -4]))  # 24
print(obj.maxProduct([2, -5, -2, -4, 3]))  # 24

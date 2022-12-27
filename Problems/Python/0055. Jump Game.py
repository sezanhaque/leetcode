from functools import cache
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DP
        # Time limit exceeded

        @cache
        def solve(idx: int) -> bool:
            if idx >= len(nums) - 1:
                return True

            for i in range(1, nums[idx] + 1):
                if solve(idx + i):
                    return True

            return False

        return solve(0)

    def canJump(self, nums: List[int]) -> bool:
        """
        To traverse all index, we need all previous index + value > current value.

        Ex: nums = [3, 2, 1, 0,4]
            for idx = 0 and res = 0
                res = max(res, idx + val) = max(0, 0 + 3) = 3

            for idx = 1 res = 3
                res = max(res, idx + val) = max(3, 1 + 2) = 3

            for idx = 2 res = 3
                res = max(res, idx + val) = max(3, 1 + 2) = 3

            for idx = 3 res = 3
                res = max(res, idx + val) = max(3, 3 + 0) = 3

            for idx = 4 res = 3
                Here idx > res, it means we can't traverse all indexes.
                So return False.
        """
        res = 0

        for idx, val in enumerate(nums):
            if idx > res:
                return False
            res = max(res, idx + val)

        return True


obj = Solution()
print(obj.canJump([2,3,1,1,4]))
print(obj.canJump([3,2,1,0,4]))
print(obj.canJump([2, 0, 0]))
from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def Backtrack(subset: []):
            if len(subset) == len(nums):
                res.append(subset)

            for num in nums:
                if num not in visited:
                    visited.add(num)
                    Backtrack(subset + [num])
                    visited.remove(num)

        Backtrack([])
        return res


obj = Solution()
print(obj.permute([1, 2, 3]))

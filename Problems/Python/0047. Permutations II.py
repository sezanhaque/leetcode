from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        counter = Counter(nums)

        def Backtracking(subset: List):
            if len(subset) == len(nums):
                res.append(subset)

            for key in counter:
                if counter[key]:
                    counter[key] -= 1
                    Backtracking(subset + [key])
                    counter[key] += 1

        Backtracking([])
        return res


obj = Solution()
print(obj.permuteUnique([1, 1, 2]))

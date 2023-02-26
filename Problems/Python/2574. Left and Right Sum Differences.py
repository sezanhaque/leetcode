from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        res = []

        for idx, num in enumerate(nums):
            res.append(abs(sum(nums[:idx]) - sum(nums[idx + 1:])))

        return res

    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        return [abs(sum(nums[:idx]) - sum(nums[idx + 1:])) for idx in range(len(nums))]


obj = Solution()
print(obj.leftRigthDifference([10, 4, 8, 3]))

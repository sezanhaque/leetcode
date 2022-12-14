class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [seen[remaining], i]

            seen[value] = i


print(Solution.twoSum(0, [2, 7, 11, 15], 9))

from math import inf


class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        if len(nums) <= 1:
            return 0

        nums.sort()
        ans = nums[k - 1] - nums[0]
        for i in range(k, len(nums)):
            ans = min(ans, nums[i] - nums[i - k + 1])

        return ans

    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        left, right = 0, k - 1
        ans = inf

        while right < len(nums):
            ans = min(ans, nums[right] - nums[left])
            left += 1
            right += 1
        return ans


print(Solution.minimumDifference(0, nums=[9, 4, 1, 7], k=2))

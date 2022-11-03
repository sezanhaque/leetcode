from math import inf


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Sliding Window

        left = sums = 0
        ans = len(nums) + 1

        for right in range(len(nums)):
            sums += nums[right]

            while sums >= target:
                ans = min(ans, right - left + 1)
                sums -= nums[left]
                left += 1

        return ans if ans < len(nums) else 0


print(Solution.minSubArrayLen(0, target=7, nums=[2, 3, 1, 2, 4, 3]))  # 2
print(Solution.minSubArrayLen(0, target=4, nums=[1, 4, 4]))  # 1
print(Solution.minSubArrayLen(0, target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
print(Solution.minSubArrayLen(0, target=11, nums=[1, 2, 3, 4, 5]))  # 3

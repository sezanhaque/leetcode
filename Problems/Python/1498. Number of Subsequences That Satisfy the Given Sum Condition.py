class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        mod = 10**9 + 7

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += pow(2, right - left, mod)
                left += 1

        return count

    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        count = 0
        right = len(nums) - 1
        mod = 10**9 + 7

        for i, left in enumerate(nums):
            while (left + nums[right]) > target and i <= right:
                right -= 1

            if i <= right:
                count += pow(2, right - i, mod)

        return count % mod


print(Solution.numSubseq(0, nums=[3, 5, 6, 7], target=9))

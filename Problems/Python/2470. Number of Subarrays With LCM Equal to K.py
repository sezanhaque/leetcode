import math


class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        res = 0

        for left in range(len(nums)):
            curr = nums[left]
            right = left
            while right < len(nums) and k % nums[right] == 0:
                curr = math.lcm(curr, nums[right])
                if curr > k:
                    break
                elif curr == k:
                    res += 1
                right += 1

        return res


print(Solution.subarrayLCM(0, nums=[3, 6, 2, 7, 1], k=6))  # 4
print(Solution.subarrayLCM(0, nums=[1], k=1))  # 1

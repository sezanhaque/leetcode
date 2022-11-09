import math


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        # Sliding Window

        nums.sort()
        res = []
        l, r = 0, len(nums) - 1

        while len(res) != len(nums):
            res.append(nums[l])
            l += 1

            if l < r:
                res.append(nums[r])
                r -= 1

        return res

    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        half = math.ceil(len(nums) / 2)
        nums[::2], nums[1::2] = nums[:half], nums[half:]
        return nums

    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()

        for i in range(1, len(nums), 2):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums


print(Solution.rearrangeArray(0, [1, 2, 3, 4, 5]))
print(Solution.rearrangeArray(0, [6, 2, 0, 9, 7]))

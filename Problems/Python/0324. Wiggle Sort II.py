import math


class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        print(nums)
        half = math.ceil(len(nums) / 2)
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        print(nums)


print(Solution.wiggleSort(0, [1, 5, 1, 1, 6, 4]))
print(Solution.wiggleSort(0, [4, 5, 5, 6]))  #   [5,6,4,5]

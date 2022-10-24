from turtle import left


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left, right = 0, sum(nums)

        for idx, num in enumerate(nums):
            right -= num
            if left == right:
                return idx
            left += num
        return -1


print(Solution.pivotIndex(0, [1, 7, 3, 6, 5, 6]))
# print(Solution.pivotIndex(0, [1, 2, 3]))
# print(Solution.pivotIndex(0, [2, 1, -1]))

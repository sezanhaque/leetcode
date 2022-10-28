from bisect import bisect_left

class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        length = len(nums)
        if length <= nums[0]:
            return length

        for num in range(1, length + 1):
            idx = bisect_left(nums, num)
            if length - idx == num:
                return num
        return -1


print(Solution.specialArray(0, [3, 5]))
print(Solution.specialArray(0, [0, 4, 3, 0, 4]))

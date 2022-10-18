def maximumProduct(self, nums: list[int]) -> int:
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


# print(maximumProduct(0, [1, 2, 3]))
# print(maximumProduct(0, [-1, -2, -3]))
# print(maximumProduct(0, [1, 2, 3, 4]))
print(maximumProduct(0, [-100, -98, -95, -1, 2, 3, 4]))

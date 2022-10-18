def triangularSum(self, nums: list[int]) -> int:
    n = len(nums)
    while n > 0:
        for i in range(n - 1):
            nums[i] = (nums[i] + nums[i + 1]) % 10
        n -= 1
    return nums[0]


# print(triangularSum(0, [1, 2, 3, 4, 5]))
print(triangularSum(0, [2, 6, 6, 5, 5, 3, 3, 8, 6, 4, 3, 3, 5, 1, 0, 1, 3, 6, 9]))

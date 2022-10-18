def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
    for i in range(k):
        nums.sort()
        nums[0] = -nums[0]
    return sum(nums)


print(largestSumAfterKNegations(0, [4, 2, 3], 1))
print(largestSumAfterKNegations(0, [3, -1, 0, 2], 3))
print(largestSumAfterKNegations(0, [2, -3, -1, 5, -4], 2))

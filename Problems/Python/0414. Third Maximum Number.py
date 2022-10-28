def thirdMax(self, nums: list[int]) -> int:
    nums = sorted(nums)
    iteration = 0
    same = 0
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            iteration += 1
            if iteration == 3:
                return nums[i + 1]
        elif nums[i] == nums[i + 1]:
            same += 1
    return nums[-1] if iteration < 2 else nums[-3 - same]

def thirdMax(self, nums: list[int]) -> int:
    nums = list(set(nums))
    nums.sort(reverse=True)
    return nums[2] if len(nums) >= 3 else nums[0]


print(thirdMax(0, [3, 2, 1]))  # 1
print(thirdMax(0, [1, 1, 2]))  # 2
print(thirdMax(0, [2, 4, 5, 3, 1]))
print(thirdMax(0, [2, 2, 3, 1]))
print(thirdMax(0, [1, 2]))
print(thirdMax(0, [3, 2, 3, 1, 2, 4, 5, 5, 6]))  # 4

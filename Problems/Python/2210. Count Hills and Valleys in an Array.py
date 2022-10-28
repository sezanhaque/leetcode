def countHillValley(self, nums: list[int]) -> int:
    count = 0

    for i in range(1, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] = nums[i - 1]

        if nums[i - 1] < nums[i] > nums[i + 1]:
            count += 1
        if nums[i - 1] > nums[i] < nums[i + 1]:
            count += 1

    return count


# print(countHillValley(0, [2, 4, 1, 1, 6, 5]))
# print(countHillValley(0, [2, 4, 6, 5, 1, 1]))
# print(countHillValley(0, [6, 6, 5, 5, 4, 1]))
print(countHillValley(0, [21, 21, 21, 2, 2, 2, 2, 21, 21, 45]))

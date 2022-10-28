def canBeIncreasing(self, nums: list[int]) -> bool:
    for i in range(len(nums)):
        if isSorted(0, nums[:i] + nums[i + 1:]):
            return True
    return False


def isSorted(self, nums: list[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            return False
    return True


print(canBeIncreasing(0, [1, 2, 10, 5, 7]))
print(canBeIncreasing(0, [2, 3, 1, 2]))
print(canBeIncreasing(0, [1, 1, 1]))
print(canBeIncreasing(0, [105, 924, 32, 968]))  # True

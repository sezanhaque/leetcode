from operator import le


def summaryRanges(self, nums: list[int]) -> list[str]:
    result = []
    left, right = 0, 0
    while right < len(nums):
        if nums[right + 1] == nums[right] + 1:
            right += 1
        else:
            result.append(str(nums[left]) + "->" + str(nums[right]))
            right = right + 1
            left = right
    print(result)

    pass


def summaryRanges(self, nums):
    i, result, length = 0, [], len(nums)

    while i < length:
        left = right = i
        while right < length - 1 and nums[right] + 1 == nums[right + 1]:
            right += 1
        result.append(str(nums[left]) + ("->" + str(nums[right])) * (left != right))
        i = right + 1

    return result


print(summaryRanges(0, [0, 1, 2, 4, 5, 7]))
# print(summaryRanges(0, [0, 2, 3, 4, 6, 8, 9]))

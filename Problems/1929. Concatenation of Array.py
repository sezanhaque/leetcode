def getConcatenation(self, nums: list[int]) -> list[int]:
    nums_length = len(nums)
    ans = [0] * (nums_length * 2)
    for i in range(nums_length):
        ans[i], ans[i + nums_length] = nums[i], nums[i]
    return ans


def getConcatenation(self, nums: list[int]) -> list[int]:
    return nums * 2


print(getConcatenation(0, [1, 2, 1]))
# print(getConcatenation(0, [1,3,2,1]))

def buildArray(self, nums: list[int]) -> list[int]:
    ans = []
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans


def buildArray(self, nums: list[int]) -> list[int]:
    return [nums[i] for i in nums]


print(buildArray(0, [0, 2, 1, 5, 3, 4]))
print(buildArray(0, [5, 0, 1, 2, 3, 4]))

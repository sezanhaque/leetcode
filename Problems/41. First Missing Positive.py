class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        seen = set(nums)

        for i in range(1, len(nums) + 2):
            if i not in seen:
                return i


print(Solution.firstMissingPositive(0, [1, 2, 0]))
print(Solution.firstMissingPositive(0, [3, 4, -1, 1]))
print(Solution.firstMissingPositive(0, [1]))

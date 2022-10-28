class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)


print(Solution.maxProduct(0, [3, 4, 5, 2]))
print(Solution.maxProduct(0, [1, 5, 4, 5]))
print(Solution.maxProduct(0, [3, 7]))

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        """
        the triangle are a≤b≤ca \leq b \leq ca≤b≤c. The necessary and sufficient condition for
        these lengths to form a triangle of non-zero area is a+b > c.
        """
        nums.sort(reverse=True)
        for idx in range(len(nums) - 2):
            if nums[idx] < nums[idx + 1] + nums[idx + 2]:
                return nums[idx] + nums[idx + 1] + nums[idx + 2]
        return 0


print(Solution.largestPerimeter(0, [2, 1, 2]))
print(Solution.largestPerimeter(0, [1, 2, 1]))

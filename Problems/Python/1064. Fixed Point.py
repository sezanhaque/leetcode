class Solution:
    def solve(self, nums):
        result = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1

            if mid == nums[mid]:
                result = mid
                right = mid - 1

            if mid > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return result


print(Solution.solve(0, [-5, -2, 0, 3, 4]))
print(Solution.solve(0, [-5, -4, 0]))
print(Solution.solve(0, [0, 1, 2]))

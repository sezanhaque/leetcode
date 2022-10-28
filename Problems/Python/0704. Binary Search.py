class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Binary Search
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


print(Solution.search(0, [-1, 0, 3, 5, 9, 12], 9))
print(Solution.search(0, [-1, 0, 3, 5, 9, 12], 2))

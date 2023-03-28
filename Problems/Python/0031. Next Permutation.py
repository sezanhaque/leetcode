from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find longest non-increasing suffix
        right = len(nums) - 1
        while right > 0 and nums[right - 1] >= nums[right]:
            right -= 1

        if right == 0:
            return self.reverse(nums, 0, len(nums) - 1)

        # find pivot
        pivot = right - 1
        successor = 0

        # find rightmost successor
        for idx in range(len(nums) - 1, pivot, -1):
            if nums[idx] > nums[pivot]:
                successor = idx
                break

        # swap pivot and successor
        nums[pivot], nums[successor] = nums[successor], nums[pivot]

        # reverse suffix
        self.reverse(nums, pivot + 1, len(nums) - 1)

    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


obj = Solution()
obj.nextPermutation([3, 2, 1])

class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Solution:
            Odd places are always greater or equal than the previous one
            Even places are always smaller or equal than the previous one
        """

        # Premium

        for i in range(1, len(nums)):
            if ((i & 1) and nums[i] <= nums[i - 1]) or (
                (not i & 1) and nums[i] >= nums[i - 1]
            ):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

        print(nums)


print(Solution.wiggleSort(0, [3, 5, 2, 1, 6, 4]))

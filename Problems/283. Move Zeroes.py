def moveZeroes(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) < 2:
        return
    left, right = 0, 1
    while right < len(nums):
        if nums[left] == 0 and nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
        elif nums[left] != 0 and nums[right] == 0:
            left += 1
            right += 1
        elif nums[left] == 0 and nums[right] == 0:
            right += 1
        else:
            left += 1
            right += 1
    print(nums)


moveZeroes(0, [0])
moveZeroes(0, [1, 0, 2, 0, 4, 5, 0, 3, 12])
moveZeroes(0, [2, 1])

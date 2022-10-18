def rotate(self, nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    k = k % length
    # nums[:] = nums[length - k :] + nums[: length - k] # Or
    nums[:] = nums[-k:] + nums[:-k]
    print(nums)


print(rotate(0, [1, 2, 3, 4, 5, 6, 7], 3))
print(rotate(0, [-1, -100, 3, 99], 2))
print(rotate(0, [1, 2], 5))  # [2, 1]

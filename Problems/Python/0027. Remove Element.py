def removeElement(self, nums: list[int], val: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        # if the left element is the target, move the right pointer to the left
        if nums[left] == val:
            nums[left], nums[right] = nums[right], nums[left]
            # move the right pointer to the left
            right -= 1
        else:
            # move the left pointer to the right
            left += 1
    return left


print(removeElement(0, [0, 1, 2, 2, 3, 0, 4, 2], 2))

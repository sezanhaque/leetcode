def removeDuplicates(self, nums: list[int]) -> int:
    """
    Two Pointers method
    """
    if not nums:
        return 0
    left, right = 0, 1
    while right < len(nums):
        if nums[left] == nums[right]:
            right += 1
        else:
            left += 1
            nums[left] = nums[right]
    return left + 1


def removeDuplicates(self, nums: list[int]) -> int:
    """
    Using SET data type to get the unique elements and then sort them
    """
    return len(sorted(set(nums)))


def removeDuplicates(self, nums: list[int]) -> int:
    nums[:] = (val for idx, val in enumerate(nums) if idx == 0 or nums[idx - 1] != val)
    return len(nums)


print(removeDuplicates(0, [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates(0, [1, 1, 2]))

def findDuplicate(self, nums: list[int]) -> int:
    duplicate_number = set()
    for i in range(len(nums)):
        if nums[i] in duplicate_number:
            return nums[i]
        else:
            duplicate_number.add(nums[i])


print(findDuplicate(0, [1, 3, 4, 2, 2]))
print(findDuplicate(0, [3, 1, 3, 4, 2]))

def findMin(self, nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        # To filter duplicate values
        while left < right and nums[left] == nums[left + 1]:
            left += 1

        while left < right and nums[right] == nums[right - 1]:
            right -= 1
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


def findMin(self, nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + ((right - left) >> 1)

        # To filter duplicate values
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


# print(findMin(0, [1, 3, 5]))
# print(findMin(0, [2, 2, 2, 2, 0, 1, 1, 1]))
print(findMin(0, [3, 3, 1, 3]))

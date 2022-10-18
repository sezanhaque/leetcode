def findPeakElement(self, nums: list[int]) -> int:
    return nums.index(max(nums))


def findPeakElement(self, nums: list[int]) -> int:
    """
    Binary Search
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


print(findPeakElement(0, [1, 2, 1, 3, 5, 6, 4]))

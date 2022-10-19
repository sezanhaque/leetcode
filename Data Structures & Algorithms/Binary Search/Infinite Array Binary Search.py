def infiniteArray(self, nums: list[int], target: int) -> int:
    """
    Infinite array means you can not use length of the array
    """
    left, right = 0, 1

    while target > nums[right]:
        left, right = right + 1, (right + (right - left) * 2)

        return binarySearch(0, nums, target)


def binarySearch(self, nums: list[int], target: int) -> int:
    """
    Binary Search
    Search the index of the target value
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


print(
    infiniteArray(
        0, [1, 2, 3, 5, 7, 9, 10, 65, 78, 89, 90, 111, 121, 125, 142, 188], 89
    )
)

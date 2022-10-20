def binarySearch(self, nums: list[int], target: int) -> int:
    """
    Binary Search
    Search the index of greatest number <= target
    """
    left, right = 0, len(nums) - 1

    # what if the target is smaller than the smallest number in the array
    if nums[left] > target:
        return 0

    while left <= right:
        mid = (left + right) >> 1

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return right


print(binarySearch(0, [-1, 0, 3, 5, 9, 12], -2))
print(binarySearch(0, [-1, 0, 3, 5, 9, 12], 2))

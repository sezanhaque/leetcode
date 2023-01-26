from bisect import bisect_left


def binarySearch(self, nums: list[int], target: int) -> int:
    """
    Binary Search
    Search the index of the target value where it should be inserted
    """
    left, right = 0, len(nums) - 1

    # what if the target is greater than the greatest number in the array
    if nums[right] < target:
        return -1

    while left <= right:
        mid = (left + right) >> 1

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return left


def binarySearch(self, nums: list[int], target: int) -> int:
    """
    Using built in function
    """
    return bisect_left(nums, target)


print(binarySearch(0, [-1, 0, 3, 5, 9, 12], 6))
print(binarySearch(0, [-1, 0, 3, 5, 9, 12], 2))

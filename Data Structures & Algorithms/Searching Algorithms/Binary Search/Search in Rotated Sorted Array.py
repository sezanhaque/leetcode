"""
Leetcode problem 33
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""


def search(self, nums: list[int], target: int) -> int:
    pivot = findPivotIndex(0, nums)
    # pivot = nums.index(max(nums))     # using built-in function

    if pivot == -1:
        return binarySearch(0, nums, target, 0, len(nums) - 1)

    if nums[pivot] == target:
        return pivot

    if target >= nums[0]:
        # if target >= nums[0] then target will be between nums[0] to nums[pivot - 1]
        return binarySearch(0, nums, target, 0, pivot - 1)

    # else target will be between nums[pivot + 1] to len(nums) - 1
    return binarySearch(0, nums, target, pivot + 1, len(nums) - 1)


def search(self, nums: list[int], target: int) -> int:
    """
    Small short and fast
    """
    if not nums:
        return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) >> 1

        if nums[mid] == target:
            return mid

        # Left position
        if nums[left] <= nums[mid]:
            # if target is between start & mid, make right to (mid - 1)
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right position
        else:
            # if target is between mid & end, make start to (mid + 1)
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def findPivotIndex(self, nums: list[int]) -> int:
    start, end = 0, len(nums) - 1

    while start < end:
        mid = start + (end - start) >> 1

        if mid < end and nums[mid] > nums[mid + 1]:
            # if mid > mid + 1 then pivot found
            return mid

        if mid > start and nums[mid] < nums[mid - 1]:
            # if mid < mid - 1 then pivot found
            return mid - 1

        if nums[mid] < nums[start]:
            # if mid < start then pivot will be between start to mid - 1
            end = mid - 1
        else:
            # if mid > end then pivot will be between mid + 1 to end
            start = mid + 1
    return -1


def binarySearch(self, nums: list[int], target: int, start: int, end: int) -> int:
    while start <= end:
        mid = start + (end - start) >> 1

        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            return mid
    return -1


print(search(0, [4, 5, 6, 7, 0, 1, 2], 0))
print(search(0, [4, 5, 6, 7, 0, 1, 2], 3))
print(search(0, [1], 3))
print(search(0, [5, 1, 3], 5))

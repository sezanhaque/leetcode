from bisect import bisect_left


def searchInsert(self, nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            position = i
            break
        elif nums[i] > target:
            position = i
            break
        elif i == len(nums) - 1:
            position = i + 1
            break
    return position


def searchInsert(self, nums: list[int], target: int) -> int:
    """
    Fastest solution
    Binary Search
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        # mid = left + (right - left) // 2
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left

def searchInsert(self, nums: list[int], target: int) -> int:
    return bisect_left(nums, target)


print(searchInsert(0, [1, 3, 5, 6, 8], 8))  # 4
print(searchInsert(0, [1, 3, 5, 6], 2))  # 1
print(searchInsert(0, [1, 3, 5, 6], 7))  # 4
print(searchInsert(0, [1, 3, 5, 6], -2))  # 4

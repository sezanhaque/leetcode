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

def binarySearchWithRecursion(nums: list[int], left: int, right: int, target: int) -> int:
    """
    Binary Search using Recursion
    Search the index of the target value
    """
    mid = (left + right) >> 1
    if nums[mid] == target:
        return mid
    elif nums[mid] < target and mid != right:
        return binarySearchWithRecursion(nums, mid + 1, right, target)
    elif nums[mid] > target and mid != left:
        return binarySearchWithRecursion(nums, left, mid - 1, target)
    else:
        return -1

print(binarySearch(0, [-1, 0, 3, 5, 9, 12], 9))
print(binarySearch(0, [-1, 0, 3, 5, 9, 12], 2))

# Recursion
nums, target = [-1, 0, 3, 5, 9, 12], 5
left, right = 0, len(nums) - 1
print(binarySearchWithRecursion(nums, left, right, target))
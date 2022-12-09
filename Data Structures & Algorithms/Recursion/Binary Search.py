def binarySearch(nums: list[int], left: int, right: int, target: int) -> int:
    """
    Binary Search using Recursion
    Search the index of the target value
    """
    mid = (left + right) >> 1
    if nums[mid] == target:
        return mid
    elif nums[mid] < target and mid != right:
        return binarySearch(nums, mid + 1, right, target)
    elif nums[mid] > target and mid != left:
        return binarySearch(nums, left, mid - 1, target)
    else:
        return -1


if __name__ == "__main__":
    nums, target = [-1, 0, 3, 5, 9, 12], 5
    left, right = 0, len(nums) - 1
    print(binarySearch(nums, left, right, target))

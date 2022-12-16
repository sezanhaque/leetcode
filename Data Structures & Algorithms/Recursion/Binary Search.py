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


def rotatedBinarySearch(nums: list[int], left: int, right: int, target: int) -> int:
    """
    Rotated Binary Search using Recursion
    Search the index of the target value

    Ex: [4, 5, 6, 7, 1, 2, 3]
    """
    if left > right:
        return -1

    mid = (left + right) >> 1
    if nums[mid] == target:
        return mid

    # if left to mid part of the array is sorted
    if nums[left] <= nums[mid]:

        # if target is between left & mid, make left to (mid + 1)
        if nums[left] <= target <= nums[mid]:
            return rotatedBinarySearch(nums, left, mid - 1, target)

        # target will be between mid + 1 & right, make right to (mid + 1)
        else:
            return rotatedBinarySearch(nums, mid + 1, right, target)

    # if target is between mid & end, make start to (mid + 1)
    if nums[mid] <= target <= nums[right]:
        return rotatedBinarySearch(nums, mid + 1, right, target)

    # else if target is between left & mid, make start to (mid - 1)
    return rotatedBinarySearch(nums, left, mid - 1, target)


if __name__ == "__main__":
    nums, target = [-1, 0, 3, 5, 9, 12], 5
    left, right = 0, len(nums) - 1
    print(binarySearch(nums, left, right, target))

    nums, target = [4, 5, 6, 7, 1, 2, 3], 2
    left, right = 0, len(nums) - 1
    print(rotatedBinarySearch(nums, left, right, target))

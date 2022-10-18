def findMin(self, nums: list[int]) -> int:
    pivot = findPivotIndex(0, nums)

    if pivot == len(nums) - 1:
        return nums[0]
    else:
        return nums[pivot + 1]


def findPivotIndex(self, nums: list[int]) -> int:
    start, end = 0, len(nums) - 1

    while start < end:
        mid = start + ((end - start) >> 1)

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
    return start


def findMin(self, nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + ((right - left) >> 1)
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


print(findMin(0, [3, 4, 5, 1, 2]))
print(findMin(0, [4, 5, 6, 7, 0, 1, 2]))
print(findMin(0, [11, 13, 15, 17]))

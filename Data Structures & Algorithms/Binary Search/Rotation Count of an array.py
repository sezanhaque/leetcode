def rotationCount(self, nums: list[int]) -> int:
    # return findPivotIndex(0, nums) + 1
    return findPivotIndexWithDuplicates(0, nums) + 1


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


def findPivotIndexWithDuplicates(self, nums: list[int]) -> int:
    """
    Find Pivot index of an array where some values are duplicate
    """
    start, end = 0, len(nums) - 1

    while start < end:
        mid = start + (end - start) >> 1

        if mid < end and nums[mid] > nums[mid + 1]:
            # if mid > mid + 1 then pivot found
            return mid

        if mid > start and nums[mid] < nums[mid - 1]:
            # if mid < mid - 1 then pivot found
            return mid - 1

        if nums[mid] == nums[start] and nums[mid] == nums[end]:
            # If elements at start, mid & end are equal then just skip the duplicates

            if nums[start] > nums[start + 1]:
                # check if start is pivot
                return start
            start += 1

            if nums[end] < nums[end - 1]:
                # check if end is pivot
                return end - 1
            end -= 1

        elif nums[start] < nums[mid] or (
            nums[start] == nums[mid] and nums[mid] > nums[end]
        ):
            # It means left side is sorted, so pivot should be in the right
            start = mid + 1
        else:
            # It means right side is sorted, so pivot should be in the left
            end = mid - 1

        if nums[mid] < nums[start]:
            # if mid < start then pivot will be between start to mid - 1
            start = mid + 1
        else:
            # if mid > end then pivot will be between mid + 1 to end
            end = mid - 1
    return -1


print(rotationCount(0, [4, 5, 6, 6, 7, 0, 1, 1, 2]))

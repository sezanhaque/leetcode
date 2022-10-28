def search(self, nums: list[int], target: int) -> int:
    if not nums:
        return False

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + ((right - left) >> 1)

        if nums[mid] == target:
            return True

        # To filter duplicate values
        while left < mid and nums[left] == nums[mid]:
            left += 1

        # Left position
        if nums[left] <= nums[mid]:
            # if target is between start & mid, make right to (mid -1)
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

    return False


def search(self, nums: list[int], target: int) -> int:
    if not nums:
        return False

    left, right = 0, len(nums) - 1

    while left <= right:

        # To filter duplicate values
        while left < right and nums[left] == nums[left + 1]:
            left += 1

        while left < right and nums[right] == nums[right - 1]:
            right -= 1

        mid = left + ((right - left) >> 1)

        if nums[mid] == target:
            return True

        # Left position
        if nums[left] <= nums[mid]:
            # if target is between start & mid, make right to (mid -1)
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

    return False


def search(self, nums: list[int], target: int) -> int:
    """
    Faster
    """
    if not nums:
        return False

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + ((right - left) >> 1)

        if nums[mid] == target:
            return True

        # Left position
        if nums[left] <= nums[mid]:
            # if target is between start & mid, make right to (mid -1)
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            elif nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            else:
                left = mid + 1

        # Right position
        else:
            # if target is between mid & end, make start to (mid + 1)
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            elif nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            else:
                right = mid - 1

    return False


def searchWithPivot(self, nums: list[int], target: int) -> int:
    pivot = findPivotIndex(0, nums)
    print(nums[pivot])

    if nums[0] <= target <= nums[pivot]:
        return binarySearch(0, nums, target, 0, pivot - 1)
    else:
        return binarySearch(0, nums, target, pivot, len(nums) - 1)


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


def binarySearch(self, nums: list[int], target: int, start: int, end: int) -> int:
    while start <= end:
        mid = start + ((end - start) >> 1)

        if nums[mid] == target:
            return True

        # start position
        if nums[start] <= nums[mid]:
            # if target is between start & mid, make end to (mid -1)
            if nums[start] <= target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # end position
        else:
            # if target is between mid & end, make start to (mid + 1)
            if nums[mid] <= target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return False


# print(search(0, [2, 5, 6, 0, 3, 1, 4], 0))
# print(search(0, [1, 1, 1, 0, 1], 0))
print(searchWithPivot(0, [2, 5, 6, 0, 3, 1, 4], 0))
print(searchWithPivot(0, [1, 1, 1, 0, 1], 0))

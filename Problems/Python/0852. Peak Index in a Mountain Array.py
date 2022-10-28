def peakIndexInMountainArray(self, arr: list[int]) -> int:
    return arr.index(max(arr))


def peakIndexInMountainArray(self, arr: list[int]) -> int:
    """
    Binary Search
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) >> 1
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1


print(peakIndexInMountainArray(0, [0, 10, 5, 2]))

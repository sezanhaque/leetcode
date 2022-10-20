def binarySearch(self, arr: list[int], target: int) -> int:
    start, end = 0, len(arr) - 1

    # Find whether the array is sorted in ascending or descending
    isAscOrder = arr[start] < arr[end]

    while start <= end:
        mid = start + ((end - start) >> 1)

        if arr[mid] == target:
            return mid

        if isAscOrder:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


print(binarySearch(0, [99, 80, 75, 22, 11, 10, 5, 2, -3], 80))

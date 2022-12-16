def selectionSort(arr: list[int], size: int):

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if arr[i] < arr[min_idx]:
                min_idx = i

        # put min at the correct position
        arr[step], arr[min_idx] = arr[min_idx], arr[step]


def selectionSortRecursion(
    arr: list[int], curr: int, end: int, maxIdx: int = 0
) -> None:
    if end == 0:
        return

    if curr < end:
        # if curr value is greater than max value
        if arr[curr] > arr[maxIdx]:
            # then change curr idx + 1
            # and make max = curr idx
            selectionSortRecursion(arr, curr + 1, end, curr)
        else:
            # else make curr idx + 1
            selectionSortRecursion(arr, curr + 1, end, maxIdx)
    else:
        # if curr idx == end idx
        # swap max idx with last idx
        # then call the function again with new end idx - 1
        arr[maxIdx], arr[end - 1] = arr[end - 1], arr[maxIdx]
        selectionSortRecursion(arr, 0, end - 1, 0)


data = [-2, 45, 0, 11, -9]
# selectionSort(data, len(data))
selectionSortRecursion(data, 0, len(data))
print(data)

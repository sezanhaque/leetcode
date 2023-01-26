def bubbleSort(arr: list[int]):
    # loop to access each arr element
    for i in range(len(arr)):
        # loop to compare arr elements
        for j in range(0, len(arr) - i - 1):
            # compare two adjacent elements
            # change > to < to sort in descending order
            if arr[j] > arr[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubbleSortRecursion(arr: list[int], curr: int, end: int) -> None:
    """
    Bubble sort using recursion
    """
    if end == 0:
        return

    if curr < end:
        if arr[curr] > arr[curr + 1]:
            arr[curr], arr[curr + 1] = arr[curr + 1], arr[curr]

        bubbleSortRecursion(arr, curr + 1, end)

    # curr == end, it means we have sorted 1 number to last idx
    else:
        # so we are sorting from 0 to end - 1
        bubbleSortRecursion(arr, 0, end - 1)


data = [-2, 45, 0, 11, -9]
# bubbleSort(data)
bubbleSortRecursion(data, 0, len(data) - 1)
print(data)

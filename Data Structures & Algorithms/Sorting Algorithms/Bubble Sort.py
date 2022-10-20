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


data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print(data)

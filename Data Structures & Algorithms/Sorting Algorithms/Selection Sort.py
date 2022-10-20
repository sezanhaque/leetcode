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


data = [-2, 45, 0, 11, -9]
selectionSort(data, len(data))
print(data)

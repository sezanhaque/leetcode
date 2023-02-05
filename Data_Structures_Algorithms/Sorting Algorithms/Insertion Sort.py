def insertionSort(arr: list[int]) -> list[int]:
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<arr[j] to key>arr[j].
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        arr[j + 1] = key


def insertionSort(arr: list[int]) -> list[int]:
    for i in range(len(arr) - 1):
        for j in range(i + 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


data = [9, 5, 1, 4, 3]
insertionSort(data)
print(data)

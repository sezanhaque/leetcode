def mergeSort(array: list[int]):
    if len(array) > 1:

        #  r is the point where the array is divided into two sub-arrays
        r = len(array) >> 1
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


def mergeSortRecursion(arr: list[int], start: int, end: int) -> None:
    if end - start == 1:
        return

    mid = (start + end) >> 1

    mergeSortRecursion(arr, start, mid)
    mergeSortRecursion(arr, mid, end)

    merge(arr, start, mid, end)


def merge(arr: list[int], start: int, mid: int, end: int) -> list[int]:
    res = [None] * (end - start)
    leftIdx, rightIdx, idx = start, mid, 0

    # While left idx < mid and right idx < end
    # check which value is smaller
    #  store smaller value to the res array
    while leftIdx < mid and rightIdx < end:
        if arr[leftIdx] < arr[rightIdx]:
            res[idx] = arr[leftIdx]
            leftIdx += 1
        else:
            res[idx] = arr[rightIdx]
            rightIdx += 1
        idx += 1

    # if left side array has any leftover
    while leftIdx < mid:
        res[idx] = arr[leftIdx]
        leftIdx += 1
        idx += 1

    # if right side array has any leftover
    while rightIdx < end:
        res[idx] = arr[rightIdx]
        rightIdx += 1
        idx += 1

    # merge res array with main array
    l = 0
    for l in range(len(res)):
        arr[start + l] = res[l]


if __name__ == "__main__":
    data = [6, 5, 12, 10, 9, 1]

    # mergeSort(data)
    mergeSortRecursion(data, 0, len(data))
    print(data)

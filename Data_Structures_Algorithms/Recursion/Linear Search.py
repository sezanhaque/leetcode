def findIndex(arr: list[int], target: int, idx: int = 0) -> int:
    """
    Find the index of the targeted value by linear search.
    """
    if idx == len(arr):
        return -1

    if arr[idx] == target:
        return idx

    return findIndex(arr, target, idx + 1)


# print(findIndex([1, 2, 3, 54, 42, 7], 42))


def findAllIndex(arr: list[int], target: int, res: list[int], idx: int = 0) -> int:
    """
    Find all index of the targeted value by linear search.
    """
    if idx == len(arr):
        return res

    if arr[idx] == target:
        res.append(idx)

    return findAllIndex(arr, target, res, idx + 1)


print(findAllIndex([1, 2, 3, 54, 42, 7, 42, 5, 42], 42, []))

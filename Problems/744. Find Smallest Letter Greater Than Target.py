from bisect import bisect_right


def nextGreatestLetter(self, letters: list[str], target: str) -> str:
    """
    Binary Search
    """
    start, end = 0, len(letters) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if target < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return letters[start % len(letters)]


def nextGreatestLetter(self, letters: list[str], target: str) -> str:
    """
    Binary Search
    """
    if target >= letters[-1] or target < letters[0]:
        return letters[0]

    start, end = 0, len(letters) - 1

    while start <= end:
        mid = (start + end) // 2

        if target < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return letters[start]

def nextGreatestLetter(self, letters: list[str], target: str) -> str:
    return letters[bisect_right(letters, target) % len(letters)]

print(nextGreatestLetter(0, ["c", "f", "j"], "a"))
print(nextGreatestLetter(0, ["c", "f", "j"], "c"))
print(nextGreatestLetter(0, ["c", "f", "j"], "d"))

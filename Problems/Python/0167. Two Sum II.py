def twoSum(self, numbers, target):
    """
    Solution 1: HashMap

    We need to find 2 numbers REMAINING, VALUE so that REMAINING + VALUE = TARGET.
    We need a HashMap data structure to store elements in the past, let name it seen.
    The idea is that we iterate b as each element in numbers, we check if we found a (where REMAINING = TARGET - VALUE) in the past.
    If a exists in seen then we already found 2 numbers REMAINING and VALUE, so that REMAINING + VALUE = TARGET, just output their indices.
    Else add b to the seen.
    """
    seen = {}
    for i, value in enumerate(numbers):
        remaining = target - numbers[i]

        if remaining in seen:
            return [seen[remaining] + 1, i + 1]

        seen[value] = i


def twoSum(self, numbers, target) -> list[int]:
    """
    Binary Search approach
    """
    investigatedSoFar = []
    for i in range(len(numbers)):
        if not numbers[i] in investigatedSoFar:

            investigatedSoFar.append(numbers[i])
            left, right = i + 1, len(numbers) - 1
            remaining = target - numbers[i]

            while left <= right:
                mid = left + ((right - left) >> 1)
                if numbers[mid] == remaining:
                    return [i + 1, mid + 1]
                elif numbers[mid] < remaining:
                    left = mid + 1
                else:
                    right = mid - 1


def twoSum(self, numbers, target) -> list[int]:
    """
    Two Pointers approach
    """
    left, right = 0, len(numbers) - 1

    while numbers[left] + numbers[right] != target:
        if numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1
    return [left + 1, right + 1]


# print(twoSum(0, [2, 7, 11, 15], 9))
print(twoSum(0, [2, 11, 15, 4, 7, 1, 8], 9))

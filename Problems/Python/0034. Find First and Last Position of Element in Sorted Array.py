def searchRange(self, nums: list[int], target: int) -> list[int]:
    start, end = -1, -1
    if len(nums) == 1:
        if nums[0] == target:
            return [0, 0]
        else:
            return [-1, -1]
    for i in range(len(nums)):
        if nums[i] == target and start > -1:
            end = i
        if nums[i] == target and start < 0:
            start = i
        if i == len(nums) - 1 and start > -1 and end < 0:
            end = start
    return [start, end]


def searchRange(self, nums: list[int], target: int) -> list[int]:
    found = []
    for i in range(len(nums)):
        if nums[i] == target:
            found.append(i)
    return [found[0], found[-1]] if found else [-1, -1]


def searchRange(self, nums: list[int], target: int) -> list[int]:
    result = [-1, -1]

    result[0] = binarySearch(0, nums, target, True)
    if result[0] != -1:
        result[1] = binarySearch(0, nums, target, False)
        
    return result


def binarySearch(self, nums: list[int], target: int, findStartIndex: bool) -> int:
    result = -1
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            result = mid
            if findStartIndex:
                end = mid - 1
            else:
                start = mid + 1

    return result


print(searchRange(0, [5, 7, 7, 8, 8, 10], 8))
print(searchRange(0, [5, 7, 7, 8, 8, 10], 6))
print(searchRange(0, [], 0))
print(searchRange(0, [1], 1))
print(searchRange(0, [1, 3], 1))
print(searchRange(0, [3, 3, 3], 3))

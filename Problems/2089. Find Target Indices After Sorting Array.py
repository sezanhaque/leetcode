from bisect import bisect_left, bisect_right


def targetIndices(self, nums: list[int], target: int) -> list[int]:
    nums = sorted(nums)
    result = [-1, -1]
    result[0] = binarySearch(0, nums, target, True)
    if result[0] != -1:
        result[1] = binarySearch(0, nums, target, False)

    if result[0] != -1:
        return [i for i in range(result[0], result[-1] + 1)]
    else:
        return []


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


def targetIndices(self, nums: list[int], target: int) -> list[int]:
    nums = sorted(nums)
    left = bisect_left(nums, target)
    right = bisect_right(nums, target) - 1
    result = [left, right]

    return [] if len(result) == 0 else [i for i in range(result[0], result[-1] + 1)]


def targetIndices(self, nums: list[int], target: int) -> list[int]:
    return [i for i, num in enumerate(sorted(nums)) if num == target]


print(targetIndices(0, [1, 2, 5, 2, 3], 2))
print(targetIndices(0, [1, 2, 5, 2, 3], 6))
print(
    targetIndices(
        0,
        [
            75,
            99,
            19,
            93,
            87,
            68,
            12,
            18,
            48,
            83,
            24,
            50,
            16,
            53,
            36,
            16,
            80,
            68,
            46,
            13,
            53,
            100,
            50,
            49,
            77,
            52,
            34,
            42,
            38,
            98,
            73,
            11,
            13,
            61,
            72,
            8,
            11,
            67,
            98,
            24,
            23,
            71,
            47,
            6,
            5,
            7,
            97,
            86,
            25,
            82,
            11,
            15,
            26,
            97,
            69,
            6,
            30,
            77,
            98,
            44,
            32,
            39,
            71,
            47,
            64,
            78,
            6,
            61,
            72,
            75,
        ],
        98,
    )
)

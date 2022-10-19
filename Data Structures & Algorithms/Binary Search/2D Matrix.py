def binarySearch(self, nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums[0]) - 1

    while left < len(nums) - 1 and right > -1:
        if nums[left][right] == target:
            return [left, right]
        if nums[left][right] < target:
            left += 1
        else:
            right -= 1

    return [left, right]


data = [[10, 20, 30, 40], [15, 25, 35, 45], [28, 29, 37, 49], [33, 34, 38, 50]]
print(
    binarySearch(
        0,
        data,
        10,
    )
)

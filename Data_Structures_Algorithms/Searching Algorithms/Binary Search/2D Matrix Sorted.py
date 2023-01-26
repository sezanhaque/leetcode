"""
Search a 2D Matrix II (Sorted)
LeetCode Problem 240
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""


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


data = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
print(
    binarySearch(
        0,
        data,
        5,
    )
)

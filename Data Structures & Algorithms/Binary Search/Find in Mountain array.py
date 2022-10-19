"""
Leetcode problem 1095
https://leetcode.com/problems/find-in-mountain-array/
"""


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: list[int]) -> int:
        mountainPoint = Solution.findMountainPoint(0, mountain_arr)
        firstPart = Solution.binarySearch(
            0, mountain_arr, target, 0, mountainPoint, True
        )

        if firstPart != -1:
            return firstPart

        return Solution.binarySearch(
            0, mountain_arr, target, mountainPoint, len(mountain_arr) - 1, False
        )

    def binarySearch(
        self, arr: list[int], target: int, start: int, end: int, isAscOrder: bool
    ) -> int:

        while start <= end:
            mid = start + ((end - start) >> 1)

            if arr[mid] == target:
                return mid

            if isAscOrder:
                if target < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target < arr[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

    def findMountainPoint(self, arr: list[int]) -> int:
        start, end = 0, len(arr) - 1

        while start < end:
            """
            If we know that the index is exist then we use start < end.
            otherwise start <= end.
            """
            mid = start + ((end - start) >> 1)

            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return start


print(Solution.findInMountainArray(0, 3, [1, 2, 3, 4, 5, 3, 1]))
print(Solution.findInMountainArray(0, 3, [0, 1, 2, 4, 2, 1]))

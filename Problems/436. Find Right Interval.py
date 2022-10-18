from bisect import bisect, bisect_left


class Solution:
    def binarySearch(arr: list[int], target: int):
        """
        Binary Search
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if arr[mid][1][0] < target:
                # check if start is less than target
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        length = len(intervals)

        if not intervals:
            return []
        elif length == 1:
            return [-1]

        result = [-1] * length
        check_list = list(
            sorted(
                [[idx, val] for idx, val in enumerate(intervals)], key=lambda x: x[1][0]
            )
        )

        for idx, interval in enumerate(intervals):
            position = Solution.binarySearch(check_list, interval[1])
            # ignore if no "right" interval found
            if position == length:
                continue
            else:
                result[idx] = check_list[position][0]

        return result

    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        starts = sorted([val[0], idx] for idx, val in enumerate(intervals)) + [
            [float("inf"), -1]
        ]
        return [starts[bisect(starts, [idx[1]])][1] for idx in intervals]


print(Solution.findRightInterval(0, [[3, 4], [2, 3], [1, 2]]))

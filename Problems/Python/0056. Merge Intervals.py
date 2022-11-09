class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Time complexity : O(nlogn)
        Space complexity : O(nlogn) / O(n)
        """
        res = []

        for interval in sorted(intervals, key=lambda x: x[0]):
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                res[-1][1] = max(res[-1][1], interval[1])

        return res

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Time complexity : O(nlogn)
        Space complexity : O(1)
        """

        intervals.sort(key=lambda x: x[0])
        idx = 0

        while idx < len(intervals) - 1:
            if intervals[idx][1] >= intervals[idx + 1][0]:
                intervals[idx][1] = max(intervals[idx][1], intervals[idx + 1][1])
                del intervals[idx + 1]
            else:
                idx += 1

        return intervals


print(Solution.merge(0, [[1, 3], [2, 6], [8, 10], [15, 18]]))
print(
    Solution.merge(
        0, [[1, 9], [2, 5], [19, 20], [10, 11], [12, 20], [0, 3], [0, 1], [0, 2]]
    )
)

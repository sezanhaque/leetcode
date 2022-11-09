class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        res = []

        for idx in range(len(intervals)):

            # if new interval is before all the intervals from current idx
            # then return it with intervals
            if newInterval[1] < intervals[idx][0]:
                res.append(newInterval)
                return res + intervals[idx:]

            # else if new interval is after the current interval
            # then append the current interval to result
            elif newInterval[0] > intervals[idx][1]:
                res.append(intervals[idx])

            else:
                newInterval = [
                    # get the min value between start position
                    # of newInterval and current interval
                    min(newInterval[0], intervals[idx][0]),
                    # get the max value between end position
                    # of newInterval and current interval
                    max(newInterval[1], intervals[idx][1]),
                ]

        # append the final newInterval after the loop
        res.append(newInterval)

        return res


print(
    Solution.insert(
        0, intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
    )
)

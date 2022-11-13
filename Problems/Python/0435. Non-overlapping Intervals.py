class Solution:
    """
    @param intervals: a collection of intervals
    @return: the minimum number of intervals you need to remove
    """

    # Premium

    def erase_overlap_intervals(self, intervals: list[int]) -> int:
        intervals.sort()
        ans, prevEnd = 0, intervals[0][1]

        for start, end in intervals[1:]:
            # check if start of current interval is greater
            # or equal than prevEnd
            # if so, then assign it to prevEnd
            if start >= prevEnd:
                prevEnd = end
            else:
                # else increment ans
                # and assign the min end to prevEnd
                ans += 1
                prevEnd = min(end, prevEnd)

        return ans


print(Solution.erase_overlap_intervals(0, [[1, 3], [2, 3], [3, 4], [1, 2]]))
print(Solution.erase_overlap_intervals(0, [[1, 2], [1, 2], [1, 2]]))
print(Solution.erase_overlap_intervals(0, [[1, 2], [2, 3]]))

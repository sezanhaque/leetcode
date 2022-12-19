from typing import List


class Solution:
    """
    Solution:

        1.  First sort the interval following end time.
            And answer = Length of list.

        2.  We track maxEnd time.

        3.  If current end time is equal or less than
            maxEnd time then we subtract 1 from answer.

        4.  Else we assign current end time to maxEnd time.

        5.  Return answer.

    Complexity:
        Time: O(nlogn)
        Space: O(1)
    """

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = len(intervals)
        maxEnd = 0

        for _, end in sorted(intervals, key=lambda x: (x[0], -x[1])):
            if end <= maxEnd:
                ans -= 1
            else:
                maxEnd = end

        return ans


print(Solution.removeCoveredIntervals(0, [[1, 4], [3, 6], [2, 8]]))  # 2
print(Solution.removeCoveredIntervals(0, [[3, 10], [4, 10], [5, 11]]))  # 2
print(Solution.removeCoveredIntervals(0, [[1, 2], [1, 4], [3, 4]]))  # 1

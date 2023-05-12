from functools import cache
from typing import List


class Solution:
    """
    This is a typical dynamic programming problem.
    For each index idx we have 2 options:

    Take points idx and jump the next brainpower idx indexes
    Skip the current index(do not collect points idx) and move to the next index
    We need to find the maximum points we can collect given the above-mentioned constraints

    Note: dp[idx] denotes the max points that can be collected for the subarray: questions[idx... questions.size() - 1].
    So we only need to compute it once for each idx
    """

    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def DP(idx: int) -> int:
            if idx >= len(questions):
                return 0

            points, jump = questions[idx][0], questions[idx][1]
            return max(DP(idx + 1), points + DP(idx + jump + 1))

        return DP(0)


obj = Solution()
print(obj.mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]))

from collections import defaultdict
from typing import List


class Solution:
    """
    The judge will be the difference between in-degree and out-degree

    In-degree: The number of people trust this guy
    Out-degree: The guy trusts how many people

    Answer will be in-degree - out-degree == n - 1
    """

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        diff = defaultdict(int)

        for a, b in trust:
            # out-degree
            diff[a] -= 1
            # in-degree
            diff[b] += 1

        for idx in range(1, n + 1):
            if diff[idx] == n - 1:
                return idx

        return -1


obj = Solution()
print(obj.findJudge(n=3, trust=[[1, 3], [2, 3]]))

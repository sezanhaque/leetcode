from collections import defaultdict
from math import atan2
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Brute Force Solution
        """
        length = len(points)

        if length == 1:
            return 1

        res = 2

        # point 1: x1, y1
        for i in range(length):

            # point 2: x2, y2
            for j in range(i + 1, length):
                count = 2

                # x2 - x1
                dx = points[j][0] - points[i][0]

                # y2 - y1
                dy = points[j][1] - points[i][1]

                # point 3: x3, y3
                for k in range(length):
                    if k != i and k != j:
                        # x3 - x1
                        dx_ = points[k][0] - points[i][0]

                        # y3 - y1
                        dy_ = points[k][1] - points[i][1]

                        # dy/dx == dy_/dx_
                        # => dy * dx_ = dx * dy_
                        if dy * dx_ == dx * dy_:
                            count += 1

                res = max(res, count)

        return res

    def maxPoints(self, points: List[List[int]]) -> int:
        length = len(points)

        if length == 1:
            return 1

        res = 2

        for i in range(length):
            count = defaultdict(int)

            for j in range(length):
                if j != i:
                    count[atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])] += 1

            res = max(res, max(count.values()) + 1)

        return res


obj = Solution()
print(obj.maxPoints([[1, 1], [2, 2], [3, 3]]))
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res = len(points)
        end = points[0][1]

        for idx in range(1, len(points)):
            # if current end is between start and end
            # of another balloon then 1 arrow will
            # shoot both of them
            if points[idx][0] <= end <= points[idx][1]:
                res -= 1
            else:
                end = points[idx][1]

        return res

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        *   Sort the points based on the end of each point.
        *   Initialize the curEnd as the end value of the first point. (Shorting the first balloon)
        *   For each point:
                if its start point is larger than the curEnd, add one more arrow,
                and update the curEnd to the new endpoint.
        """
        points.sort(key=lambda x: x[1])
        res, currEnd = 1, points[0][1]

        for start, end in points:
            if start > currEnd:
                currEnd = end
                res += 1

        return res


obj = Solution()
print(obj.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))  # 2
print(obj.findMinArrowShots([[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]))  # 2
print(obj.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))  # 4
print(obj.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))  # 2

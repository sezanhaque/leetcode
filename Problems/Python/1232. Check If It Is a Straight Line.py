from typing import List


class Solution:
    """
    Find slope for first two points, point1 and point2

    Then compare the slopes of all other points to this slope

    Slope of point1 (x1, y1) and point2 (x2, y2) is:
    (y2 - y1) / (x2 - x1)

    Slope of point1 (x1, y1) and point3 (x3, y3) is:
    (y3 - y1) / (x3 - x1)

    For all three points to be on the same line, the slopes should be equal, in other words:
    (y2 - y1) / (x2 - x1) = (y3 - y1) / (x3 - x1)

    To avoid the 'divide by zero' error, use cross multiplication to find slope:
    (y2 - y1) * (x3 - x1) = (y3 - y1) * (x2 - x1)
    """

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]

        for x3, y3 in coordinates[2:]:
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                return False

        return True


obj = Solution()
print(obj.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))

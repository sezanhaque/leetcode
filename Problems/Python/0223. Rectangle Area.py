"""
    Algorithm:
        (1) calculate the total area covered by the two rectangles
        (2) calculate the area of the overlap between the two rectangles
        (3) subtract the overlap from the total area

    The tricky part is how to calculate the overlapped area.
    We get the overlap on x-axis, and y-axis separately.
    Using examples on x-axis for illustration:

    case1:
    ax1-----------ax2
        bx1-----------bx2

    case2:
    ax1-----------ax2
        bx1-bx2

    case3:
    ax1-----------ax2
                        bx1-----------bx2

    If you draw all the cases down for a and b, there can be 10 cases. 
    However, after we swap a and b, there are only 3 cases as shown above, and all we need to do is to
        (1) find the minimum of the two endpoints
        (2) find the maximum of the two start points
        (3) overlap = (1) - (2) Note that if the result is negative, it means there is no overlap, 
            then overlap=0, so we do overlap = max( (1)-(2), 0)
"""


class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        area_of_a = Solution.area(0, ax1, ay1, ax2, ay2)
        area_of_b = Solution.area(0, bx1, by1, bx2, by2)
        overlap_x = max(min(ax2, bx2) - max(ax1, bx1), 0)
        overlap_y = max(min(ay2, by2) - max(ay1, by1), 0)
        return (
            area_of_a + area_of_b
        ) - (overlap_x * overlap_y)

    def area(self, x1: int, y1: int, x2: int, y2: int) -> int:
        """
        Calculate the area of a rectangle
        """
        return (x2 - x1) * (y2 - y1)


print(Solution.computeArea(0, ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2))

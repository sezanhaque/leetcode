from typing import List


class Solution:
    """
    Area of a rectangle is L x W.
    So if we could check only from square root of area then
    we will get the min diff between L, W.

    The first value from square root to 1 that will divide
    the area and the reminder will be 0, it will be W
    and the dividend result will be L.

    L x W = Area
    So, W = Area // L
    """
    def constructRectangle(self, area: int) -> List[int]:
        for idx in range(int(area ** 0.5), 0, -1):
            if not area % idx:
                return [area // idx, idx]


obj = Solution()
print(obj.constructRectangle(4))

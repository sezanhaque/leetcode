class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        def helper(start1, end1, start2, end2):
            startMax = max(start1, start2)
            endMin = min(end1, end2)
            return startMax < endMin

        rec1_x1, rec1_y1, rec1_x2, rec2_y2 = rec1
        rec2_x1, rec2_y1, rec2_x2, rex2_y2 = rec2

        return helper(rec1_x1, rec1_x2, rec2_x1, rec2_x2) and helper(rec1_y1, rec2_y2, rec2_y1, rex2_y2)


print(Solution.isRectangleOverlap(0, rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3]))  # true
print(Solution.isRectangleOverlap(0, rec1=[0, 0, 1, 1], rec2=[1, 0, 2, 1]))  # false
print(Solution.isRectangleOverlap(0, rec1=[5, 15, 8, 18], rec2=[0, 3, 7, 9]))  # false

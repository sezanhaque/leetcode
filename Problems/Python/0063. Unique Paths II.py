from functools import cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def DFS(row: int, col: int) -> int:
            right = bottom = 0
            # if we are on the bottom of the box
            # and there is no obstacles
            # so return 1
            if (
                    row == len(obstacleGrid) - 1
                    and col == len(obstacleGrid[0]) - 1
                    and not obstacleGrid[row][col]
            ):
                return 1

            # if we face any obstacle
            if obstacleGrid[row][col]:
                return 0

            # we are going right
            if col < len(obstacleGrid[0]) - 1:
                right = DFS(row, col + 1)

            # we are going bottom
            if row < len(obstacleGrid) - 1:
                bottom = DFS(row + 1, col)

            return right + bottom

        return DFS(0, 0)


obj = Solution()
print(obj.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(obj.uniquePathsWithObstacles([[0, 0], [0, 1]]))

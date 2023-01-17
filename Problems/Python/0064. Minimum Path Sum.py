from functools import cache
from math import inf
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def DFS(row: int, col: int) -> int:
            # we are out of the box
            if row > len(grid) - 1 or col > len(grid[0]) - 1:
                return inf

            # we are on the last block of the grid
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]

            # return current block value + min of right / bottom
            return grid[row][col] + min(DFS(row + 1, col), DFS(row, col + 1))

        return DFS(0, 0)

    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def DFS(row: int, col: int):
            # we are out of bound
            if row > (rowMax := len(grid) - 1) or col > (colMax := len(grid[0]) - 1):
                return inf

            # if we are on the bottom of the box
            if (row, col) == (rowMax, colMax):
                return grid[row][col]

            # return current block value + min of right / bottom
            return grid[row][col] + min(DFS(row + 1, col), DFS(row, col + 1))

        return DFS(0, 0)


obj = Solution()
print(obj.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

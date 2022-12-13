from functools import cache
from math import inf


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        length = len(matrix)

        @cache
        def dfs(row, col):
            # the bottom is reached
            if row == length:
                return 0

            # a boundary is reached
            if col < 0 or col == length:
                return inf

            # recursive condition
            return matrix[row][col] + min(
                dfs(row + 1, col - 1), dfs(row + 1, col), dfs(row + 1, col + 1)
            )

        # try all starting elements
        return min(dfs(0, col) for col in range(length))


print(Solution.minFallingPathSum(0, [[2, 1, 3], [6, 5, 4], [7, 8, 9]]))

from itertools import product
from typing import List


class Solution:
    def __init__(self):
        self.res = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        empty = 1

        # loop through row x col to get total empty cells
        # and starting cell
        for i, j in product(range(row), range(col)):
            if grid[i][j] == 1:
                (start, end) = (i, j)
            elif grid[i][j] == 0:
                empty += 1

        # we can get empty cells and starting by
        # this way also
        # for i in range(row):
        #     for j in range(col):
        #         if grid[i][j] == 1:
        #             (start, end) = (i, j)
        #         elif grid[i][j] == 0:
        #             empty += 1

        def DFS(x: int, y: int, rest: int) -> None:
            # if x is not in between 0 - row
            # y is not in between 0 - col
            # current value grid[x][y] is not
            # greater than or equal to 0 means -1
            # then return
            if not (0 <= x < row and 0 <= y < col and grid[x][y] >= 0):
                return

            # If current value is 2
            # then check if rest empty cell is 0
            # if so then add 1 to result
            if grid[x][y] == 2:
                self.res += rest == 0
                return

            # make current value to -2
            # so that we can determine that
            # we have traversed this cell
            grid[x][y] = -2

            # go to
            # up (x + 1, y)
            DFS(x + 1, y, rest - 1)

            # down (x - 1, y)
            DFS(x - 1, y, rest - 1)

            # right (x, y + 1)
            DFS(x, y + 1, rest - 1)

            # left (x, y - 1)
            DFS(x, y - 1, rest - 1)

            # after traversing from current cell
            # make the current cell to 0
            grid[x][y] = 0

        DFS(start, end, empty)

        return self.res


obj = Solution()
print(obj.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))  # 2

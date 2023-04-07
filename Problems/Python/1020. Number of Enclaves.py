from itertools import product
from typing import List


class Solution:
    """
    We check edges of the matrix
    if we find any "1" then do DFS and clean all its connected 1 into 0
    return the sum of left 1's
    """
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def DFS(row: int, col: int) -> None:
            # if the row, col is in the boundary and the block is 1
            if 0 <= row < rows and 0 <= col < cols and grid[row][col]:
                # mark the block as visited
                grid[row][col] = 0

                # visit up, down, right, left
                # list(map(DFS, (row + 1, row - 1, row, row), (col, col, col + 1, col - 1)))
                for r, c in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                    DFS(r, c)

        for row, col in product(range(rows), range(cols)):
            # if the row, col is in the boundary and the block is 1
            if row in (0, rows - 1) or col in (0, cols - 1) and grid[row][col]:
                DFS(row, col)

        return sum(sum(row) for row in grid)
        # return sum(map(sum, grid))


obj = Solution()
print(obj.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
print(obj.numEnclaves([[0, 0, 0, 1, 1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
                       [0, 1, 1, 0, 0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
                       [0, 1, 1, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]]))  # 3

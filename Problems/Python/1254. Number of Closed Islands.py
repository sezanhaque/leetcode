from itertools import product
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def DFS(row: int, col: int) -> bool:
            # check the boundary
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            # if current block is 1
            if grid[row][col]:
                return True

            # mark as visited
            grid[row][col] = 1

            # traverse in all direction
            left = DFS(row, col - 1)
            right = DFS(row, col + 1)
            up = DFS(row - 1, col)
            down = DFS(row + 1, col)

            # return True if all direction have True value
            return left and right and up and down

        for row, col in product(range(rows), range(cols)):
            if not grid[row][col] and DFS(row, col):
                res += 1

        return res

        # or we can write in one line also
        # return sum(1 for row, col in product(range(rows), range(cols)) if not grid[row][col] and DFS(row, col))

    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def BFS(row: int, col: int) -> int:
            visited.add((row, col))
            queue = [(row, col)]
            res = 1

            for row, col in queue:
                for r, c in (row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col):
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        res = 0
                    elif not grid[r][c] and (r, c) not in visited:
                        visited.add((r, c))
                        queue.append((r, c))

            return res

        return sum(BFS(row, col) for row, col in product(range(rows), range(cols)) if
                   not grid[row][col] and (row, col) not in visited)


obj = Solution()
print(obj.closedIsland(
    [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 0]]))

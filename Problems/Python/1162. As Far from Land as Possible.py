from collections import deque
from typing import List


class Solution:
    # BFS
    def maxDistance(self, grid: List[List[int]]) -> int:
        length = len(grid)
        queue = deque()
        res = -1

        # add land coordinates (1) to queue
        queue += ([row, col] for row in range(length) for col in range(length) if grid[row][col])

        # top: 0, 1             bottom: 0, -1
        # right: 1, 0           left: -1, 0
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            row, col = queue.popleft()

            res = grid[row][col]

            # move from current position to 4 direction
            # left, right, top, bottom
            for direct_row, direct_col in direct:
                new_row, new_col = row + direct_row, col + direct_col

                # Check boundary
                # if current block is between 0 and length of grid
                # and current block value is 0, it means it is not
                # visited, so we can add it to queue and update its
                # value to its parent grid + 1
                if (min(new_row, new_col) >= 0
                        and max(new_row, new_col) < length
                        and not grid[new_row][new_col]):
                    queue.append([new_row, new_col])
                    grid[new_row][new_col] = grid[row][col] + 1

        return res - 1 if res > 1 else - 1


obj = Solution()
print(obj.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))

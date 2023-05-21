from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        found = False
        stack = []
        n, m = len(grid), len(grid[0])
        # -----------
        # find the first island
        # -----------
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    # -----------
                    # using depth first search to find all connected ('1') locations, since we already know there
                    # are only two islands. so we only need to find the first one.
                    # -----------
                    self.dfs(grid, i, j, n, m, stack)
                    found = True
                    break
            if found:
                break
        steps = 0

        # -----------
        # breadth first search, once we find next '1', that is our final answer
        # -----------
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while stack:
            size = len(stack)
            level = []

            while (size):
                temp = stack.pop()
                size -= 1
                x, y = temp[0], temp[1]

                for dx, dy in dirs:
                    tx = x + dx
                    ty = y + dy
                    if tx < 0 or ty < 0 or tx >= n or ty >= m or grid[tx][ty] == 2:
                        continue
                    if grid[tx][ty] == 1:
                        return steps
                    grid[tx][ty] = 2
                    level.append((tx, ty))

            steps += 1
            stack = level

        return -1

    def dfs(self, A, row, col, n, m, stack):
        # -----------
        # we only need to find connected '1's. that's why we need grid[row][col]==1
        # -----------
        if row < 0 or col < 0 or row >= n or col >= m or A[row][col] != 1:
            return

        A[row][col] = 2
        # -----------
        # use stack for breath first search
        # -----------
        stack.append((row, col))

        self.dfs(A, row + 1, col, n, m, stack)
        self.dfs(A, row - 1, col, n, m, stack)
        self.dfs(A, row, col + 1, n, m, stack)
        self.dfs(A, row, col - 1, n, m, stack)


obj = Solution()
print(obj.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))

from typing import List


class Solution:
    """
    Approach:
    The problem can be solved using a breadth-first search (BFS) algorithm.
    We can use a queue to explore the grid cells in a breadth-first manner, starting from the top-left cell.
    At each step, we consider the neighboring cells that are valid and not visited yet,
    marking them as visited and adding them to the queue. We continue this process until we reach
    the bottom-right cell or exhaust all possible paths.

    Intuition:
    The intuition behind the solution is to explore all possible paths from the top-left cell to the bottom-right
    cell in the binary matrix. By using a breadth-first search, we ensure that we first explore all paths at
    the same distance level before moving to the next level. This guarantees that the first path we encounter
    from the top-left cell to the bottom-right cell will be the shortest path.

    We start by checking if the top-left or bottom-right cell is blocked (contains a 1). If either of them is blocked,
    it means there is no valid path, so we return -1.

    We initialize a queue and add the top-left cell with a distance of 1 to start the BFS traversal.
    We also mark the top-left cell as visited by changing its value to 1.

    In each iteration of the BFS loop, we dequeue a cell from the queue and check if it is the bottom-right cell.
    If it is, we return the distance of that cell as it represents the shortest path length.

    Next, we consider all possible directions (horizontal, vertical, and diagonal) from the current cell and check if
    the neighboring cells are valid and not visited yet (contain a 0). If a neighboring cell satisfies these conditions,
    we mark it as visited by changing its value to 1, enqueue it into the queue with an incremented distance, and
    continue the BFS traversal.

    If we exhaust all possible paths without reaching the bottom-right cell, it means there is no valid path,
    so we return -1.
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        queue = [(0, 0, 1)]
        grid[0][0] = 1

        for i, j, d in queue:
            if i == n - 1 and j == n - 1:
                return d

            directions = [
                (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),  # top
                (i, j - 1), (i, j + 1),  # mid
                (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)  # bottom
            ]

            for x, y in directions:
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    queue.append((x, y, d + 1))

        return -1


obj = Solution()
print(obj.shortestPathBinaryMatrix([[0, 1], [1, 0]]))

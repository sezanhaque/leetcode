from itertools import product
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        def DFS(n: int, row: int, col: int) -> Node:
            all_same = True

            for i, j in product(range(n), range(n)):
                if grid[row][col] != grid[row + i][col + j]:
                    all_same = False
                    break

            if all_same:
                return Node(grid[row][col], True, None, None, None, None)

            n >>= 1

            top_left = DFS(n, row, col)
            top_right = DFS(n, row, col + n)

            bottom_left = DFS(n, row + n, col)
            bottom_right = DFS(n, row + n, col + n)

            return Node(0, False, top_left, top_right, bottom_left, bottom_right)

        return DFS(len(grid), 0, 0)


obj = Solution()
print(obj.construct([[0, 1], [1, 0]]))

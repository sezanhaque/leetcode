from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        x, y, dx, dy = 0, 0, 1, 0

        for i in range(n * n):
            matrix[y][x] = i + 1
            if not 0 <= x + dx < n or not 0 <= y + dy < n or matrix[y + dy][x + dx] != 0:
                dx, dy = -dy, dx
            x, y = x + dx, y + dy

        return matrix

    def generateMatrix(self, n: int) -> List[List[int]]:
        res, lo = [[n * n]], n * n

        while lo > 1:
            lo, hi = lo - len(res), lo
            res = [[i for i in range(lo, hi)]] + [list(j) for j in zip(*res[::-1])]

        return res


obj = Solution()
print(obj.generateMatrix(3))

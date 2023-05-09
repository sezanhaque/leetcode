from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Let us use coordinate (x, y) and direction of movement (dx, dy).
        Each time when we reach point outside matrix we rotate. How we can rotate?
        We can either create array of rotations in advance or we can use the trick dx, dy = -dy, dx.
        Also, how we understand it is time to rotate? We will write already visited elements with *,
        so when we see * or we go outside the grid, it is time to rotate.
        """
        n, m = len(matrix[0]), len(matrix)
        x, y, dx, dy = 0, 0, 1, 0
        res = []

        for _ in range(m * n):
            if not 0 <= x + dx < n or not 0 <= y + dy < m or matrix[y + dy][x + dx] == "*":
                dx, dy = -dy, dx

            res.append(matrix[y][x])
            matrix[y][x] = "*"
            x, y = x + dx, y + dy

        return res

    def spiralOrder(self, matrix):
        """
        Take the first row plus the spiral order of the rotated remaining matrix.
        Inefficient for large matrices, but here I got it accepted in 40 ms, one of the fastest Python submissions.

        spiral_order([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

            = [1, 2, 3] + spiral_order([[6, 9],
                                        [5, 8],
                                        [4, 7]])

            = [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
                                                 [5, 4]])

            = [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
                                                          [5]])

            = [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

            = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

            = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

            = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        """
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


obj = Solution()
print(obj.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

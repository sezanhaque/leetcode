from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)

        # sum over each corner
        # top left = mat[i][i]
        # top right = mat[i][~i]
        # bottom left = mat[~i][i]
        # bottom right = mat[~i][~i]
        for i in range(n >> 1):
            res += mat[i][i] + mat[i][~i] + mat[~i][i] + mat[~i][~i]

        # if the length is odd then add the middle element
        if n & 1:
            i = n >> 1
            res += mat[i][i]

        return res

    def diagonalSum(self, mat: List[List[int]]) -> int:
        return sum(sum(row[j] for j in {i, len(row) - i - 1}) for i, row in enumerate(mat))

obj = Solution()
print(obj.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

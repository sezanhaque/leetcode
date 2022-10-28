class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Binary Search
        """
        length = len(matrix)
        row, column = 0, len(matrix[0]) - 1

        while row < length and column > -1:
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                row += 1
            else:
                column -= 1
        return False


print(
    Solution.searchMatrix(
        0,
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        5,
    )
)

print(
    Solution.searchMatrix(
        0,
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        20,
    )
)

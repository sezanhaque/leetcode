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

    # def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    #     rowLength, colLength = len(matrix), len(matrix[0])
    #     left, right = 0, rowLength * colLength - 1

    #     while left <= right:
    #         middle = (left + right) >> 1
    #         posM, posN = (middle // colLength), (middle % colLength)

    #         if matrix[posM][posN] == target:
    #             return True

    #         if target < matrix[posM][posN]:
    #             right = middle - 1
    #         else:
    #             left = middle + 1

    #     return False


print(Solution.searchMatrix(0, [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 34))
# print(Solution.searchMatrix(0, [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
# print(Solution.searchMatrix(0, [[1, 3]], 3))
# print(Solution.searchMatrix(0, [[1, 4], [2, 5]], 2))

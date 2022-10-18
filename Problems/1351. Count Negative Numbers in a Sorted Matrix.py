class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        def binarySearch(self, row: list[int]) -> int:
            # Binary Search
            left, right = 0, len(row) - 1

            while left <= right:
                mid = (left + right) >> 1

                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1

            return len(row) - left

        result = 0
        for row in grid:
            if row[-1] > 0:
                # If last element is positive - it means there are no negative numbers in a row
                continue
            elif row[0] < 0:
                # Check edge cases - if first element is < 0 - all elements in row are negative
                result += len(row)
                continue
            else:
                result += binarySearch(0, row)

        return result


print(
    Solution.countNegatives(
        0, [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    )
)
print(Solution.countNegatives(0, [[3, 2], [1, 0]]))

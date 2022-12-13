class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()

        res = 0

        for i in zip(*grid):
            res += max(i)
        return res


print(Solution.deleteGreatestValue(0, [[1, 2, 4], [3, 3, 1]]))  # 8

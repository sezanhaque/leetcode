class Solution:
    # Premium
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        ans = set(mat[0]).intersection(set(mat[1]))
        for i in range(2, len(mat)):
            ans = ans.intersection(mat[i])
        return min(ans) if ans else -1


print(
    Solution.smallestCommonElement(
        0,
        [
            [1, 2, 3, 4, 5, 6],
            [2, 4, 5, 6, 8, 10],
            [3, 5, 6, 7, 9, 11],
            [1, 3, 5, 6, 7, 9],
        ],
    )
)

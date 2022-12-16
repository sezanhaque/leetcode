from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return Solution.helper(0, text1, text2, 0, 0)

    @cache
    def helper(self, text1: str, text2: str, i: int, j: int) -> int:
        if i >= len(text1) or j >= len(text2):
            return 0

        if text1[i] == text2[j]:
            return 1 + Solution.helper(0, text1, text2, i + 1, j + 1)
        else:
            return max(
                Solution.helper(0, text1, text2, i + 1, j),
                Solution.helper(0, text1, text2, i, j + 1),
            )


print(Solution.longestCommonSubsequence(0, text1="abcde", text2="ace"))
print(Solution.longestCommonSubsequence(0, text1="ezupkr", text2="ubmrapg"))  # ur
print(
    Solution.longestCommonSubsequence(
        0, text1="ylqpejqbalahwr", text2="yrkzavgdmdgtqpg"
    )
)

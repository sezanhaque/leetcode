from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j - 1][i] > strs[j][i]:
                    res += 1
                    break

        return res

    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(any(a > b for a, b in zip(col, col[1:])) for col in zip(*strs))


obj = Solution()
print(obj.minDeletionSize(["cba", "daf", "ghi"]))

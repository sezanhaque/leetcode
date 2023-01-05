from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = Counter(tasks)
        res = 0

        for idx in counts:
            if counts[idx] == 1:
                return -1

            mod = counts[idx] % 3
            if mod == 0:
                res = res + counts[idx] // 3
            else:
                res = res + counts[idx] // 3 + 1

        return res

    def minimumRounds(self, tasks: List[int]) -> int:
        counts = Counter(tasks)
        res = 0

        for val in counts.values():
            if val == 1:
                return -1

            res += val // 3 + min(1, val % 3)

        return res


obj = Solution()
print(obj.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))

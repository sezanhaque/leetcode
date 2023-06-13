from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # count total number of column pair
        cols = Counter(zip(*grid))

        # count total number of row pair
        rows = Counter(map(tuple, grid))

        return sum(cols[i] * rows[i] for i in cols)


obj = Solution()
print(obj.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))

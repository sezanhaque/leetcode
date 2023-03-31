from functools import cache
from itertools import product
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        @cache
        def has_apple(start_row: int, start_col: int, end_row: int, end_col: int) -> bool:
            for row, col in product(range(start_row, end_row + 1), range(start_col, end_col + 1)):
                if pizza[row][col] == "A":
                    return True

            return False

            # we can write in one line
            # return any(pizza[row][col] == "A" for row, col in product(range(start_row, end_row + 1), range(start_col, end_col + 1)))

        @cache
        def DP(start_row: int, start_col: int, slices_left: int) -> int:
            if slices_left == 1 and has_apple(start_row, start_col, len(pizza) - 1, len(pizza[0]) - 1):
                return 1

            num_ways = 0

            for i in range(start_col + 1, len(pizza[0])):
                if has_apple(start_row, start_col, len(pizza) - 1, i - 1):
                    num_ways += DP(start_row, i, slices_left - 1)

            for j in range(start_row + 1, len(pizza)):
                if has_apple(start_row, start_col, j - 1, len(pizza[0]) - 1):
                    num_ways += DP(j, start_col, slices_left - 1)

            return num_ways

        return DP(0, 0, k) % (10 ** 9 + 7)


obj = Solution()
print(obj.ways(pizza=["A..", "AAA", "..."], k=3))
print(obj.ways(pizza=["A..", "AA.", "..."], k=3))
print(obj.ways(pizza=["A..", "A..", "..."], k=1))

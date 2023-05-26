from functools import cache
from typing import List


class Solution:
    @staticmethod
    def _suffix_sum(piles: List[int]) -> List[int]:
        suffix_sum = [0]

        for pile in reversed(piles):
            suffix_sum.append(suffix_sum[-1] + pile)

        suffix_sum.reverse()

        return suffix_sum

    def stoneGameII(self, piles: List[int]) -> int:
        suffix_sum = self._suffix_sum(piles)

        @cache
        def DFS(pile: int, M: int) -> int:
            sum_next_player = suffix_sum[pile]

            for next_pile in range(pile + 1, min(pile + 2 * M + 1, len(piles) + 1)):
                sum_next_player = min(
                    sum_next_player, DFS(next_pile, max(M, next_pile - pile))
                )

            sum_player = suffix_sum[pile] - sum_next_player

            return sum_player

        return DFS(0, 1)


obj = Solution()
print(obj.stoneGameII([2, 7, 9, 4, 4]))

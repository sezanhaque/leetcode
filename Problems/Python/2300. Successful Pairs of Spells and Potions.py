import bisect
from typing import List


class Solution:
    """
    Solution 1:
    1. Sort `potions` for binary search
    2. Traverse `spells`, for each element `spell`, compute the ceiling of the quotient of `(success + s - 1) // s`;
    3. Binary search the corresponding ceiling of each quotient in 2
    to find out how many pairs with a product at least `success`.

    If we use float `factor = success / s = 10 / 3 = 3.3333333333...3` (there are `k` 3's)
    then we will miss the correct `potions[i]` in binary search.

    In contrast, `(success + s - 1) // s = (10 + 3 - 1) // 3 = 4` will guarantee to obtain correct result.

    __________________________________________________________________________________________________________________

    Solution 2:
    1. Sort `potions` for binary search
    2. Traverse `spells`, for each element `spell`, check where spell * potion[mid] >= success;
    3. Binary search the corresponding ceiling of each quotient in 2
    to find out how many pairs with a product at least `success`.
    """

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def valid_position(needed: float) -> int:
            left, right = 0, len(potions)

            while left < right:
                mid = (left + right) >> 1

                if potions[mid] < needed:
                    left = mid + 1
                else:
                    right = mid

            return left

        return [len(potions) - valid_position((success + spell - 1) // spell) for spell in spells]

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        return [len(potions) - bisect.bisect_left(potions, (success + spell - 1) // spell) for spell in spells]

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        Solution 2:
        Simply we can check if the spell * potion is greater than or equal to success.
        """
        potions.sort()

        def valid_position(spell: int) -> int:
            left, right = 0, len(potions)

            while left < right:
                mid = (left + right) >> 1

                if spell * potions[mid] < success:
                    left = mid + 1
                else:
                    right = mid

            return left

        return [len(potions) - valid_position(spell) for spell in spells]


obj = Solution()
print(obj.successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))

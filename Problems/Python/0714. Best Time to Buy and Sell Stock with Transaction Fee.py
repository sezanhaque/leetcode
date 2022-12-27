from typing import List


class Solution:
    """
    If I am holding a share after today, then either I am just continuing holding the share I had yesterday,
    or that I held no share yesterday, but bought in one share today: hold = max(hold, cash - prices[i]).

    If I am not holding a share after today, then either I did not hold a share yesterday,
    or that I held a share yesterday, but I decided to sell it out today:
        cash = max(cash, hold + prices[i] - fee).


    Related leetcode challenge:

    Leetcode #121 Best Time to Buy and Sell Stock I

    Leetcode #122 Best Time to Buy and Sell Stock II

    Leetcode #123 Best Time to Buy and Sell Stock III

    Leetcode #188 Best Time to Buy and Sell Stock IV

    Leetcode #121 Best Time to Buy and Sell Stock with Transaction Fee

    Leetcode #309 Best Time to Buy and Sell Stock with Cooldown
    """

    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]

        for idx in range(1, len(prices)):
            # cash = what amount share I am holding +
            # current share price - fee
            cash = max(cash, hold + prices[idx] - fee)

            # hold = what cash I have - current price
            hold = max(hold, cash - prices[idx])

        return cash


obj = Solution()
print((obj.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2)))

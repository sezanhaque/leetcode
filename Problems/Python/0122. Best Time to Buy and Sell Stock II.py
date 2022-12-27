from typing import List


class Solution:
    """
    Check if the current day price is less than next day price.
    If so then subtract from it and add to the profit.

    Return the profit.

    Related leetcode challenge:

    Leetcode #121 Best Time to Buy and Sell Stock I

    Leetcode #122 Best Time to Buy and Sell Stock II

    Leetcode #123 Best Time to Buy and Sell Stock III

    Leetcode #188 Best Time to Buy and Sell Stock IV

    Leetcode #121 Best Time to Buy and Sell Stock with Transaction Fee

    Leetcode #309 Best Time to Buy and Sell Stock with Cooldown
    """

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for idx in range(len(prices) - 1):
            if prices[idx] < prices[idx + 1]:
                profit += prices[idx + 1] - prices[idx]

        return profit

    def maxProfit(self, prices: List[int]) -> int:
        return sum((prices[idx + 1] - prices[idx]) for idx in range(len(prices) - 1) if prices[idx] < prices[idx + 1])


obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))

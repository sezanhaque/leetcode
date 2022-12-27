from typing import List


class Solution:
    """
    Related leetcode challenge:

    Leetcode #121 Best Time to Buy and Sell Stock I

    Leetcode #122 Best Time to Buy and Sell Stock II

    Leetcode #123 Best Time to Buy and Sell Stock III

    Leetcode #188 Best Time to Buy and Sell Stock IV

    Leetcode #121 Best Time to Buy and Sell Stock with Transaction Fee

    Leetcode #309 Best Time to Buy and Sell Stock with Cooldown
    """

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        lowest_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            elif prices[i] - lowest_price > max_profit:
                max_profit = prices[i] - lowest_price
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        min_price = prices[0]
        profit = 0

        for idx in range(1, len(prices)):
            min_price = min(min_price, prices[idx])
            profit = max(profit, prices[idx] - min_price)

        return profit


obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))
# print(maxProfit(0, [7, 6, 4, 3, 1]))
# print(maxProfit(0, [1, 2]))

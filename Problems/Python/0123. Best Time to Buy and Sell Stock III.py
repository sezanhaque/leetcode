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
        # forward traversal, profits record the max profit
        # by the ith day, this is the first transaction
        current_min = prices[0]
        max_profit = 0
        profits = []

        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)

        # backward traversal, max_profit records the max profit
        # after the ith day, this is the second transaction
        total_max = max_profit = 0
        current_max = profits[-1]

        for idx in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[idx])
            max_profit = max(max_profit, current_max - prices[idx])
            total_max = max(total_max, max_profit + profits[idx])

        return total_max

    def maxProfit(self, prices: List[int]) -> int:
        """
        We can make at most 2 transactions.

        So we will loop through the prices and make 2 transactions.

        min_price_1: min price for 1st transaction.
        profit_1: profit after 1st transaction.
            current price - min_profit_1 = profit_1

        min_price_2: min price for 2nd transaction.
            After making profit_1, suppose we have $10.
            So, next time when we are buying any stock,
            we are actually giving that stock price - profit_1.
            So, current price - profit_1 = min_price_2

        profit_2: profit after 2nd transaction.

        Complexity:
            Time:   O(n)
            Space:  O(1)

        @param prices: list[int]
        @return: profit_2
        """

        min_price_1 = prices[0]
        profit_1 = 0

        min_price_2 = prices[0]
        profit_2 = 0

        for idx in range(1, len(prices)):
            min_price_1 = min(min_price_1, prices[idx])
            profit_1 = max(profit_1, prices[idx] - min_price_1)

            min_price_2 = min(min_price_2, prices[idx] - profit_1)
            profit_2 = max(profit_2, prices[idx] - min_price_2)

        return profit_2


obj = Solution()
print(obj.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))

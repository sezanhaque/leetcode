from functools import cache
from math import inf
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
        length = len(prices)

        @cache
        def solve(day: int, buy: bool) -> int:
            # break condition
            if day >= length:
                return 0

            # buy
            if buy:
                # if we want to buy
                # we will call solve to next day to sell
                # and from that solve we will get our sell price
                # then we subtract that from present day price
                take = solve(day + 1, False) - prices[day]

                # if we want to hold
                # we will go to next day to buy
                hold = solve(day + 1, True)

            # sell
            else:
                # after selling we have to wait 1 day then buy
                # this will return buying price + current price
                take = solve(day + 2, True) + prices[day]

                # if we want to hold then we can't buy stock
                # without selling it first
                hold = solve(day + 1, False)

            return max(take, hold)

        return solve(0, True)

    def maxProfit(self, prices: List[int]) -> int:
        """
        free is the maximum profit I can have while being free to buy.
        have is the maximum profit I can have while having stock.
        cool is the maximum profit I can have while cooling down.
        """
        free = 0
        have = cool = -inf

        for p in prices:
            # Understand that all values (i.e. have, free and cool) are overwritten
            # at the same time is a key understanding to get this solution.
            # So we are writing them at same line.
            free, have, cool = max(free, cool), max(have, free - p), have + p

        return max(free, cool)

    def maxProfit(self, prices: List[int]) -> int:
        """
        cool_down denotes the max profit of current Day_i, with either do nothing,
        or just sell out on previous day and enter cooling on Day_i

        sell denotes the max profit of current Day_i, with selling stock with price quote of Day_i

        hold denotes the max profit of current Day_i, with keep holding or buy and hold on Day_i
        
        Solution Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solutions/761981/python-go-java-js-c-o-n-by-dp-and-state-machine-w-visualization/
        """
        cool_down, sell, hold = 0, 0, -inf

        for stock_price_of_Day_i in prices:
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold

            # Max profit of cooldown on Day i comes from either cool down of Day_i-1,
            # or sell out of Day_i-1 and today Day_i is cooling day
            cool_down = max(prev_cool_down, prev_sell)

            # Max profit of sell on Day_i comes from hold of Day_i-1 and sell on Day_i
            sell = prev_hold + stock_price_of_Day_i

            # Max profit of hold on Day_i comes from either hold of Day_i-1, or cool down on Day_i-1 and buy on Day_i
            hold = max(prev_hold, prev_cool_down - stock_price_of_Day_i)

        # The action of final trading day must be either sell or cool down
        return max(sell, cool_down)


obj = Solution()
print(obj.maxProfit([1, 2, 3, 0, 2]))

from math import inf
from typing import List


class Solution:
    """
    Use the idea of "reinvesting", we can "carry-over" a
    previous transaction into the next transaction in order
    to calculate a total profit.

    For example, given [3,2,6,5,7,0,3]

    If k = 1, then we would keep track of the lowest price and
    max profit for each day.

        3, min_price [3], max_profit [0]
        2, min_price [2], max_profit [0]
        6, min_price [2], max_profit [4]
        5, min_price [2], max_profit [4]
        7, min_price [2], max_profit [5]
        0, min_price [0], max_profit [5]
        3, min_price [0], max_profit [5]

    If k = 2, we want to understand how much money we could make
    if we "reinvest" profit from k = 1. This means we could only
    initiate a k=2 transaction IFF k=1 (on a previous day) has a
    non-zero max_profit.

        3, min_price [3, 3], max_profit [0, 0]
        2, min_price [2, 2], max_profit [0, 0]
        6, min_price [2, 2], max_profit [4, 4]
        5, min_price [2, 1], max_profit [4, 4]  <- Reinvest profit
        7, min_price [2, 1], max_profit [5, 6]
        0, min_price [0, -5], max_profit [5, 6]
        3, min_price [0, -5], max_profit [5, 8] <- Max profit with 2 transactions

    Notice that the new min_price is $1 when price is $5. Similarly, the new min_price
    is -$5 when price is $0. Why?

    To understand, imagine if we bought at $2 and sold at $6. Then bought at $5
    and sold at $7. That is two transactions with a total profit of
    $4 + $2 = $6.

    Alternative, we can also think of it as (-$2)(+$6)(-$5)(+$7). This means when
    the stock is at $5, we will use our profit to bring its effective price
    down to $1 (i.e. (-$2)(+$6)(-$5)). When we sell at $7, we capture a TOTAL
    profit of $6. Our tabulation is cumulative.


    If k = 3, we do the same thing:

        3, min_price [3, 3, 3], max_profit [0, 0, 0]
        2, min_price [2, 2, 2], max_profit [0, 0, 0]
        6, min_price [2, 2, 2], max_profit [4, 4, 4]
        5, min_price [2, 1, 1], max_profit [4, 4, 4]
        7, min_price [2, 1, 1], max_profit [5, 6, 6]
        0, min_price [0, -5, -6], max_profit [5, 6, 6]
        3, min_price [0, -5, -6], max_profit [5, 8, 9]


    Related leetcode challenge:

    Leetcode #121 Best Time to Buy and Sell Stock I

    Leetcode #122 Best Time to Buy and Sell Stock II

    Leetcode #123 Best Time to Buy and Sell Stock III

    Leetcode #188 Best Time to Buy and Sell Stock IV

    Leetcode #121 Best Time to Buy and Sell Stock with Transaction Fee

    Leetcode #309 Best Time to Buy and Sell Stock with Cooldown
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        # If k is greater than len(prices) / 2
        # then we will be able to make unlimited transaction
        # then it will be same problem as:
        #   Leetcode  # 122 Best Time to Buy and Sell Stock II
        if k > len(prices) >> 1:
            return sum((prices[idx + 1] - prices[idx]) for idx in range(len(prices) - 1) if prices[idx] < prices[idx + 1])

        min_price = [inf] * (k + 1)
        max_profit = [0] * (k + 1)

        for price in prices:
            for idx in range(1, k + 1):
                min_price[idx] = min(min_price[idx], price - max_profit[idx - 1])
                max_profit[idx] = max(max_profit[idx], price - min_price[idx])

        return max_profit[k]


obj = Solution()
print(obj.maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))

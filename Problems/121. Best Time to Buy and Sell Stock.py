def maxProfit(self, prices: list[int]) -> int:
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



print(maxProfit(0, [7, 1, 5, 3, 6, 4]))
# print(maxProfit(0, [7, 6, 4, 3, 1]))
# print(maxProfit(0, [1, 2]))

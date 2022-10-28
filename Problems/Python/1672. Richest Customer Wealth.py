from functools import reduce
from itertools import accumulate


def maximumWealth(self, accounts: list[list[int]]) -> int:
    return max([reduce(lambda x, y: x + y, account) for account in accounts])


def maximumWealth(self, accounts: list[list[int]]) -> int:
    """
    Fast
    """
    return max([sum(i) for i in accounts])


print(maximumWealth(0, [[1, 2, 3], [3, 2, 1]]))
print(maximumWealth(0, [[1, 5], [7, 3], [3, 5]]))
print(maximumWealth(0, [[2, 8, 7], [7, 1, 3], [1, 9, 5]]))

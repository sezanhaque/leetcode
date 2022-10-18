from math import sqrt


class Solution:
    def arrangeCoins(self, n: int) -> int:
        sums, i = 0, 0
        limit = n
        if not n & 1:
            n = (n >> 1) + 1
        else:
            n = (n >> 1) + 2
        for i in range(1, n):
            sums += i
            if sums > limit:
                return i - 1
        return i

    def arrangeCoins(self, n: int) -> int:
        # Fast
        return int(sqrt(1 + 8 * n) - 1) >> 1

    def arrangeCoins(self, n: int) -> int:
        # Binary Search
        left, right, result = 1, n, 0

        while left <= right:
            rows = (left + right) >> 1
            coinsNeeded = rows * (rows + 1) >> 1

            if coinsNeeded <= n:
                left, result = rows + 1, rows
            else:
                right = rows - 1
        return result


if __name__ == "__main__":
    print(Solution.arrangeCoins(0, 8))
    # print(Solution.arrangeCoins(0, 5))

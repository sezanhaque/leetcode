from typing import List


class Solution:
    @staticmethod
    def cmp(a, b):
        return (a > b) - (a < b)

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * 3
        for i in range(len(stoneValue) - 1, -1, -1):
            dp[i % 3] = max(sum(stoneValue[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))

        return ["Tie", "Alice", "Bob"][self.cmp(dp[0], 0)]

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 3

        for i in range(n - 1, -1, -1):
            takeOne = stoneValue[i] - dp[(i + 1) % 3]

            takeTwo = float('-inf')
            if i + 1 < n:
                takeTwo = stoneValue[i] + stoneValue[i + 1] - dp[(i + 2) % 3]

            takeThree = float('-inf')
            if i + 2 < n:
                takeThree = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[(i + 3) % 3]

            dp[i % 3] = max(takeOne, takeTwo, takeThree)

        value = dp[0]
        if value > 0:
            return "Alice"
        elif value < 0:
            return "Bob"
        else:
            return "Tie"


obj = Solution()
print(obj.stoneGameIII([1, 2, 3, 7]))

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(count["b"], count["a"], count["l"] >> 1, count["o"] >> 1, count["n"])

    def maxNumberOfBalloons(self, text: str) -> int:
        # NeetCode Solution

        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)  # or float("inf")
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        return res


# print(Solution.maxNumberOfBalloons(0, "nlaebolko"))
# print(Solution.maxNumberOfBalloons(0, "loonbalxballpoon"))
# print(Solution.maxNumberOfBalloons(0, "leetcode"))
# print(Solution.maxNumberOfBalloons(0, "balon"))
# print(Solution.maxNumberOfBalloons(0, "balllllllllllloooooooooon"))

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(count["b"], count["a"], count["l"] >> 1, count["o"] >> 1, count["n"])


# print(Solution.maxNumberOfBalloons(0, "nlaebolko"))
# print(Solution.maxNumberOfBalloons(0, "loonbalxballpoon"))
# print(Solution.maxNumberOfBalloons(0, "leetcode"))
# print(Solution.maxNumberOfBalloons(0, "balon"))
# print(Solution.maxNumberOfBalloons(0, "balllllllllllloooooooooon"))
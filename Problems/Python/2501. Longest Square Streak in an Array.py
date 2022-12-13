class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        dict = {}

        for i in nums:
            dict[i] = dict.get(i * i, 0) + 1
        res = max(dict.values())

        return res if res >= 2 else -1


print(Solution.longestSquareStreak(0, [4, 3, 6, 16, 8, 2]))

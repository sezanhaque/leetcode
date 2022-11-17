class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        max_distance = 0
        for i in range(len(colors)):
            for j in range(len(colors) - 1, 0, -1):
                if colors[i] != colors[j] and j > i:
                    max_distance = max(max_distance, j - i)
        return max_distance

    def maxDistance(self, colors: list[int]) -> int:
        """
        Iterate all element, and check its color with the first and the last house.
        """
        max_distance = 0

        for idx, val in enumerate(colors):
            # if curr value is not same as first value
            if val != colors[0]:
                max_distance = max(max_distance, idx)
            # if if curr value is not same as last value
            if val != colors[-1]:
                max_distance = max(max_distance, len(colors) - 1 - idx)
        return max_distance

    def maxDistance(self, colors: list[int]) -> int:
        """
        Find the first house with different color of the last house.
        Find the last house with different color of the first house.
        Return the max distance of these two options.
        """
        first, last = 0, len(colors) - 1

        while colors[first] == colors[-1]:
            first += 1
        while colors[last] == colors[0]:
            last -= 1

        return max(last, len(colors) - 1 - first)


print(Solution.maxDistance(0, [1, 1, 1, 6, 1, 1, 1, 1, 3]))
print(Solution.maxDistance(0, [1, 8, 3, 8, 3]))
print(Solution.maxDistance(0, [0, 1]))
print(Solution.maxDistance(0, [9, 9, 9, 18, 9, 9, 9, 9, 9, 18]))
print(Solution.maxDistance(0, [6, 6, 6, 6, 6, 6, 6, 6, 6, 19, 19, 6, 6]))
print(Solution.maxDistance(0, [4, 4, 4, 11, 4, 4, 11, 4, 4, 4, 4, 4]))  # 8

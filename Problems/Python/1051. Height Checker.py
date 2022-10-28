class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        sortedHeights = sorted(heights)
        result = 0
        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]:
                result += 1

        return result
    
    def heightChecker(self, heights: list[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))


print(Solution.heightChecker(0, [1, 1, 4, 2, 1, 3]))
print(Solution.heightChecker(0, [5, 1, 2, 3, 4]))
print(Solution.heightChecker(0, [1, 2, 3, 4, 5]))

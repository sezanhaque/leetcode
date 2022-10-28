class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        difference = (sum(bobSizes) - sum(aliceSizes)) >> 1
        bobSet = set(bobSizes)
        for candy in aliceSizes:
            if candy + difference in bobSet:
                return [candy, candy + difference]


print(Solution.fairCandySwap(0, [1, 1], [2, 2]))

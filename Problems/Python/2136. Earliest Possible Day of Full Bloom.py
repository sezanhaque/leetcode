class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        """
        Sort the grow time in descending order so that we can find the longest grow time.
        It will growing and we will be able to plant other plants by that time.
        """
        prevPlant, ans = 0, 0
        for grow, plant in sorted(zip(growTime, plantTime), reverse=True):
            print(grow, plant)
            ans = max(ans, (grow + plant + prevPlant))
            prevPlant += plant
        return ans

    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        """
        Imagine all flowers grow first (by them), and then you need to start planting.
        You start by planting the flower that "grew" first, then you plant the next flower that "grew", and so on.
        """
        ans = 0
        for grow, plant in sorted(zip(growTime, plantTime)):
            print(grow, plant)
            ans = max(ans, grow) + plant
        return ans


print(Solution.earliestFullBloom(0, [1, 4, 3], [2, 3, 1]))
# print(Solution.earliestFullBloom(0, [3, 4], [1, 3]))

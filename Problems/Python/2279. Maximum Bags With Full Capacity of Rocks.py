from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0
        diff = sorted(capacity[idx] - rocks[idx] for idx in range(len(capacity)))

        for idx in range(len(diff)):
            if additionalRocks >= diff[idx]:
                additionalRocks -= diff[idx]
                res += 1
            else:
                break

        return res


obj = Solution()
print(obj.maximumBags(capacity=[2, 3, 4, 5], rocks=[1, 2, 4, 4], additionalRocks=2))
print(obj.maximumBags(capacity=[10, 2, 2], rocks=[2, 2, 0], additionalRocks=100))
print(obj.maximumBags(capacity=[91, 54, 63, 99, 24, 45, 78], rocks=[35, 32, 45, 98, 6, 1, 25], additionalRocks=17))
print(obj.maximumBags(
    capacity=[54, 18, 91, 49, 51, 45, 58, 54, 47, 91, 90, 20, 85, 20, 90, 49, 10, 84, 59, 29, 40, 9, 100, 1, 64, 71, 30,
              46, 91],
    rocks=[14, 13, 16, 44, 8, 20, 51, 15, 46, 76, 51, 20, 77, 13, 14, 35, 6, 34, 34, 13, 3, 8, 1, 1, 61, 5, 2, 15, 18],
    additionalRocks=77)
)  # 13

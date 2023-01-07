from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = curr = 0

        for cost in sorted(costs):
            curr += cost
            if curr <= coins:
                res += 1
            else:
                break

        return res


obj = Solution()
print(obj.maxIceCream(costs=[1, 3, 2, 4, 1], coins=7))

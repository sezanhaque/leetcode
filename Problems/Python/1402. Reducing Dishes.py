from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res = curr_sum = 0

        # sort largest to smallest satisfaction
        for val in sorted(satisfaction, reverse=True):
            curr_sum += val
            # if it's no longer beneficial to serve the next dish
            if curr_sum < 0:
                break
            res += curr_sum

        return res


obj = Solution()
print(obj.maxSatisfaction([-1, -8, 0, 5, -9]))

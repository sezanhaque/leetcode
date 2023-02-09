from collections import defaultdict, Counter
from typing import List


class Solution:
    # sliding window problem
    def totalFruit(self, fruits: List[int]) -> int:
        res = total = left = 0
        count = Counter()

        for right, val in enumerate(fruits):
            count[val] += 1
            total += 1

            # while len of count is greater than 2
            # we will slide the window from left to right
            while len(count) > 2:
                fruit = fruits[left]
                count[fruit] -= 1
                total -= 1
                left += 1
                if not count[fruit]:
                    count.pop(fruit)

            res = max(res, total)

        return res


obj = Solution()
print(obj.totalFruit([0, 1, 2, 2]))

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = curr_sum = 0
        banned_set = set(banned)

        for num in range(1, n + 1):
            if curr_sum + num > maxSum:
                break
            if num not in banned_set:
                curr_sum += num
                res += 1

        return res


obj = Solution()
print(obj.maxCount(banned=[1, 6, 5], n=5, maxSum=6))
print(obj.maxCount(banned=[1, 2, 3, 4, 5, 6, 7], n=8, maxSum=1))
print(obj.maxCount(banned=[11], n=7, maxSum=50))

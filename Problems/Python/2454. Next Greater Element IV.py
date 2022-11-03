from collections import defaultdict
from sortedcontainers import SortedList


class Solution:
    def secondGreaterElement(self, nums: list[int]) -> list[int]:
        # ! Time limit exceeded
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            k = -1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j] and k == -1:
                    k = nums[j]
                elif nums[i] < k and nums[i] < nums[j]:
                    ans[i] = nums[j]
                    break
        return ans

    def secondGreaterElement(self, nums: list[int]) -> list[int]:
        tmp = defaultdict(list)

        for idx, val in enumerate(nums):
            tmp[val].append(idx)

        q = SortedList()
        res = [-1] * len(nums)

        for k in sorted(tmp.keys(), reverse=True):
            for i in tmp[k]:
                idx = q.bisect_left(i)
                if idx + 1 < len(q):
                    res[i] = nums[q[idx + 1]]
            for i in tmp[k]:
                q.add(i)

        return res

    def secondGreaterElement(self, nums: list[int]) -> list[int]:
        res, s1, s2 = [-1] * len(nums), [], []
        for i, a in enumerate(nums):
            while s2 and nums[s2[-1]] < a:
                res[s2.pop()] = a
            tmp = []
            while s1 and nums[s1[-1]] < a:
                tmp.append(s1.pop())
            s2 += tmp[::-1]
            s1.append(i)
        return res


print(Solution.secondGreaterElement(0, [2, 4, 0, 9, 6]))
# print(Solution.secondGreaterElement(0, [3, 3]))

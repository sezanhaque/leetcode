import bisect
from itertools import accumulate


def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
    def findSmaller(num: int, nums: list[int]):
        result = []
        sum = 0
        for _, v in enumerate(nums):
            if sum + v <= num:
                sum += v
                result.append(v)
        return len(result)

    result = []
    nums.sort()
    for _, v in enumerate(queries):
        result.append(findSmaller(v, nums))
    return result


def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
    nums.sort()

    pref = [0] * (len(nums) + 1)
    for i, num in enumerate(nums):
        pref[i + 1] = pref[i] + num
    result = [bisect.bisect_right(pref, query) - 1 for query in queries]
    return result


def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
    nums.sort()
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    res = []
    for q in queries:
        idx = bisect.bisect_right(nums, q)
        res.append(idx)
    return res


def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
    prefix = list(accumulate(sorted(nums)))
    return [bisect.bisect_right(prefix, q) for q in queries]


"""
Q & A

Q1: ans.append(bisect.bisect_right(prefix_sum, q) - 1) - what does this line mean?
A1: bisect.bisect_right(prefix_sum, q) - Binary search to find the largest index idx such that all 
prefix_sum[ : idx] <= q and all prefix_sum[idx :] > q. Since we put a dummy value 0 in the front 
of the prefix sum array prefix_sum, it is necessary to deduct 1 from idx. Therefore, idx - 1 is 
the longest size of subsequence that is no greater than q.
"""

print(answerQueries(0, [4, 5, 2, 1], [3, 10, 21]))  # [2,3,4]
# print(answerQueries(0, [2, 3, 4, 5], [1]))  # [0]
# print(
#     answerQueries(
#         0,
#         [736411, 184882, 914641, 37925, 214915],
#         [331244, 273144, 118983, 118252, 305688, 718089, 665450],
#     )
# )  # [2,2,1,1,2,3,3]
# print(
#     answerQueries(
#         0, [469781, 45635, 628818, 324948, 343772, 713803, 452081], [816646, 929491]
#     )
# )  # [3,3]

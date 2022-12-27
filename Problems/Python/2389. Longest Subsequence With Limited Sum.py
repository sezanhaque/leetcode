import bisect
from itertools import accumulate
from typing import List


class Solution:
    """
    We just have to check the sum and length of the subsequence, the order doesn't matter.
    Let's say you have this array [3, 2, 1, 5, 4]
    If it's in any arrangement [1,2,3,4,5], [1,2,3,5,4], [4,2,3,1,5], ....... and many more.
    The sum and its length will always be the same.

    And if you are wondering why even we need to sort the array?
    We have to give the longest length, which can only be achieved by taking small values into consideration first.
    And as we noticed rearranging doesn't affect the total sum, it means we can sort and choose elements from
    the beginning until the required sum is reached.

    Now see this example, arr = [2,3,4,1,1,1,3,54]
    you have to form the longest subseq with sum <= 6.
    So you have to take the smallest values first 1,1,1 then bigger 2
    Thus you have to take [2,1,1,1] subsequence
    Or [1,1,1,2] subseq if the array was sorted.

    Q & A

    Q1: ans.append(bisect.bisect_right(prefix_sum, q) - 1) - what does this line mean?
    A1: bisect.bisect_right(prefix_sum, q) - Binary search to find the largest index idx such that all
    prefix_sum[ : idx] <= q and all prefix_sum[idx :] > q. Since we put a dummy value 0 in the front
    of the prefix sum array prefix_sum, it is necessary to deduct 1 from idx. Therefore, idx - 1 is
    the longest size of subsequence that is no greater than q.
    """

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        result = []
        nums.sort()
        for _, v in enumerate(queries):
            result.append(self.findSmaller(v, nums))
        return result

    def findSmaller(self, num: int, nums: List[int]):
        result = []
        sums = 0
        for _, v in enumerate(nums):
            if v <= num and sums + v <= num:
                sums += v
                result.append(v)
        return len(result)

    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()

        pref = [0] * (len(nums) + 1)

        for i, num in enumerate(nums):
            pref[i + 1] = pref[i] + num
        result = [bisect.bisect_right(pref, query) - 1 for query in queries]

        return result

    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()

        # prefix sum
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


obj = Solution()
print(obj.answerQueries([4, 5, 2, 1], [3, 10, 21]))  # [2,3,4]
print(obj.answerQueries([2, 3, 4, 5], [1]))  # [0]
print(obj.answerQueries(
    [736411, 184882, 914641, 37925, 214915],
    [331244, 273144, 118983, 118252, 305688, 718089, 665450],
)
)  # [2,2,1,1,2,3,3]
print(obj.answerQueries([469781, 45635, 628818, 324948, 343772, 713803, 452081], [816646, 929491]))  # [3,3]

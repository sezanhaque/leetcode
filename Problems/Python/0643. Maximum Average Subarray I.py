from cmath import inf
import itertools
import operator


def findMaxAverage(self, nums: list[int], k: int) -> float:
    sums = [0] + list(itertools.accumulate(nums))
    return max(map(operator.sub, sums[k:], sums)) / k


def findMaxAverage(self, nums: list[int], k: int) -> float:
    # Time limit exceeded
    return max(sum(nums[i : i + k]) for i in range(len(nums) - k + 1)) / k


print(findMaxAverage(0, [1, 12, -5, -6, 50, 3], 4))
print(findMaxAverage(0, [5], 1))

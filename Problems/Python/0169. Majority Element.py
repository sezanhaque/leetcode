from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority = len(nums) >> 1
        count = Counter(nums)
        for i in count:
            if count[i] > majority:
                return i

    def majorityElement(self, nums: list[int]) -> int:
        return sorted(nums)[len(nums) >> 1]


print(Solution.majorityElement(0, [3, 2, 3]))
print(Solution.majorityElement(0, [2, 2, 1, 1, 1, 2, 2]))

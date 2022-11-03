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

    def majorityElement(self, nums: list[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
            
        return res

print(Solution.majorityElement(0, [3, 2, 3]))
print(Solution.majorityElement(0, [2, 2, 1, 1, 1, 2, 2]))

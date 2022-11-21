from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        left = 0
        while left < len(nums) - 1:
            right = left + 1
            while right < len(nums):
                if nums[left] == nums[right]:
                    count += 1
                right += 1
            left += 1
        return count

    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Algorithm:  Imagine a room with n people, each of whom shakes hands with everyone else.
                    If you focus on just one person you see that she participates in n-1 handshakes.
                    Since there are n people, that would lead to n(n-1) handshakes.
        Rule     :  n(n-1)/2.

        So, for every occurrences we will check how many pair will be there.
        """
        return sum(k * (k - 1) >> 1 for k in Counter(nums).values())


print(Solution.numIdenticalPairs(0, [1, 2, 3, 1, 1, 3]))
# print(Solution.numIdenticalPairs(0, [1, 1, 1, 1]))
# print(Solution.numIdenticalPairs(0, [1, 2, 3]))

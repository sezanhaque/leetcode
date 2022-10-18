from math import ceil


class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        """
        Binary Search
        """
        low, high = 1, max(nums)

        while low < high:
            mid = (low + high) >> 1

            if sum(ceil(num / mid) for num in nums) > threshold:
                low = mid + 1
            else:
                high = mid

        return low


print(Solution.smallestDivisor(0, [1, 2, 5, 9], 6))
print(Solution.smallestDivisor(0, [44, 22, 33, 11, 1], 5))

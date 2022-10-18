from collections import Counter


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        count = Counter(nums)
        for val in count:
            if count[val] == 1:
                return val

    def singleNonDuplicate(self, nums: list[int]) -> int:
        """
        Binary Search
        """
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == nums[mid ^ 1]:
                """
                odd xor 1 = odd - 1
                even xor 1 = even + 1
                mid ^ 1 equal to mid + 1 if mid >> 1 == 0 else mid - 1
                """
                left = mid + 1
            else:
                right = mid
        return nums[left]


# print(Solution.singleNonDuplicate(0, [1, 1, 2, 3, 3, 4, 4, 8, 8]))
# print(Solution.singleNonDuplicate(0, [3, 3, 7, 7, 10, 11, 11]))
print(Solution.singleNonDuplicate(0, [1, 1, 2]))

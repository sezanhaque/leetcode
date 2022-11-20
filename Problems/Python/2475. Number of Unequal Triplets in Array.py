from collections import Counter


class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        count = 0

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[i] == nums[j]:
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        count += 1

        return count

    def unequalTriplets(self, nums: list[int]) -> int:
        count = 0
        prev, nxt = 0, len(nums)
        items = Counter(nums).items()
        for _, frequency in items:
            nxt -= frequency
            count += prev * frequency * nxt
            prev += frequency
        return count


print(Solution.unequalTriplets(0, [4, 4, 2, 4, 3]))  # 3
print(Solution.unequalTriplets(0, [1, 1, 1, 1, 1]))  # 0
print(Solution.unequalTriplets(0, [1, 3, 1, 2, 4]))  # 7
# print(Solution.unequalTriplets(0, [2, 3, 4, 5]))  # 4

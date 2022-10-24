class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        count = 0
        numsSet = set(nums)

        for i in numsSet:
            if i - 1 not in numsSet:
                # Check if it is the start of a sequence if there is no num - 1
                length = 0
                while i + length in numsSet:
                    # Check the sequence
                    length += 1
                count = max(count, length)

        return count


print(Solution.longestConsecutive(0, [100, 4, 200, 1, 3, 2]))
# print(Solution.longestConsecutive(0, [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(Solution.longestConsecutive(0, [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))  # 7

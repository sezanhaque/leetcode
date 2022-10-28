class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        left, right, length = 0, 1, len(nums)

        while left < length and right < length:
            if not nums[left] & 1:
                left += 2
            elif nums[right] & 1:
                right += 2
            else:
                nums[left], nums[right] = nums[right], nums[left]

        return nums


print(Solution.sortArrayByParityII(0, [4, 2, 6, 8, 5, 7]))
# print(Solution.sortArrayByParityII(0, [3, 4]))
print(Solution.sortArrayByParityII(0, [4, 1, 2, 1]))

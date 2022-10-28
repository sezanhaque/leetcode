class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] & 1 and not nums[right] & 1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[left] & 1:
                right -= 1
            else:
                left += 1
        return nums

    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        return sorted(nums, key=lambda x: x & 1)

    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            if not nums[left] & 1:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        return nums


# print(Solution.sortArrayByParity(0, [3, 1, 2, 4]))
# print(Solution.sortArrayByParity(0, [0, 1, 2]))
print(Solution.sortArrayByParity(0, [1, 2, 3]))

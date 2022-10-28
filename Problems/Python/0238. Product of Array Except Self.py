class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        prefix, postfix = 1, 1

        # Calculate Prefix
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Calculate Postfix
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        left, right = 1, 1

        for i in range(len(nums)):
            result[i] *= left
            # "~ i" is equal to "-1 - i"
            result[~i] *= right
            left *= nums[i]
            right *= nums[~i]

        return result


print(Solution.productExceptSelf(0, [1, 2, 3, 4]))

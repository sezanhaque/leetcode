class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # Sliding Window
        
        left = ans = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]

            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1

        return ans


print(Solution.numSubarrayProductLessThanK(0, nums=[10, 5, 2, 6], k=100))

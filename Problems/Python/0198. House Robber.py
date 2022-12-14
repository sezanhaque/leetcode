from functools import cache


class Solution:
    def rob(self, nums: list[int]) -> int:
        length = len(nums)
        maxStolen = [0] * (length + 1)
        maxStolen[1] = nums[0]

        for i in range(2, len(maxStolen)):
            steal = nums[i - 1] + maxStolen[i - 2]
            skip = maxStolen[i - 1]

            maxStolen[i] = max(steal, skip)

        return maxStolen[length]

    def rob(self, nums: list[int]) -> int:
        """
        Same as previous one, but without using extra memory
                            # Fast
        """
        skip = steal = 0

        for num in nums:
            skip, steal = steal, max(skip + num, steal)

        return steal

    # __________ Using Dynamic Programing __________

    def rob(self, nums: list[int]) -> int:
        length = len(nums)

        # to store the calculated values
        seen = [-1] * 101

        def solve(idx: int) -> int:
            if idx >= length:
                return 0

            if seen[idx] != -1:
                return seen[idx]

            steal = nums[idx] + solve(idx + 2)
            skip = solve(idx + 1)

            seen[idx] = max(steal, skip)

            return seen[idx]

        return solve(0)

    def rob(self, nums: list[int]) -> int:
        length = len(nums)

        # by using "@cache", we don't need extra space to store
        # calculated values
        @cache
        def solve(idx: int) -> int:
            if idx >= length:
                return 0

            steal = nums[idx] + solve(idx + 2)
            skip = solve(idx + 1)

            return max(steal, skip)

        return solve(0)


print(Solution.rob(0, [1, 2, 3, 1]))

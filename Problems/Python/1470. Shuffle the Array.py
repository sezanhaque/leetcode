from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Fast
        """
        result = []
        for i in range(0, n):
            result.extend([nums[i], nums[i + n]])
        return result

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [num for idx in zip(nums[:n], nums[n:]) for num in idx]

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # bit manipulation
        # store x, y in the same idx
        for idx in range(n):
            # shift x by 10
            nums[idx] = nums[idx] << 10
            # store x, y
            nums[idx] = nums[idx] | nums[idx + n]

        j = 2 * n - 1
        for idx in range(n - 1, -1, -1):
            y = nums[idx] & (2 ** 10 - 1)
            x = nums[idx] >> 10

            nums[j] = y
            nums[j - 1] = x
            j -= 2

        return nums


obj = Solution()
print(obj.shuffle([2, 5, 1, 3, 4, 7], 3))
# print(obj.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))

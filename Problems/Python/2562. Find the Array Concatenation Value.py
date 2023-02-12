from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = sum(int(str(nums[idx]) + str(nums[~idx])) for idx in range(len(nums) >> 1))

        # if nums is an odd length list then add the middle
        # one to the result else return result only
        return res + nums[len(nums) >> 1] if len(nums) & 1 else res


obj = Solution()
print(obj.findTheArrayConcVal([7, 52, 2, 4]))
print(obj.findTheArrayConcVal([5, 14, 13, 8, 12]))
print(obj.findTheArrayConcVal([5]))

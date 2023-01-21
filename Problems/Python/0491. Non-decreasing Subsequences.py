from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def Backtracking(idx: int, subSequence: List[int]):
            # if the current sub-sequence has more than 1 value
            # then add the sub-seq to the res as the current
            # sub-sequence will already be verified by previous
            # backtracking call
            if len(subSequence) > 1:
                res.add(tuple(subSequence))

            if idx == len(nums):
                return

            # if the len of sub-sequence is 0 or
            # current idx value >= sub-sequence[-1]
            # then we have a new value
            if not subSequence or nums[idx] >= subSequence[-1]:
                Backtracking(idx + 1, subSequence + [nums[idx]])

            # else go to the next idx and call the backtracking
            Backtracking(idx + 1, subSequence)

        Backtracking(0, [])
        return res


obj = Solution()
print(obj.findSubsequences([4, 6, 7, 7]))

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_num1, set_num2 = set(nums1), set(nums2)
        return [list(set_num1.difference(set_num2)), list(set_num2.difference(set_num1))]


obj = Solution()
print(obj.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))

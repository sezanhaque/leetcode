from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums2)
        for num in nums1:
            if num in s:
                return num
        return -1

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = [val for val in nums1 if val in nums2]
        return min(common) if common else -1

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = list(set(nums1).intersection(nums2))
        return min(common) if common else -1

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # O(n) solution
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return -1


obj = Solution()
print(obj.getCommon(nums1=[1, 2, 3], nums2=[2, 4]))
print(obj.getCommon(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]))
print(obj.getCommon(nums1=[1, 2, 3], nums2=[4, 5, 6, 7, 8, 9]))

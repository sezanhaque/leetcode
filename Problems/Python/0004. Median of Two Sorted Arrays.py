class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sorted_arrays = sorted(nums1 + nums2)
        mid = len(sorted_arrays) >> 1
        if not len(sorted_arrays) & 1:
            return (sorted_arrays[mid] + sorted_arrays[mid - 1]) / 2
        else:
            return sorted_arrays[mid]


# print(Solution.findMedianSortedArrays(0, [1, 3], [2, 4]))
# print(Solution.findMedianSortedArrays(0, [1, 3], [2]))
# print(Solution.findMedianSortedArrays(0, [2, 4, 6], [1, 3, 5]))
# print(Solution.findMedianSortedArrays(0, [3], [-2, -1]))
print(Solution.findMedianSortedArrays(0, [1, 2, 5], [3, 6, 7]))

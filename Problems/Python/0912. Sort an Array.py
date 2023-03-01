from typing import List


class Solution:
    def mergeSort(self, array: list[int]):
        if len(array) > 1:

            #  mid is the point where the array is divided into two sub-arrays
            mid = len(array) >> 1
            left = array[:mid]
            right = array[mid:]

            # Sort the two halves
            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0

            # Until we reach either end of either left or right, pick larger among
            # elements left and right and place them in the correct position at A[p..mid]
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            # When we run out of elements in either left or right,
            # pick up the remaining elements and put in A[p..mid]
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums


obj = Solution()
print(obj.sortArray([5, 2, 3, 1]))

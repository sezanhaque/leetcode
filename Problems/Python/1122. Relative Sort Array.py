class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        """
        Sort array 1 then add the array 2 with it
        Now sort the array 1 with the key of new sorted array index
        """
        return sorted(arr1, key=(arr2 + sorted(arr1)).index)


print(
    Solution.relativeSortArray(
        0, [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]
    )
)

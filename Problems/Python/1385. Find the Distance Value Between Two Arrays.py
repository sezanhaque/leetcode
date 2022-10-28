class Solution:
    def search(self, arr: list[int], start: int, end: int) -> bool:
        """
        Binary Search
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) >> 1
            if start <= arr[mid] <= end:
                return False
            if arr[mid] < start:
                left = mid + 1
            else:
                right = mid - 1
        return True

    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0
        for num in arr1:
            if Solution.search(0, arr2, num - d, num + d):
                count += 1
        return count


print(Solution.findTheDistanceValue(0, [4, 5, 8], [10, 9, 1, 8], 2))
print(Solution.findTheDistanceValue(0, [1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3))
print(Solution.findTheDistanceValue(0, [2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))

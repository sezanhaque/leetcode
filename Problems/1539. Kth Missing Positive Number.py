from bisect import bisect_left


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) >> 1

            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid

        return left + k

    def findKthPositive(self, arr: list[int], k: int) -> int:
        class Count(object):
            def __getitem__(self, i):
                return arr[i] - i - 1
        return k + bisect_left(Count(), k, 0, len(arr))


print(Solution.findKthPositive(0, [2, 3, 4, 7, 11], 5))
# print(Solution.findKthPositive(0, [1, 2, 3, 4], 2))
# print(Solution.findKthPositive(0, [5, 6, 7, 8, 9], 9))

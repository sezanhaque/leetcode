class Solution:
    
    def check(mid: int, matrix: list[list[int]], length: int):
        i, j, cnt = 0, length - 1, 0
        for i in range(length):
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            cnt += j + 1
        return cnt
        
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        length, beg, end = len(matrix), matrix[0][0], matrix[-1][-1]

        while beg < end:
            mid = (beg + end) // 2
            if Solution.check(mid, matrix, length) < k:
                beg = mid + 1
            else:
                end = mid

        return beg


print(Solution.kthSmallest(0, [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))

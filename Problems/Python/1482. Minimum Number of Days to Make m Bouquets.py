class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        """
        Binary Search
        """
        if m * k > len(bloomDay):
            return -1

        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) >> 1

            flower, bouquet = 0, 0
            for bloom in bloomDay:
                flower = 0 if bloom > mid else flower + 1

                if flower >= k:
                    flower = 0
                    bouquet += 1
                    if bouquet == m:
                        break

            if bouquet == m:
                right = mid
            else:
                left = mid + 1

        return left


print(Solution.minDays(0, [7, 7, 7, 7, 12, 7, 7], 2, 3))

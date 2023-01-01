from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res: List[int] = []
        for num in range(left, right + 1):
            if self.isSelfDividingNumber(num):
                res.append(num)

        return res

    def isSelfDividingNumber(self, num: int) -> bool:
        length = num

        while length > 0:
            length, div = divmod(length, 10)
            if div == 0 or num % div != 0:
                return False

        return True


obj = Solution()
print(obj.selfDividingNumbers(left=1, right=22))

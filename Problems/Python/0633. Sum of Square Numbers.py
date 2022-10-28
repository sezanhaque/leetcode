from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
    
        def mySqrt(self, x: int) -> int:
            result = x
            while result * result > x:
                result = (result + x // result) >> 1
            return result

        left = 0
        # right = int(sqrt(c))
        right = mySqrt(0, c)
        while left <= right:
            cur = left * left + right * right
            if cur == c:
                return True
            if cur < c:
                left += 1
            else:
                right -= 1
        return False


if __name__ == "__main__":
    print(Solution.judgeSquareSum(0, 8))
    # print(Solution.judgeSquareSum(0, 3))
    # print(Solution.judgeSquareSum(0, 10))

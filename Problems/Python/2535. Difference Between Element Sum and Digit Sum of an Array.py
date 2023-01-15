from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = digitSum = 0

        for num in nums:
            digitSum += self.getDigitSum(num)
            elementSum += num

        return abs(elementSum - digitSum)

    def getDigitSum(self, num) -> int:
        res = 0

        while num > 0:
            num, reminder = divmod(num, 10)
            res += reminder

        return res


obj = Solution()
print(obj.differenceOfSum([1, 15, 6, 3]))
print(obj.differenceOfSum([1, 2, 3, 4]))

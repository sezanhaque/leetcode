from typing import List


class Solution:
    def get_digits(self, num: int, digits: list):
        if not num:
            return digits
        else:
            self.get_digits(num // 10, digits)
            digits.append(num % 10)
            return digits

    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            self.get_digits(num, res)

        return res

    def separateDigits(self, nums: List[int]) -> List[int]:
        return (int(digit) for num in nums for digit in str(num))


obj = Solution()
print(obj.separateDigits([13, 25, 83, 77]))
print(obj.separateDigits([7, 1, 3, 9]))

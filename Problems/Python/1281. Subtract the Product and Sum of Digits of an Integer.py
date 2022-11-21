from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = []
        while n != 0:
            n, remainder = divmod(n, 10)
            nums.append(remainder)
        multiply = reduce((lambda x, y: x * y), nums)
        return multiply - sum(nums)

    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sums = 0

        while n != 0:
            n, remainder = divmod(n, 10)
            product *= remainder
            sums += remainder

        return product - sums


print(Solution.subtractProductAndSum(0, 4421))

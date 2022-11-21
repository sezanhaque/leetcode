class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n != 0:
            n, reminder = divmod(n, k)
            res += reminder
        return res


print(Solution.sumBase(0, n=34, k=6))
print(Solution.sumBase(0, n=10, k=10))

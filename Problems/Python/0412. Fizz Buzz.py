class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res = []
        for i in range(1, n + 1):
            by3 = i % 3 == 0
            by5 = i % 5 == 0
            if by3 and by5:
                res.append("FizzBuzz")
            elif by3:
                res.append("Fizz")
            elif by5:
                res.append("Buzz")
            else:
                res.append(str(i))

        return res


print(Solution.fizzBuzz(0, 15))
print(Solution.fizzBuzz(0, 5))

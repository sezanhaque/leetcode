import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # remove leading whitespace
        s = re.findall("^[\+\-]*\d+", s)  # find "42" "+42" "-42" type pattern
        MAX, MIN = 2**31 - 1, -(2**31)
        try:
            res = int("".join(s))
            return max(min(res, MAX), MIN)
        except:
            return 0


print(Solution.myAtoi(0, "   -42"))
print(Solution.myAtoi(0, "42"))
print(Solution.myAtoi(0, "4193 with words"))
print(Solution.myAtoi(0, "words and 987"))

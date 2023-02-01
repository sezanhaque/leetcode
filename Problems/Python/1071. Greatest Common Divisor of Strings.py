import math


class Solution:
    """
    From 0 to Greatest common divisor of str1 and str2 will be the ans.
    """
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        maxLength = math.gcd(len(str1), len(str2))
        return str1[:maxLength]


obj = Solution()
print(obj.gcdOfStrings(str1="ABCABC", str2="ABC"))

from functools import cache


class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False

        f = self.isScramble

        for i in range(1, len(s1)):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
                    f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True

        return False


obj = Solution()
print(obj.isScramble(s1="great", s2="rgeat"))

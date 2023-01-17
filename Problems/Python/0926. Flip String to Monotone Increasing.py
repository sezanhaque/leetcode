class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = num = 0

        for char in s:
            if char == "0":
                res = min(num, res + 1)
            else:
                num += 1

        return res


obj = Solution()
print(obj.minFlipsMonoIncr("00110"))
print(obj.minFlipsMonoIncr("010110"))
print(obj.minFlipsMonoIncr("00011000"))

class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        tmp = []

        for char in s:
            if char in tmp:
                tmp = [char]
                res += 1
            else:
                tmp += [char]

        return res


obj = Solution()
print(obj.partitionString("abacaba"))

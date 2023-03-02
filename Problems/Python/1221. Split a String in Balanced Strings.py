class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = prefix = 0

        for char in s:
            prefix += 1 if char == "R" else - 1
            if not prefix:
                res += 1

        return res


obj = Solution()
print(obj.balancedStringSplit("RLRRLLRLRL"))

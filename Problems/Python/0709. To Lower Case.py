class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join(chr(ord(char) + 32) if "A" <= char <= "Z" else char for char in s)

    def toLowerCase(self, s: str) -> str:
        return s.lower()


obj = Solution()
print(obj.toLowerCase("Hello"))

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int((s.count(letter) / len(s)) * 100)


obj = Solution()
print(obj.percentageLetter(s="foobar", letter="o"))
print(obj.percentageLetter(s="sgawtb", letter="s"))  # 16

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        step = len(needle)

        for idx in range(len(haystack) - step + 1):
            if haystack[idx:idx + step] == needle:
                return idx

        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


obj = Solution()
print(obj.strStr(haystack="sadbutsad", needle="sad"))

from functools import cache
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def DFS(currStr: str, path: []):
            # if there is nothing in currStr
            # then append the path to res and return
            if not currStr:
                res.append(path)
                return

            # iterate from the index 1 to last of currStr
            # and check if the current portion from 0 to idx
            # is palindrome and if so then go to next idx
            # and add the current path to path
            for idx in range(1, len(currStr) + 1):
                # if they are palindrome
                if currStr[:idx] == currStr[:idx][::-1]:
                    DFS(currStr[idx:], path + [currStr[:idx]])

        DFS(s, [])
        return res

    @cache
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]

        res = []

        for idx in range(1, len(s) + 1):
            # if they are palindrome, prefix
            if s[:idx] == s[:idx][::-1]:
                # process suffix recursively
                for suffix in self.partition(s[idx:]):
                    res.append([s[:idx]] + suffix)

        return res


obj = Solution()
print(obj.partition("aab"))

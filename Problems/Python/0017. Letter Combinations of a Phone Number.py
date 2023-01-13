from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        hashmap = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                   '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        def DFS(pos: int, currStr: str) -> None:
            if pos == len(digits):
                res.append(currStr)
            else:
                letters = hashmap[digits[pos]]
                for letter in letters:
                    DFS(pos + 1, currStr + letter)

        DFS(0, "")

        return res


obj = Solution()
print(obj.letterCombinations(digits="23"))

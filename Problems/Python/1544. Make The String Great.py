from collections import deque


class Solution:
    def makeGood(self, s: str) -> str:
        left, right = 0, 1
        while right < len(s):
            if s[left].swapcase() == s[right]:
                s = s[:left] + s[right + 1:]
                if left == 0:
                    continue
                elif left > 0:
                    left -= 1
                    right -= 1
                    continue
            left += 1
            right += 1
        return s

    def makeGood(self, s: str) -> str:
        pointer = 0
        for i in range(len(s)):
            if pointer > 0 and s[i].swapcase() == s[pointer - 1]:
                pointer -= 1
            else:
                s = s[:pointer] + s[i] + s[pointer + 1:]
                pointer += 1
        return s[:pointer]

    def makeGood(self, s: str) -> str:
        # res = deque() # Using list
        res = [] # Using list
        for char in s:
            if res and res[-1].lower() == char.lower() and res[-1] != char:
                res.pop()
            else:
                res.append(char)
        return "".join(res)

print(Solution.makeGood(0, "hHcOzoC"))  # "cOzoC"
print(Solution.makeGood(0, "leEeetcode"))
print(Solution.makeGood(0, "abBAcC"))
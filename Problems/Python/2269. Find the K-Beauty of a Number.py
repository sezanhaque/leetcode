class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        strNum = str(num)
        ans = 0

        for i in range(len(strNum) - k + 1):
            tmp = int(strNum[i : i + k])
            if tmp != 0 and num % tmp == 0:
                ans += 1

        return ans


print(Solution.divisorSubstrings(0, 240, 2))
print(Solution.divisorSubstrings(0, 430043, 2))

class Solution:
    def sortSentence(self, s: str) -> str:
        strList = s.split()
        ans = [""] * len(strList)
        for i in range(len(strList)):
            idx = int(strList[i][-1])
            ans[idx - 1] = strList[i][:-1]
        return " ".join(ans)


print(Solution.sortSentence(0, "is2 sentence4 This1 a3"))

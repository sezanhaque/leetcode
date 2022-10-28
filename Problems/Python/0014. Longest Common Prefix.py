class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result

    def longestCommonPrefix(self, strs: list[str]) -> str:
        m = max(strs)
        n = min(strs)
        
        for i in range(len(n)):
            if m[i] != n[i]:
                return m[:i]
        return n 
             

print(Solution.longestCommonPrefix(0, ["flower", "flow", "flight"]))
print(Solution.longestCommonPrefix(0, ["dog", "racecar", "car"]))
print(Solution.longestCommonPrefix(0, ["cir", "car"]))
print(Solution.longestCommonPrefix(0, ["c", "acc", "ccc"]))
print(Solution.longestCommonPrefix(0, ["aa", "ab"]))
print(Solution.longestCommonPrefix(0, ["ab", "a"]))

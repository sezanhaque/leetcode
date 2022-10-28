class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                # If j == 0, it means i != j so return false
                # Or j and j-1 is not equal then it means j is not in i
                return False
        return i == len(name)


# print(Solution.isLongPressedName(0, "alex", "aaleex"))
# print(Solution.isLongPressedName(0, "saeed", "ssaaedd"))
# print(Solution.isLongPressedName(0, "xnhtq", "xhhttqq"))  # false
# print(Solution.isLongPressedName(0, "rick", "kric"))  # false
print(
    Solution.isLongPressedName(0, "zlexya", "aazlllllllllllllleexxxxxxxxxxxxxxxya")
)  # false

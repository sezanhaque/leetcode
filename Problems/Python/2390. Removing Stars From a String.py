def removeStars(self, s: str) -> str:
    # while s.__contains__("*"):
    #     idx = 0
    #     while idx < len(s) and len(s) > 0:
    #         if s[idx] == "*":
    #             s = s[: idx - 1] + s[idx + 1 :]
    #             idx -= 1
    #         else:
    #             idx += 1

    # while s.__contains__("*"):
    idx = 0
    while idx < len(s):
        if s[idx] == "*":
            s = s.replace(s[idx - 1] + s[idx], "")
            idx -= 1
        else:
            idx += 1

    # while s.__contains__("*"):
    #     idx = s.find("*")
    #     s = s.replace(s[idx - 1] + s[idx], "")
    return s


def removeStars(self, s: str) -> str:
    result = []
    for char in s:
        if char != "*":
            result.append(char)
        else:
            result.pop()
    return "".join(result)


print(removeStars(0, "leet**cod*e"))
# print(removeStars(0, "erase*****"))

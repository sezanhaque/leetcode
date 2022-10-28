def addToArrayForm(self, num: list[int], k: int) -> list[int]:
    if k == 0:
        return num
    string = ""
    for i in num:
        string += str(i)
    return [int(i) for i in string]


print(addToArrayForm(0, [2, 1, 5], 806))

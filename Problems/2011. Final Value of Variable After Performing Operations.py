def finalValueAfterOperations(self, operations: list[str]) -> int:
    my_dict = {
        "++X": 1,
        "X++": 1,
        "--X": -1,
        "X--": -1,
    }
    ans = 0
    for operation in operations:
        ans += my_dict[operation]
    return ans


def finalValueAfterOperations(self, operations: list[str]) -> int:
    ans = 0
    for operation in operations:
        if operation == "++X" or operation == "X++":
            ans += 1
        else:
            ans -= 1
    return ans


print(finalValueAfterOperations(0, ["--X", "X++", "X++"]))  # 1
print(finalValueAfterOperations(0, ["++X", "++X", "X++"]))  # 3
print(finalValueAfterOperations(0, ["X++", "++X", "--X", "X--"]))  # 0

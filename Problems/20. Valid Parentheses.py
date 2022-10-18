def isValid(self, s: str) -> bool:
    check = []
    for i in s:

        # if i is a left parenthesis, append it to the check list
        if i == "(" or i == "[" or i == "{":
            check.append(i)

        # if i is a right parenthesis, check if the last element in the check list is a left parenthesis
        elif i == ")":

            """
            if the check list is empty, return False
            if the last element in the check list is a left parenthesis, pop it off the list
            if not, return False
            """

            if len(check) == 0 or check.pop() != "(":
                return False
        elif i == "}":
            if len(check) == 0 or check.pop() != "{":
                return False
        elif i == "]":
            if len(check) == 0 or check.pop() != "[":
                return False

    # if the check list is empty, then the parentheses are valid
    return len(check) == 0


print(isValid(0, "({})[()]{}"))


def isValidTwo(self, s: str) -> bool:
    close_to_open = {")": "(", "}": "{", "]": "["}
    stack = []

    for c in s:
        if c in "({[":
            stack.append(c)
        else:
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(isValidTwo(0, "({})[()]{}"))

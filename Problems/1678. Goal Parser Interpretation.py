class Solution:
    def interpret(self, command: str) -> str:
        left, right = 0, 1

        while right < len(command):
            find = command[left : right + 1]
            if find == "()":
                command = command[:left] + "o" + command[right + 1 :]
            elif find == "(a":
                command = command[:left] + "al" + command[right + 3 :]
            left += 1
            right += 1
        return command

    def interpret(self, command: str) -> str:
        return command.replace("()", "(o)").replace("(", "").replace(")", "")


print(Solution.interpret(0, "G()(al)"))
print(Solution.interpret(0, "G()()()()(al)"))
print(Solution.interpret(0, "(al)G(al)()()G"))

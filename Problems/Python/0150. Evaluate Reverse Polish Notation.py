from collections import deque


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = deque()
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))

        return stack[0]

    def evalRPN(self, tokens: list[str]) -> int:
        stack = deque()

        for token in tokens:
            if token in "+-*/":
                stack.append(Solution.calculate(0, stack.pop(), stack.pop(), token))
            else:
                stack.append(int(token))

        return stack[0]

    def calculate(self, num1: int, num2:int, token: str) -> int:
        if token == "+":
            return num1 + num2
        elif token == "-":
            return num2 - num1
        elif token == "*":
            return num1 * num2
        elif token == "/":
            return int(num2 / num1)

print(
    Solution.evalRPN(
        0, ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)  # 22

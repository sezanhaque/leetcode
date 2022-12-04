from collections import deque

class MyStack:
    def __init__(self):
        self.input = deque()

    def push(self, x: int) -> None:
        self.input.appendleft(x)

    def pop(self) -> int:
        return self.input.popleft()

    def top(self) -> int:
        return self.input[0]

    def empty(self) -> bool:
        return not self.input


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

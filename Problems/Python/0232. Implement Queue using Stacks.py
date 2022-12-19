class MyQueue:
    def __init__(self):
        self.input, self.output = [], []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.move()
        return self.output.pop()

    def peek(self) -> int:
        self.move()
        return self.output[-1]

    def empty(self) -> bool:
        return (not self.input) and (not self.output)

    def move(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())


class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack = [x] + self.stack

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(4)
obj.push(3)
obj.pop()

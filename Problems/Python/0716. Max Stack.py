from collections import deque


class MaxStack:
    """
    # Premium
    """

    def __init__(self):
        self.stack = deque()
        self.maxStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        # checking min between current value and last value of maxStack
        val = max(val, self.maxStack[-1] if self.maxStack else val)
        self.maxStack.append(val)

    def pop(self) -> None:
        self.maxStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxStack[-1]

    def popMax(self) -> int:
        curMax = self.maxStack[-1]

        tmp = deque()
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] != curMax:
                tmp.append(self.stack.pop())
                self.maxStack.pop()
            else:
                self.stack.pop()
                self.maxStack.pop()
                break

        for val in reversed(tmp):
            self.push(val)

        return curMax


if __name__ == "__main__":
    obj = MaxStack()
    obj.push(-2)
    obj.push(4)
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.peekMax())
    # print(obj.pop())
    print(obj.popMax())
    print(obj.top())
    print(obj.popMax())
    print(obj.peekMax())

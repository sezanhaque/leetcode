class OrderedStream:
    def __init__(self, n: int):
        """
        Put a blank at the beginning AND the end of your stream.
        Then you don't even have to check about going off the far end.
        """
        self.stream = [None] * (n + 2)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream[idKey] = value

        if idKey == self.ptr:
            while self.stream[self.ptr] is not None:
                self.ptr += 1

        return self.stream[idKey : self.ptr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

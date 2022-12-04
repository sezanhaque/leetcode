class MyHashMap:
    def eval_hash(self, key):
        return ((key * 1031237) & (1 << 20) - 1) >> 5

    def __init__(self):
        self.arr = [[] for _ in range(1 << 15)]

    def put(self, key, value):
        t = self.eval_hash(key)
        for i, (k, v) in enumerate(self.arr[t]):
            if k == key:
                self.arr[t][i] = (k, value)
                return
        self.arr[t].append((key, value))

    def get(self, key):
        t = self.eval_hash(key)
        for i, (k, v) in enumerate(self.arr[t]):
            if k == key:
                return v
        return -1

    def remove(self, key: int):
        t = self.eval_hash(key)
        for i, (k, v) in enumerate(self.arr[t]):
            if k == key:
                self.arr[t].remove((k, v))


class MyHashMap:
    def __init__(self):
        self.data = [None] * 1000001

    def put(self, key: int, val: int) -> None:
        self.data[key] = val

    def get(self, key: int) -> int:
        val = self.data[key]
        return val if val != None else -1

    def remove(self, key: int) -> None:
        self.data[key] = None

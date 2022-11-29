from collections import defaultdict
import random


class RandomizedCollection:
    """
    My own solution 😃 with sort
    """

    def __init__(self):
        self.indices = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.indices:
            self.indices[val] = self.indices[val] + [len(self.arr)]
            self.arr.append(val)
            return False
        else:
            self.indices[val] = [len(self.arr)]
            self.arr.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        last_value = self.arr[-1]
        position = self.indices[val][-1]

        self.indices[last_value][-1] = position
        self.indices[last_value].sort()
        self.arr[position] = last_value

        self.indices[val].pop()
        if len(self.indices[val]) == 0:
            self.indices.pop(val)
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


class RandomizedCollection:
    def __init__(self):
        self.indices = defaultdict(set)
        self.arr = []

    def insert(self, val: int) -> bool:
        self.arr.append(val)
        self.indices[val].add(len(self.arr) - 1)
        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        if self.indices[val]:
            last_value, out = self.arr[-1], self.indices[val].pop()
            self.arr[out] = last_value
            if self.indices[last_value]:
                self.indices[last_value].add(out)
                self.indices[last_value].discard(len(self.arr) - 1)
            self.arr.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
obj.insert(1)
obj.insert(1)
obj.insert(2)
obj.insert(2)
obj.insert(2)

obj.remove(1)
obj.remove(1)
obj.remove(2)

obj.insert(1)
obj.remove(2)

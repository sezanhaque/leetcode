import random


class RandomizedSet:
    def __init__(self):
        # Store the indices of each value
        self.indices = {}

        # Store all values
        self.arr = []

    def insert(self, val: int) -> bool:
        # Return False if value is not present
        if val in self.indices:
            return False

        # Store the value with its index in the hashmap indices
        # Append the value to the array
        self.indices[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        # Get the last position of the array
        last_value = self.arr[-1]

        # Get the index of the value we want
        # to delete from the hashmap
        position = self.indices[val]

        # Change the index of last value with
        # the index of the value we want to delete
        self.indices[last_value] = position

        # Move the last value to the position
        # of the value we want to delete
        self.arr[position] = last_value

        # Delete the value from both
        self.indices.pop(val)
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.remove(2)
param_3 = obj.getRandom()

demo = dict()
demo[1] = ["hi"]
demo[1] = demo[1] + ["bye"]
tmp = demo[1][-1]
print(demo[1], tmp)

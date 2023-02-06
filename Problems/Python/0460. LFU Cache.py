from collections import defaultdict, OrderedDict


class Node:
    def __init__(self, key: int, val: int, count: int) -> None:
        self.key = key
        self.val = val
        self.count = count


class LFUCache(object):
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.count_to_node = defaultdict(OrderedDict)
        self.min_count = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        del self.count_to_node[node.count][key]

        # clean memory
        if not self.count_to_node[node.count]:
            del self.count_to_node[node.count]

        node.count += 1
        self.count_to_node[node.count][key] = node

        # if min_count node is empty it means we already
        # deleted that node, so increase min_count
        if not self.count_to_node[self.min_count]:
            self.min_count += 1

        return node.val

    def put(self, key: int, value: int) -> None:
        # if capacity is 0 then there is no space
        # to store any value
        if not self.capacity:
            return

        if key in self.cache:
            self.cache[key].val = value
            self.get(key)  # NOTICE, put makes count+1 too
            return

        if len(self.cache) == self.capacity:
            # popitem(last=False) is FIFO, like queue
            # it return key and value
            k, n = self.count_to_node[self.min_count].popitem(last=False)
            self.cache.pop(k)

        self.count_to_node[1][key] = self.cache[key] = Node(key, value, 1)
        self.min_count = 1

        return


lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))
lfu.put(3, 3)
print(lfu.get(2))
print(lfu.get(3))
lfu.put(4, 4)
print(lfu.get(1))
print(lfu.get(3))
print(lfu.get(4))
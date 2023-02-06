class Node:
    def __init__(self, key=None, val=None) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}  # hashmap from key to node

        # we will put new node between head & tail
        # head: most recently used node
        # tail: least recently used node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node: Node) -> None:
        # insert after head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node) -> None:
        # break the relation of curr node
        # from its previous and next node
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node: Node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # if key is in hashmap then remove the key
        # and create new node with new key then
        # insert the node to head
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if the capacity is full
        # then delete the least recently used node
        # from hashmap and update the tail
        if len(self.cache) > self.capacity:
            self.cache.pop(self.tail.prev.key)
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail


obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

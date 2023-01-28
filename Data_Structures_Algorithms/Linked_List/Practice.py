from Data_Structures_Algorithms.Helper.Messages import MESSAGE


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class SinglyLinkedList:
    def __init__(self, nodes=None):
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0

        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node
            self.size += 1

            for element in nodes:
                node.next = Node(data=element)
                node = node.next
                self.size += 1

            self.tail = node
        else:
            raise Exception(MESSAGE.empty.value)

    def __iter__(self):
        node: Node = self.head

        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        self.isEmpty()
        nodes = []

        # node: Node = self.head
        # while node is not None:
        #     nodes.append(node.data)
        #     node = node.next

        for node in self:
            nodes.append(node.data)

        nodes.append("None")
        return " -> ".join(nodes)

    def isEmpty(self):
        if self.head is None:
            raise Exception(MESSAGE.empty.value)

    def insertFirst(self, val):
        node = Node(val, next=self.head)
        self.head = node

        if self.tail is None:
            self.tail = node

        self.size += 1

    def insertLast(self, val):
        if self.head is None:
            return self.insertFirst(val)

        node = Node(val)
        self.tail.next = node
        self.tail = node

        self.size += 1

    def insertAfter(self, val, idx: int):
        self.isEmpty()

        if idx == self.size - 1:
            return self.insertLast(val)

        if idx >= self.size:
            raise Exception(MESSAGE.outOfBound.value)

        nodeAfter = self.getIdx(idx)
        newNode: Node = Node(val, next=nodeAfter.next)
        nodeAfter.next = newNode

        self.size += 1

    def getIdx(self, idx: int):
        self.isEmpty()

        tmpIdx = 0
        for node in self:
            if tmpIdx == idx:
                return node
            tmpIdx += 1

        raise Exception(MESSAGE.targetIdxNotFound.value % idx)


if __name__ == "__main__":
    singleLinkedList = SinglyLinkedList(["a", "b", "c"])
    singleLinkedList.insertFirst("0")
    singleLinkedList.insertAfter("d", 3)

    print(f"Head: {singleLinkedList.head}\t Tail: {singleLinkedList.tail}\t Size: {singleLinkedList.size}")
    print(singleLinkedList.__repr__())

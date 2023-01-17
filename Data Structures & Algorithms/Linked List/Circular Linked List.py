from Messages import MESSAGE


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __repr__(self):
        """
        Represent the linked list Node
        """
        return self.data


class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.head: Node = None
        self.tail: Node = None
        self.size = 0

        # quickly create a linked list
        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node
            self.tail = node
            self.size += 1

            for element in nodes:
                node.next = Node(data=element)
                node = node.next
                self.size += 1

            self.tail = node
            # make circle
            self.tail.next = self.head
        else:
            raise Exception(MESSAGE.empty.value)

    def __iter__(self):
        """
        Create a generator function for linked list
        it will help to traverse through a loop
        """
        self.isEmpty()

        node: Node = self.head

        yield node
        node = node.next

        while node is not self.head:
            yield node
            node = node.next

    def __repr__(self) -> str:
        """
        Represent the linked list
        Returns a string representation of the linked list
        """
        self.isEmpty()

        # with while loop
        # node: Node = self.head
        # nodes = [node.data]
        # node = node.next
        # while node is not self.head:
        #     nodes.append(node.data)
        #     node = node.next

        # or for loop
        nodes = []
        for node in self:
            nodes.append(node.data)

        nodes.append("None")
        return " -> ".join(nodes)

    def print(self):
        """
        Print the linked list
        """
        self.isEmpty()

        node: Node = self.head
        nodes = [node.data]
        node = node.next

        while node is not self.head:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        print(" -> ".join(nodes))

    def isEmpty(self):
        """
        Check if the linked list is empty.
        """
        if self.head is None:
            raise Exception(MESSAGE.empty.value)

    # __________ Starting Insertion of a linked list __________

    def insertFirst(self, val) -> None:
        """
        Insert a value at the beginning of a linked list
        """
        node = Node(val, next=self.head)
        self.head = node
        self.tail.next = node

        self.size += 1

    def insertLast(self, val):
        """
        Insert a value at the end of a linked list
        """
        # check if head is null
        # if so then we have null linked list
        # therefore we have to insert first
        if self.head is None:
            return self.insertFirst(val)

        node = Node(val, next=self.head)
        # the node which is in the tail,
        # make the new node as its next node
        self.tail.next = node
        # then update the tail as new node
        self.tail = node

        self.size += 1

    def insertAfter(self, val, idx: int):
        """
        Insert value after given idx in a linked list
        """
        if idx == self.size - 1:
            return self.insertLast(val)

        if idx >= self.size:
            raise Exception(MESSAGE.outOfBound.value)

        nodeAfter = self.getIdx(idx)
        newNode = Node(val, next=nodeAfter.next)
        nodeAfter.next = newNode

        if nodeAfter == self.tail:
            self.tail = newNode

        self.size += 1

    def addFirst(self, node: Node):
        """
        Add a node to the head of a linked list.
        """
        node.next = self.head
        self.head = node
        self.tail.next = node

        self.size += 1

    def addLast(self, node: Node):
        """
        Add a node to the last of a linked list.
        """
        # check if head is null
        # if so then we have null linked list
        # therefore we have to insert first
        if self.head is None:
            return self.addFirst(node)

        node.next = self.head
        # the node which is in the tail,
        # make the new node as its next node
        self.tail.next = node
        # then update the tail as new node
        self.tail = node

        self.size += 1

    def addAfter(self, targetNodeData, newNode: Node):
        """
        Add a node after the given value in a linked list.
        """
        self.isEmpty()

        nodeAfter = self.getNode(targetNodeData)
        newNode.next, nodeAfter.next = nodeAfter.next, newNode

        # update tail
        if self.tail == nodeAfter:
            self.tail = newNode

        self.size += 1

    def addBefore(self, targetNodeData, newNode: Node):
        """
        Add a node before given value in a linked list.
        """
        self.isEmpty()

        # if target node data is in head
        if self.head.data == targetNodeData:
            return self.addFirst(newNode)

        prevNode = self.head

        for node in self:
            if node.data == targetNodeData:
                prevNode.next, newNode.next = newNode, prevNode.next
                self.size += 1
                return
            prevNode = node

        raise Exception(MESSAGE.targetDataNotFound.value % targetNodeData)

    # __________ Finishing Insertion of a linked list __________

    # __________ Starting Deletion of a linked list __________

    def deleteIdx(self, idx: int):
        """
        Delete the given idx of a linked list
        """
        self.isEmpty()

        # if the idx is not present
        # then we don't have to delete anything
        if idx >= self.size:
            raise Exception(f"{idx}" + MESSAGE.notPresent.value)

        node: Node = self.head

        # if idx == 0, it means we have to
        # remove head
        if idx == 0:
            self.head = self.head.next
            self.tail.next = self.head
            self.size -= 1
            return

        # find the position - 1 of given idx
        for i in range(idx - 1):
            node = node.next

        # update tail
        if self.tail == node.next:
            self.tail = node

        node.next = node.next.next

        self.size -= 1

    def deleteNode(self, targetNodeData):
        """
        Delete a targeted node data from the linked list.
        """
        self.isEmpty()

        # if target data is in head
        if self.head.data == targetNodeData:
            self.head = self.head.next
            self.tail.next = self.head

            self.size -= 1
            return

        prevNode = self.head

        for node in self:
            if node.data == targetNodeData:
                prevNode.next = node.next
                if self.tail == node:
                    self.tail = prevNode
                self.size -= 1
                return
            prevNode = node

        raise Exception(MESSAGE.targetDataNotFound.value % targetNodeData)

    def getIdx(self, idx: int) -> Node:
        """
        Get the value of the given idx in a linked list
        """
        self.isEmpty()

        tmpIdx = 0
        for node in self:
            if tmpIdx == idx:
                return node
            tmpIdx += 1

        raise Exception(MESSAGE.targetIdxNotFound.value % idx)

    def getNode(self, targetNodeData) -> Node:
        """
        Get the node of targeted node from a linked list
        """
        self.isEmpty()

        for node in self:
            if node.data == targetNodeData:
                return node

        raise Exception(MESSAGE.targetDataNotFound.value % targetNodeData)

    def getMiddleElement(self) -> Node:
        """
        Get middle element of a linked list on single search
        """
        self.isEmpty()

        fast: Node = self.head
        slow: Node = self.head

        while fast.next is not self.head:
            fast = fast.next
            if fast.next is not self.head:
                fast = fast.next
                slow = slow.next

        # if we want second last one of an even
        # number of length linked list
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next

        return slow


if __name__ == "__main__":
    Llist = LinkedList(["a", "b", "d", "e"])

    # __________ Starting Insertion of a linked list __________
    # print(Llist.size)
    # Llist.insertFirst("0")
    Llist.insertLast("f")
    Llist.insertAfter("c", 2)
    Llist.addFirst(Node("0"))
    Llist.addLast(Node("g"))
    # Llist.addAfter("g", Node("h"))
    # Llist.addBefore("g", Node("i"))
    # Llist.insertLast("g")
    # Llist.insertLast("i")
    # Llist.insertLast("j")
    # Llist.addAfter("j", Node("k"))
    # Llist.addLast(Node("m"))
    # Llist.addLast(Node("m"))
    # Llist.addAfter("m", Node("n"))
    # __________ Finishing Insertion of a linked list __________

    # Llist.print()
    # Llist.deleteIdx(8)
    Llist.deleteNode("b")
    print(f"Head: {Llist.head}\t Tail: {Llist.tail}\t Tail.next: {Llist.tail.next}\t Size: {Llist.size}")
    print(Llist.__repr__())
    # print(Llist.getMiddleElement())
    # for node in Llist:
    #     print(node, end=" ")

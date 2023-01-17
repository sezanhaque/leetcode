from Messages import MESSAGE


class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        """
        Represent the linked list Node
        """
        return self.data


class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.head = None
        self.tail = None
        self.size = 0

        # quickly create a linked list
        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node
            self.size += 1

            for element in nodes:
                node.next = Node(data=element, prev=node)
                node = node.next
                self.size += 1

            self.tail = node
        else:
            raise Exception(MESSAGE.empty.value)

    def __iter__(self):
        """
        Create a generator function for linked list
        it will help to traverse through a loop
        """
        self.isEmpty()

        node: Node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        """
        Represent the linked list
        Returns a string representation of the linked list
        """
        self.isEmpty()

        nodes = []

        # with while loop
        # node: Node = self.head
        # while node is not None:
        #     nodes.append(node.data)
        #     node = node.next

        # or for loop
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
        last: Node = self.tail

        while node is not None:
            print(node.data + " -> ", end="")
            node = node.next
        print("None")

        print("Reversed Linked List:")
        while last:
            print(last.data + " -> ", end="")
            last = last.prev
        print("Start")

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
        self.head.prev = node
        self.head = node

        # check if tail is null
        # if so then add tail as head
        if self.tail is None:
            self.tail = self.head

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

        node = Node(val, prev=self.tail)
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
        newNode = Node(val, prev=nodeAfter, next=nodeAfter.next)
        nodeAfter.next = newNode

        if newNode.next:
            newNode.next.prev = newNode

        self.size += 1

    def addFirst(self, node: Node):
        """
        Add a node to the head of a linked list.
        """
        node.next = self.head
        self.head.prev = node
        self.head = node

        # check if tail is null
        # if so then add tail as head
        if self.tail is None:
            self.tail = self.head

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

        node.prev = self.tail
        self.tail.next = node
        self.tail = node

        self.size += 1

    def addAfter(self, targetNodeData, newNode: Node):
        """
        Add a node after the given value in a linked list.
        """
        self.isEmpty()

        nodeAfter = self.getNode(targetNodeData)
        nodeAfter.next = newNode
        newNode.prev = nodeAfter

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

        nodeBefore = self.getNode(targetNodeData)
        newNode.prev = nodeBefore.prev
        newNode.next = nodeBefore

        nodeBefore.prev.next = newNode
        nodeBefore.prev = newNode

        self.size += 1

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
            self.head.prev = None

            self.size -= 1
            return

        node = self.getIdx(idx)
        node.prev.next = node.next

        # if current node is not tail
        if node.next:
            # then assign prev of its next as its prev
            node.next.prev = node.prev
        else:
            # else we are in the tail so update it
            self.tail = node.prev

        self.size -= 1

    def deleteNode(self, targetNodeData):
        """
        Delete a targeted node data from the linked list.
        """
        self.isEmpty()

        # if target data is in head
        if self.head.data == targetNodeData:
            self.head = self.head.next
            self.head.prev = None

            self.size -= 1
            return

        node = self.getNode(targetNodeData)
        node.prev.next = node.next

        # if current node is not tail
        if node.next:
            # then assign prev of its next as its prev
            node.next.prev = node.prev
        else:
            # else we are in the tail so update it
            self.tail = node.prev

        self.size -= 1

    # __________ Finishing Deletion of a linked list __________

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

        while fast.next is not None:
            fast = fast.next
            if fast.next is not None:
                fast = fast.next
                slow = slow.next

        # if we want second last one of an even
        # number of length linked list
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next

        return slow

    # __________ Finishing Get element of a linked list __________

    def convertToList(self) -> list:
        """
        Convert a linked list to an array / list
        """
        self.isEmpty()
        return [node.data for node in self]


if __name__ == "__main__":
    Llist = LinkedList(["a", "b", "d", "e"])

    # __________ Starting Insertion of a linked list __________
    Llist.insertFirst("0")
    Llist.insertAfter("c", 2)
    Llist.insertLast("f")
    # Llist.addFirst(Node("A"))
    # Llist.insertLast("g")
    Llist.addLast(Node("g"))
    Llist.addAfter("g", Node("h"))
    # Llist.insertLast("i")
    # Llist.insertLast("j")
    # Llist.addAfter("h", Node("i"))
    # Llist.addLast(Node("m"))
    # Llist.addLast(Node("m"))
    Llist.addBefore("f", Node("g"))
    # Llist.addAfter("l", Node("m"))
    # __________ Finishing Insertion of a linked list __________

    # __________ Starting Get element of a linked list __________
    # print(Llist.getIdx(8))
    # print(Llist.getNode("a"))
    # print(Llist.getMiddleElement())
    # __________ Finishing Get element of a linked list __________

    # print(Llist.size)
    # Llist.deleteIdx(9)
    # Llist.deleteNode("a")
    # print(Llist.tail)
    print(Llist.print())
    # Llist.removeDuplicates()
    # Llist.__repr__()
    # Llist.reverse()
    # print(Llist.__repr__())
    # print(Llist.convertToList())

    # iterate over linked list
    # as we use __iter__ function
    # it will iterate over linked list
    # and give us the value
    # for node in Llist:
    #     print(node, end=" ")

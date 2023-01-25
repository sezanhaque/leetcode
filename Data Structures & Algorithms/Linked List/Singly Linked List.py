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
        self.head = None
        self.tail = None
        self.size = 0

        # quickly create a linked list
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

        # node: Node = self.head
        # with while loop
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
        nodes = []

        # while node is not None:
        #     nodes.append(node.data)
        #     node = node.next

        for node in self:
            nodes.append(node.data)

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
        node = Node(val, self.head)
        # node.next = self.head
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

        node = Node(val)
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

        self.size += 1

    def insertRecursively(self, val, currNode: Node, idx: int):
        """
        Insert the value at the given index recursively
        """
        if idx > self.size:
            raise Exception(MESSAGE.outOfBound.value)

        # if our head is None or index is 0
        # then we should add the value to the head
        if self.head is None or idx == 0:
            return self.insertFirst(val)

        if idx == 1:
            newNode = Node(val, next=currNode.next)
            currNode.next = newNode

            # if newNode is the last node
            # then update our tail
            if newNode.next is None:
                self.tail = newNode

            self.size += 1
            return newNode
        else:
            return self.insertRecursively(val, currNode.next, idx - 1)

    def addFirst(self, node: Node):
        """
        Add a node to the head of a linked list.
        """
        node.next = self.head
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

    # __________ Finishing Deletion of a linked list __________

    # __________ Starting Get element of a linked list __________

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

    def removeDuplicates(self):
        """
        Remove duplicates from a sorted linked list

        LeetCode: 83. Remove Duplicates from Sorted List
        Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
        """
        node = self.head

        while node.next:
            if node.data == node.next.data:
                node.next = node.next.next
                if self.tail.data == node.data:
                    self.tail = node
                self.size -= 1
            else:
                node = node.next

    def reverse(self):
        """
        Reverse a linked list
        """
        if self.size < 2:
            return

        prev: Node = None
        curr: Node = self.head
        self.tail = curr

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev


if __name__ == "__main__":
    Llist = LinkedList(["a", "b", "d", "e"])

    # __________ Starting Insertion of a linked list __________
    # print(Llist.size)
    Llist.insertAfter("c", 3)
    Llist.insertRecursively("f", Llist.head, 5)
    # Llist.insertLast("f")
    # Llist.insertLast("g")
    # Llist.insertLast("i")
    # Llist.insertLast("j")
    # Llist.addAfter("g", Node("h"))
    # Llist.addAfter("j", Node("k"))
    # Llist.addLast(Node("l"))
    # Llist.addLast(Node("m"))
    # Llist.addLast(Node("m"))
    # Llist.addBefore("m", Node("g"))
    # Llist.addAfter("m", Node("n"))
    # __________ Finishing Insertion of a linked list __________

    # __________ Starting Get element of a linked list __________
    # print(Llist.getIdx(10))
    # print(Llist.getNode("a"))
    # print(Llist.getMiddleElement())
    # __________ Finishing Get element of a linked list __________

    # Llist.deleteNode("m")
    print(Llist.size)
    # Llist.deleteIdx(4)
    # print(Llist.tail)
    # Llist.removeDuplicates()
    Llist.print()
    # print(Llist.__repr__())
    Llist.reverse()
    print(f"Head: {Llist.head}\t Tail: {Llist.tail}\t Size: {Llist.size}")
    print(Llist.__repr__())
    # print(Llist.convertToList())

    # iterate over linked list
    # as we use __iter__ function
    # it will iterate over linked list
    # and give us the value
    # for node in Llist:
    #     print(node, end=" ")

# Queue implementation in Python

class Queue:

    def __init__(self):
        self.queue = []

    # String representation of the queue
    def __str__(self):
        out = ""
        for el in self.queue:
            out += str(el) + "->"
        return out[:-2]

    # Get the size of the queue
    def __sizeof__(self):
        return len(self.queue)

    # Display the queue
    def display(self):
        print(self.queue)

    # Check if the queue is empty
    def isEmpty(self):
        return not self.queue

    # Get the top of the queue
    def top(self):
        if self.isEmpty():
            raise Exception("Popping from an empty queue")
        return self.queue[0]

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Popping from an empty queue")
        return self.queue.pop(0)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    # q.display()
    print(q)
    q.dequeue()
    q.dequeue()

    print("After removing an element")
    q.display()

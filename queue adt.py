class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()

    print("Is queue empty?", queue.is_empty())

    
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueueing:", queue.items)

   
    print("Front of queue:", queue.peek())

    
    print("Dequeued item:", queue.dequeue())
    print("Queue after dequeuing:", queue.items)

    
    print("Current queue size:", queue.size())

    print("Is queue empty?", queue.is_empty())

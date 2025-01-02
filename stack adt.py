class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()

    print("Is stack empty?", stack.is_empty())

    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushing:", stack.items)

    
    print("Top of stack:", stack.peek())

   
    print("Popped item:", stack.pop())
    print("Stack after popping:", stack.items)

   
    print("Current stack size:", stack.size())

    print("Is stack empty?", stack.is_empty())

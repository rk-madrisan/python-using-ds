class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        if self.is_empty():
            raise ValueError("List is empty")
        
        current = self.head
        while current:
            if current.data == data:
                # Update pointers
                if current.prev:
                    current.prev.next = current.next
                else:  # Deleting the head
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:  # Deleting the tail
                    self.tail = current.prev

                return  # Node deleted
            current = current.next
        raise ValueError(f"Value {data} not found in list")

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("Is the list empty?", dll.is_empty())

    
    dll.append(10)
    dll.append(20)
    dll.append(30)
    print("\nList after appending:")
    dll.display_forward()

    
    dll.prepend(5)
    print("\nList after prepending:")
    dll.display_forward()

    
    print("\nDisplay list backward:")
    dll.display_backward()

    
    dll.delete(20)
    print("\nList after deleting 20:")
    dll.display_forward()

    
    print("\nIs the list empty?", dll.is_empty())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            new_node = self.head    
        return self.head


    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def print_stack(self):
        while self.head.next is not None:
            print(self.head.data)
            self.head = self.head.next

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print_stack()

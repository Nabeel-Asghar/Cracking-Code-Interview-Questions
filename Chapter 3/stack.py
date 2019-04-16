class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            print("Stack is empty")
        else:
            return self.stack.pop()

    def is_empty(self):
        return (self.stack == [])

    def peek(self):
        return self.stack[0]


a = Stack()

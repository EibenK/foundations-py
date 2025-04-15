"""
Creates a stack(LIFO) implementation in Python - under-the-hood list container

Notes for code review:
    - Error handling
    - include git tagging (semantic versions)
    - abstraction/virtual functions for similiar datastructures
    - testing architecture
    - comments explaining each function

"""

class Stack():
    def __init__(self):
        self.stack_data = []

    def push(self, value):
        self.stack_data.append(None)

        # pushing into the front first - LIFO
        for i in range(len(self.stack_data) - 1, 0, -1):
            self.stack_data[i] = self.stack_data[i - 1]

        self.stack_data[0] = value    

    def pop(self):
        if len(self.stack_data) <= 0:
            return
        
        # popping from the front first - LIFO
        for i in range(1, len(self.stack_data)):
            self.stack_data[i - 1] = self.stack_data[i]
        
        self.stack_data = self.stack_data[:-1]

    def top(self):
        return self.stack_data[0]

    def is_empty(self):
        return (len(self.stack_data) == 0)

    def size(self):
        return len(self.stack_data)

    def clear(self):
        while(not self.is_empty()):
            self.pop()

    def display(self):
        # argument unpacking with *
        print("Data: ", *self.stack_data)
        
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    s.pop()
    s.display()
    s.pop()
    s.display()
    s.pop()
    s.display()

"""
Creates a pythonic(non-manual) queue(FIFO) implementation in Python - under-the-hood list container

Notes for code review:
    - Error handling
    - include git tagging (semantic versions)
    - abstraction/virtual functions for similiar datastructures
    - testing architecture
    - comments explaining each function

"""

from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, value):
        self.data.append(value)
        
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.data.popleft()
        
    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def front(self):
        return self.data[0]

    def back(self):
        return self.data[-1]

    def display(self):
        print("Data: ", *self.data)

    def clear(self):
        while not self.is_empty():
            self.dequeue()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    q.display() # Data:  10 20 30
    q.dequeue()
    q.display() # Data:  20 30
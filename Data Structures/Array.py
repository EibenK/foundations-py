"""
Creates a resizable array in Python - mimics array.array

Notes for code review:
    - Error handling
    - Add more types
    - fix bugs when you try to add a token that is not the same type as the array
    - include git tagging (semantic versions)
    - abstraction/virtual functions for similiar datastructures

"""


class Arr:    
    _type_validator = {
        "i": int,
        "b": str,
        "f": float,
    }
    
    def __init__(self, reference_type, arr):
        if reference_type not in self._type_validator:
            print(f"Type {reference_type} not implemented yet")
        
        self.reference_type = self._type_validator[reference_type]
        self.capacity = max(2, len(arr) * 2)
        self.length = len(arr)
        self.arr = [0] * self.capacity

        for i in range(self.length):
            if not isinstance(arr[i], self.reference_type):
                raise TypeError(f"Element {arr[i]} is not of type {self.reference_type}")
            self.arr[i] = arr[i]

    def _resize(self):
        self.capacity *= 2
        new_arr = [0] * self.capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def append(self, value):
        if not isinstance(value, self.reference_type):
            print(f"value is of type {type(value)} not of type {type(self.reference_type)}")
            return

        if self.length >= self.capacity:
            self._resize()

        self.arr[self.length] = value
        self.length += 1

    def pop(self):
        if self.length == 0:
            print("Nothing to pop")
            return
        
        self.length -= 1
        self.arr[self.length] = 0

    def count(self):
        return self.length

    def display(self):
        print("Data: ", ' '.join(str(self.arr[i]) for i in range(self.length)))


if __name__ == "__main__":
    a = Arr("i", [])
    a.append(1)
    a.append(2)
    a.append(4)
    a.append(5)
    a.pop()
    a.display()
    #a.append("c")
    a.display()
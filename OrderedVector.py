import numpy as np


class OrderedVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lastPosition = -1
        self.values = np.empty(self.capacity, dtype=int)

    def printVector(self):
        if self.lastPosition == -1:
            print("Vector is empty")
        else:
            for i in range(self.lastPosition + 1):
                print(i, ' - ', self.values[i])

    def add(self, value):
        if self.lastPosition == self.capacity - 1:
            print("Maximum capacity reached!")
            return
        position = 0
        for i in range(self.lastPosition + 1):
            position = i
            if self.values[i] > value:
                break
            if i == self.lastPosition:
                position = i + 1

        x = self.lastPosition
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1
        self.values[position] = value
        self.lastPosition += 1


vector = OrderedVector(10)
vector.add(4)
vector.add(2)
vector.add(5)
vector.add(1)
vector.add(8)
vector.add(10)
vector.add(9)
vector.printVector()

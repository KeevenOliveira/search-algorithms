import numpy as np


class OrderedVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lastPosition = -1
        self.values = np.empty(self.capacity, dtype=object)

    def printResult(self):
        if self.lastPosition == -1:
            print("Vector is empty")
        else:
            for i in range(self.lastPosition + 1):
                print(i, ' - ', self.values[i].vertex.tag, ' - ',
                      self.values[i].cost, ' - ',
                      self.values[i].vertex.distanceObjective,  ' - ',
                      self.values[i].distanceAStar
                )

    def add(self, adjacent):
        if self.lastPosition == self.capacity - 1:
            print("Maximum capacity reached!")
            return
        position = 0
        for i in range(self.lastPosition + 1):
            position = i
            if self.values[i].distanceAStar > adjacent.distanceAStar:
                break
            if i == self.lastPosition:
                position = i + 1

        x = self.lastPosition
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1
        self.values[position] = adjacent
        self.lastPosition += 1

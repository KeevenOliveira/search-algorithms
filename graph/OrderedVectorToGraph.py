import numpy as np

from graph.Graph import graph


class OrderedVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lastPosition = -1
        self.values = np.empty(self.capacity, dtype=object)

    def printVectors(self):
        if self.lastPosition == -1:
            print("Vector is empty")
        else:
            for i in range(self.lastPosition + 1):
                print(i, ' - ', self.values[i].tag, ' - ', self.values[i].distanceObjective)

    def add(self, vertex):
        if self.lastPosition == self.capacity - 1:
            print("Maximum capacity reached!")
            return
        position = 0
        for i in range(self.lastPosition + 1):
            position = i
            if self.values[i].distanceObjective > vertex.distanceObjective:
                break
            if i == self.lastPosition:
                position = i + 1

        x = self.lastPosition
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1
        self.values[position] = vertex
        self.lastPosition += 1

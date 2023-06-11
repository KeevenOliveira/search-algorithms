class Vertex:
    def __init__(self, tag, distanceObjective):
        self.tag = tag
        self.visited = False
        self.adjacents = []
        self.distanceObjective = distanceObjective

    def addAdjacent(self, adjacent):
        self.adjacents.append(adjacent)

    def showAdjacents(self):
        for i in self.adjacents:
            print(i.vertex.tag, i.cost)

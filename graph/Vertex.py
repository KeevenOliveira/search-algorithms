class Vertex:
    def __init__(self, tag):
        self.tag = tag
        self.visited = False
        self.adjacents = []

    def addAdjacent(self, adjacent):
        self.adjacents.append(adjacent)

    def showAdjacents(self):
        for i in self.adjacents:
            print(i.vertex.tag, i.cost)

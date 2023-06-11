class Adjacent:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost
        self.distanceAStar = vertex.distanceObjective + self.cost
    
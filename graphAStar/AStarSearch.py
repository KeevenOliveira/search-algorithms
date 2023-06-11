from graphAStar.OrderedVectorToGraph import OrderedVector


class AStarSearch:
    def __init__(self, objective):
        self.objective = objective
        self.found = False

    def search(self, present):
        print(' --------- ')
        print('Present: {}'.format(present.tag))
        present.visited = True

        if present == self.objective:
            self.found = True
        else:
            orderedVector = OrderedVector(len(present.adjacents))
            for adjacent in present.adjacents:
                if not adjacent.vertex.visited:
                    adjacent.vertex.visited = True
                    orderedVector.add(adjacent)
            orderedVector.printResult()

            if orderedVector.values[0] is not None:
                self.search(orderedVector.values[0].vertex)

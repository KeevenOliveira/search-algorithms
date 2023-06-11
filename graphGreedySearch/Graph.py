from graphGreedySearch.Adjacent import Adjacent
from graphGreedySearch.Vertex import Vertex


class Graph:
    arad = Vertex('Arad', 366)
    zerind = Vertex('Zerind', 374)
    oradea = Vertex('Oradea', 380)
    sibiu = Vertex('Sibiu', 253)
    timisoara = Vertex('Timisoara', 329)
    lugoj = Vertex('Lugoj', 244)
    mehadia = Vertex('Mehadia', 241)
    dobreta = Vertex('Dobreta', 242)
    craiova = Vertex('Craiova', 160)
    rimnicu = Vertex('Rimnicu', 193)
    fagaras = Vertex('Fagaras', 178)
    pitesti = Vertex('Pitestit', 98)
    bucharest = Vertex('Bucharest', 0)
    giurgiu = Vertex('Giurgiu', 77)

    arad.addAdjacent(Adjacent(zerind, 75))
    arad.addAdjacent(Adjacent(sibiu, 140))
    arad.addAdjacent(Adjacent(timisoara, 118))

    zerind.addAdjacent(Adjacent(arad, 75))
    zerind.addAdjacent(Adjacent(oradea, 71))

    oradea.addAdjacent(Adjacent(zerind, 71))
    oradea.addAdjacent(Adjacent(sibiu, 151))

    sibiu.addAdjacent(Adjacent(oradea, 151))
    sibiu.addAdjacent(Adjacent(arad, 140))
    sibiu.addAdjacent(Adjacent(fagaras, 99))
    sibiu.addAdjacent(Adjacent(rimnicu, 80))

    timisoara.addAdjacent(Adjacent(oradea, 118))
    timisoara.addAdjacent(Adjacent(lugoj, 111))

    lugoj.addAdjacent(Adjacent(timisoara, 111))
    lugoj.addAdjacent(Adjacent(mehadia, 70))

    mehadia.addAdjacent(Adjacent(lugoj, 70))
    mehadia.addAdjacent(Adjacent(dobreta, 75))

    dobreta.addAdjacent(Adjacent(mehadia, 75))
    dobreta.addAdjacent(Adjacent(craiova, 120))

    craiova.addAdjacent(Adjacent(dobreta, 120))
    craiova.addAdjacent(Adjacent(pitesti, 138))
    craiova.addAdjacent(Adjacent(rimnicu, 146))

    rimnicu.addAdjacent(Adjacent(craiova, 146))
    rimnicu.addAdjacent(Adjacent(sibiu, 80))
    rimnicu.addAdjacent(Adjacent(pitesti, 97))

    fagaras.addAdjacent(Adjacent(sibiu, 99))
    fagaras.addAdjacent(Adjacent(bucharest, 211))

    pitesti.addAdjacent(Adjacent(rimnicu, 97))
    pitesti.addAdjacent(Adjacent(craiova, 138))
    pitesti.addAdjacent(Adjacent(bucharest, 101))

    bucharest.addAdjacent(Adjacent(fagaras, 211))
    bucharest.addAdjacent(Adjacent(pitesti, 101))
    bucharest.addAdjacent(Adjacent(giurgiu, 90))


graph = Graph()

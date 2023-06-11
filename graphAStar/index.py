from graphAStar.AStarSearch import AStarSearch
from graphAStar.Graph import graph
from graphAStar.OrderedVectorToGraph import OrderedVector

vector = OrderedVector(3)
vector.add(graph.arad.adjacents[0])
vector.add(graph.arad.adjacents[1])
vector.add(graph.arad.adjacents[2])

aStarSearch = AStarSearch(graph.bucharest)
aStarSearch.search(graph.arad)

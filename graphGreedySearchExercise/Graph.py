from graphGreedySearch.Adjacent import Adjacent
from graphGreedySearch.Vertex import Vertex


class Graph:
    portoUniao = Vertex('Porto União', 203)
    pauloFrontin = Vertex('Paulo Frontin', 172)
    canoinhas = Vertex('Canoinhas', 141)
    tresBarras = Vertex('Três Barras', 131)
    saoMateusDoSul = Vertex('São Mateus do Sul', 123)
    irati = Vertex('Irati', 139)
    curitiba = Vertex('Curitiba', 0)
    palmeira = Vertex('Palmeira', 59)
    mafra = Vertex('Mafra', 94)
    campoLargo = Vertex('Campo Largo', 27)
    balsaNova = Vertex('Balsa Nova', 41)
    lapa = Vertex('Lapa', 74)
    tijucasDoSul = Vertex('Tijucas do Sul', 56)
    araucaria = Vertex('Araucária', 23)
    saoJoseDosPinhais = Vertex('São José dos Pinhas', 13)
    contenda = Vertex('Contenda', 39)

    portoUniao.addAdjacent(Adjacent(portoUniao, 46))
    portoUniao.addAdjacent(Adjacent(saoMateusDoSul, 87))
    portoUniao.addAdjacent(Adjacent(canoinhas, 78))

    canoinhas.addAdjacent(Adjacent(portoUniao, 78))
    canoinhas.addAdjacent(Adjacent(tresBarras, 12))
    canoinhas.addAdjacent(Adjacent(mafra, 66))

    mafra.addAdjacent(Adjacent(canoinhas, 66))
    mafra.addAdjacent(Adjacent(lapa, 57))
    mafra.addAdjacent(Adjacent(tijucasDoSul, 99))

    tijucasDoSul.addAdjacent(Adjacent(mafra, 99))
    tijucasDoSul.addAdjacent(Adjacent(saoJoseDosPinhais, 49))

    saoJoseDosPinhais.addAdjacent(Adjacent(tijucasDoSul, 49))
    saoJoseDosPinhais.addAdjacent(Adjacent(curitiba, 15))

    curitiba.addAdjacent(Adjacent(saoJoseDosPinhais, 15))
    curitiba.addAdjacent(Adjacent(araucaria, 37))
    curitiba.addAdjacent(Adjacent(balsaNova, 51))
    curitiba.addAdjacent(Adjacent(campoLargo, 29))

    campoLargo.addAdjacent(Adjacent(curitiba, 29))
    campoLargo.addAdjacent(Adjacent(balsaNova, 22))
    campoLargo.addAdjacent(Adjacent(palmeira, 55))

    palmeira.addAdjacent(Adjacent(campoLargo, 55))
    palmeira.addAdjacent(Adjacent(saoMateusDoSul, 77))
    palmeira.addAdjacent(Adjacent(irati, 75))

    irati.addAdjacent(Adjacent(palmeira, 75))
    irati.addAdjacent(Adjacent(saoMateusDoSul, 57))
    irati.addAdjacent(Adjacent(pauloFrontin, 75))

    pauloFrontin.addAdjacent(Adjacent(irati, 75))
    pauloFrontin.addAdjacent(Adjacent(portoUniao, 46))

    saoMateusDoSul.addAdjacent(Adjacent(portoUniao, 87))
    saoMateusDoSul.addAdjacent(Adjacent(tresBarras, 43))
    saoMateusDoSul.addAdjacent(Adjacent(irati, 57))
    saoMateusDoSul.addAdjacent(Adjacent(palmeira, 77))
    saoMateusDoSul.addAdjacent(Adjacent(lapa, 60))

    lapa.addAdjacent(Adjacent(saoMateusDoSul, 60))
    lapa.addAdjacent(Adjacent(mafra, 57))
    lapa.addAdjacent(Adjacent(contenda, 26))

    contenda.addAdjacent(Adjacent(lapa, 26))
    contenda.addAdjacent(Adjacent(balsaNova, 19))
    contenda.addAdjacent(Adjacent(araucaria, 18))

    araucaria.addAdjacent(Adjacent(contenda, 18))
    araucaria.addAdjacent(Adjacent(curitiba, 37))

    balsaNova.addAdjacent(Adjacent(contenda, 19))
    balsaNova.addAdjacent(Adjacent(campoLargo, 22))
    balsaNova.addAdjacent(Adjacent(curitiba, 51))

    tresBarras.addAdjacent(Adjacent(saoMateusDoSul, 43))
    tresBarras.addAdjacent(Adjacent(canoinhas, 12))


graph = Graph()

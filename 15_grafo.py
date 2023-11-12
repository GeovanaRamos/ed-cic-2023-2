class GrafoMatrizAdjacencia:
    def __init__(self):
        self.matriz_adjacencia = []
        self.vertices = []

    def adicionar_no(self, valor):
        self.vertices.append(valor)

        # Adiciona uma nova coluna para o novo nó em cada linha existente
        for linha in self.matriz_adjacencia:
            linha.append(0)

        # Adiciona uma nova linha para o novo nó
        nova_linha = [0] * len(self.vertices)
        self.matriz_adjacencia.append(nova_linha)

    def remover_no(self, valor):
        if valor in self.vertices:
            indice = self.vertices.index(valor)
            del self.vertices[indice]
            del self.matriz_adjacencia[indice]
            for linha in self.matriz_adjacencia:
                del linha[indice]

    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            indice_origem = self.vertices.index(origem)
            indice_destino = self.vertices.index(destino)

            self.matriz_adjacencia[indice_origem][indice_destino] = 1
            # Se o grafo é não-direcionado, você também pode adicionar:
            # self.matriz_adjacencia[indice_destino][indice_origem] = 1


class GrafoListaAdjacencia:
    def __init__(self):
        self.lista_adjacencia = {}
        self.vertices = []

    def adicionar_no(self, valor):
        self.lista_adjacencia[valor] = {'valor': valor, 'vizinhos': []}
        self.vertices.append(valor)

    def remover_no(self, valor):
        if valor in self.vertices:
            del self.vertices[self.vertices.index(valor)]
            del self.lista_adjacencia[valor]
            for outros_nos in self.lista_adjacencia.values():
                if valor in outros_nos['vizinhos']:
                    outros_nos['vizinhos'].remove(valor)

    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.lista_adjacencia[origem]['vizinhos'].append(destino)
            # Se o grafo é não-direcionado, você também pode adicionar:
            # self.lista_adjacencia[destino]['vizinhos'].append(origem)

# Exemplo de uso:
grafo_matriz = GrafoMatrizAdjacencia()
grafo_matriz.adicionar_no("A")
grafo_matriz.adicionar_no("B")
grafo_matriz.adicionar_aresta("A", "B")

grafo_lista = GrafoListaAdjacencia()
grafo_lista.adicionar_no("X")
grafo_lista.adicionar_no("Y")
grafo_lista.adicionar_aresta("X", "Y")

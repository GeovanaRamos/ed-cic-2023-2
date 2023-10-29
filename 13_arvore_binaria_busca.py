class Noh:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, noh, valor):
        if noh is None:
            return Noh(valor)
        if valor < noh.valor:
            noh.esquerda = self._inserir(noh.esquerda, valor)
        elif valor > noh.valor:
            noh.direita = self._inserir(noh.direita, valor)
        return noh

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, noh, valor):
        if noh is None or noh.valor == valor:
            return noh
        if valor < noh.valor:
            return self._buscar(noh.esquerda, valor)
        return self._buscar(noh.direita, valor)

    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)

    def _remover(self, noh, valor):
        if noh is None:
            return noh

        # Busca pelo nó a ser removido
        if valor < noh.valor:
            noh.esquerda = self._remover(noh.esquerda, valor)
        elif valor > noh.valor:
            noh.direita = self._remover(noh.direita, valor)
        else:
            # Caso 1: Nó folha ou caso 2: Nó com um filho
            if noh.esquerda is None:
                return noh.direita
            elif noh.direita is None:
                return noh.esquerda

            # Caso 3: Nó com dois filhos
            noh.valor = self._minimo_valor(noh.direita)
            noh.direita = self._remover(noh.direita, noh.valor)

        return noh

    def _minimo_valor(self, noh):
        while noh.esquerda is not None:
            noh = noh.esquerda
        return noh.valor

    def preordem(self):
        return self._preordem(self.raiz)

    def _preordem(self, noh):
        if noh is not None:
            print(noh.valor, end=' ')
            self._preordem(noh.esquerda)
            self._preordem(noh.direita)

    def emordem(self):
        return self._emordem(self.raiz)

    def _emordem(self, noh):
        if noh is not None:
            self._emordem(noh.esquerda)
            print(noh.valor, end=' ')
            self._emordem(noh.direita)

    def posordem(self):
        return self._posordem(self.raiz)

    def _posordem(self, noh):
        if noh is not None:
            self._posordem(noh.esquerda)
            self._posordem(noh.direita)
            print(noh.valor, end=' ')

# Exemplo de uso
arvore = ArvoreBinariaBusca()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)

print("Emordem antes da remoção:")
arvore.emordem()

valor_para_buscar = 7
resultado_busca = arvore.buscar(valor_para_buscar)
if resultado_busca:
    print(f"\nValor {valor_para_buscar} encontrado na árvore.")
else:
    print(f"\nValor {valor_para_buscar} não encontrado na árvore.")

arvore.remover(5)

print("\nEmordem após a remoção:")
arvore.emordem()


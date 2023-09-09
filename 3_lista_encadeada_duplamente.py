class Noh:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserir_inicio(self, valor):
        novo_no = Noh(valor)
        novo_no.proximo = self.cabeca
        if self.cabeca:
            self.cabeca.anterior = novo_no
        else:
            self.cauda = novo_no
        self.cabeca = novo_no

    def inserir_meio(self, posicao, valor):
        if posicao == 0:
            self.inserir_inicio(valor)
            return

        novo_no = Noh(valor)
        atual = self.cabeca
        for i in range(posicao - 1):
            if atual is None:
                raise Exception("Posição inválida")
            atual = atual.proximo
        novo_no.proximo = atual.proximo
        novo_no.anterior = atual
        if atual.proximo:
            atual.proximo.anterior = novo_no
        else:
            self.cauda = novo_no
        atual.proximo = novo_no

    def inserir_final(self, valor):
        novo_no = Noh(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            self.cauda = novo_no
            return
        self.cauda.proximo = novo_no
        novo_no.anterior = self.cauda
        self.cauda = novo_no

    def deletar_inicio(self):
        if not self.cabeca:
            return
        if self.cabeca.proximo:
            self.cabeca.proximo.anterior = None
        else:
            self.cauda = None
        self.cabeca = self.cabeca.proximo

    def deletar_meio(self, posicao):
        if posicao == 0:
            self.deletar_inicio()
            return
        atual = self.cabeca
        for i in range(posicao):
            if atual is None:
                raise Exception("Posição inválida")
            atual = atual.proximo
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        else:
            self.cauda = atual.anterior

    def deletar_final(self):
        if not self.cabeca:
            return
        if not self.cabeca.proximo:
            self.cabeca = None
            self.cauda = None
            return
        self.cauda.anterior.proximo = None
        self.cauda = self.cauda.anterior

    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def travessia(self):
        atual = self.cabeca
        while atual:
            print(atual.valor)
            atual = atual.proximo

# Testes
lista = ListaDuplamenteEncadeada()
lista.inserir_final(1)
lista.inserir_final(2)
lista.inserir_final(3)
lista.inserir_inicio(0)
lista.inserir_meio(2, 1.5)
print("Travessia após inserções:")
lista.travessia()

print("Buscar valor 2:", lista.buscar(2))
print("Buscar valor 4:", lista.buscar(4))

lista.deletar_inicio()
lista.deletar_meio(2)
lista.deletar_final()
print("Travessia após deleções:")
lista.travessia()


class Noh:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    # Inserção no início
    def inserir_inicio(self, valor):
        novo_no = Noh(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    # Inserção no meio
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
        atual.proximo = novo_no

    # Inserção no final
    def inserir_final(self, valor):
        novo_no = Noh(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    # Deleção no início
    def deletar_inicio(self):
        if not self.cabeca:
            return
        self.cabeca = self.cabeca.proximo

    # Deleção no meio
    def deletar_meio(self, posicao):
        if posicao == 0:
            self.deletar_inicio()
            return
        atual = self.cabeca
        for i in range(posicao - 1):
            if atual is None:
                raise Exception("Posição inválida")
            atual = atual.proximo
        if atual.proximo:
            atual.proximo = atual.proximo.proximo

    # Deleção no final
    def deletar_final(self):
        if not self.cabeca:
            return
        if not self.cabeca.proximo:
            self.cabeca = None
            return
        atual = self.cabeca
        while atual.proximo.proximo:
            atual = atual.proximo
        atual.proximo = None

    # Busca
    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    # Travessia
    def travessia(self):
        atual = self.cabeca
        while atual:
            print(atual.valor)
            atual = atual.proximo

# Testes
lista = ListaEncadeada()
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


class Noh:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.cabeca = None

    def inserir_inicio(self, valor):
        novo_no = Noh(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            novo_no.proximo = novo_no 
        else:
            temp = self.cabeca
            while temp.proximo != self.cabeca:
                temp = temp.proximo
            temp.proximo = novo_no
            novo_no.proximo = self.cabeca
            
    def inserir_meio(self, posicao, valor):
        if posicao == 0:
            self.inserir_inicio(valor)
            return

        novo_no = Noh(valor)
        atual = self.cabeca
        for i in range(posicao - 1):
            if atual.proximo == self.cabeca:
                break
            atual = atual.proximo
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no

    def inserir_final(self, valor):
        novo_no = Noh(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            novo_no.proximo = novo_no
        else:
            temp = self.cabeca
            while temp.proximo != self.cabeca:
                temp = temp.proximo
            temp.proximo = novo_no
            novo_no.proximo = self.cabeca

    def deletar_inicio(self):
        if not self.cabeca:
            return
        if self.cabeca.proximo == self.cabeca:
            self.cabeca = None
            return
        temp = self.cabeca
        while temp.proximo != self.cabeca:
            temp = temp.proximo
        temp.proximo = self.cabeca.proximo
        self.cabeca = self.cabeca.proximo

    def deletar_meio(self, posicao):
        if posicao == 0:
            self.deletar_inicio()
            return
        atual = self.cabeca
        anterior = None
        for i in range(posicao):
            if atual.proximo == self.cabeca:
                break
            anterior = atual
            atual = atual.proximo
        anterior.proximo = atual.proximo

    def deletar_final(self):
        if not self.cabeca:
            return
        if self.cabeca.proximo == self.cabeca:
            self.cabeca = None
            return
        temp = self.cabeca
        while temp.proximo.proximo != self.cabeca:
            temp = temp.proximo
        temp.proximo = self.cabeca

    def buscar(self, valor):
        atual = self.cabeca
        while True:
            if atual.valor == valor:
                return True
            atual = atual.proximo
            if atual == self.cabeca:
                break
        return False

    def travessia(self):
        if not self.cabeca:
            return
        atual = self.cabeca
        while True:
            print(atual.valor)
            atual = atual.proximo
            if atual == self.cabeca:
                break

# Testes
lista = ListaCircular()
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


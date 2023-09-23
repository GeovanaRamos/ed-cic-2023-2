class Noh:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class FilaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def enqueue(self, valor):
        novo_no = Noh(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo_no
        else:
            self.cauda.proximo = novo_no
            self.cauda = novo_no
            
    def dequeue(self):
        removido = self.cabeca.valor
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.proximo
        return removido


fila = FilaEncadeada()
fila.enqueue(2)
fila.enqueue(4)
fila.enqueue(6)
fila.enqueue(8)
fila.enqueue(10)
# fazer: tratar inserção na fila cheia


# fazer: chamar metodo que imprime a fila

print(fila.dequeue())
print(fila.dequeue())
print(fila.dequeue())
print(fila.dequeue())
print(fila.dequeue())
print(fila.dequeue()) # fazer: tratar remoção de fila vazia

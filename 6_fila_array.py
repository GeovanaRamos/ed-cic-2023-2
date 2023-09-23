class FilaArray:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        return self.itens.pop(0)
    
    

fila = FilaArray()
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

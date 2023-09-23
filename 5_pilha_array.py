class PilhaArray:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        return self.itens.pop()


pilha = PilhaArray()
pilha.push(2)
pilha.push(4)
pilha.push(6)
pilha.push(8)
pilha.push(10)
# fazer: tratar inserção na pilha cheia


# fazer: chamar metodo que imprime a pilha

print(pilha.pop())
print(pilha.pop())
print(pilha.pop())
print(pilha.pop())
print(pilha.pop())
print(pilha.pop()) # fazer: tratar remoção de pilha vazia
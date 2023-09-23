class Noh:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.cabeca = None

    def push(self, valor):
        novo_no = Noh(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def pop(self):
        removido = self.cabeca.valor
        self.cabeca = self.cabeca.proximo
        return removido


pilha = PilhaEncadeada()
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


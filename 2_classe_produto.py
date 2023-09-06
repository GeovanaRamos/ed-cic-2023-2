# Definição da classe com seus atributos e métodos/funções
class Produto:

    def __init__(self, nome, valor, tipo):
        self.nome = nome 
        self.valor = valor  
        self.tipo = tipo
            
    def eh_alimenticio(self):
        return self.tipo == "ALIMENTICIO"

    def imprime_no_extrato(self):
        return f"{self.nome}\t\tR$ {self.valor:.2f}"


# Função FORA da classe
def calcular_desconto_vale(produtos):
    total = 0
    print("Extrato do Vale-Alimentação:")

    for produto in produtos:
        if produto.eh_alimenticio():
            total += produto.valor
            print(produto.imprime_no_extrato())

    print(f"Total a ser descontado: R$ {total:.2f}")
    return total


# Criação dos objetos
produto_1 = Produto('Arroz', 12.34, 'ALIMENTICIO')
produto_2 = Produto('Feijao', 13.65, 'ALIMENTICIO')
produto_3 =  Produto('Desinfetante', 7.45, 'N_ALIMENTICIO')

# Adicionando os objetos em uma lista
produtos = [produto_1, produto_2, produto_3]

# Chamando função
calcular_desconto_vale(produtos)



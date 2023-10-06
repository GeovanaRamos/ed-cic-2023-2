def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        metade_esquerda = lista[:meio]
        metade_direita = lista[meio:]

        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0

        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                lista[k] = metade_esquerda[i]
                i += 1
            else:
                lista[k] = metade_direita[j]
                j += 1
            k += 1

        while i < len(metade_esquerda):
            lista[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            lista[k] = metade_direita[j]
            j += 1
            k += 1

# Exemplo de uso
lista = [64, 25, 12, 22, 11]

# Criando cópias da lista original para cada algoritmo
lista_bubble = lista.copy()
lista_selection = lista.copy()
lista_insertion = lista.copy()
lista_merge = lista.copy()

print("Lista original:", lista)

bubble_sort(lista_bubble)
print("Bubble Sort:", lista_bubble)

selection_sort(lista_selection)
print("Selection Sort:", lista_selection)

insertion_sort(lista_insertion)
print("Insertion Sort:", lista_insertion)

merge_sort(lista_merge)
print("Merge Sort:", lista_merge)


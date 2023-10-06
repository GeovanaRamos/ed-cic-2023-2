def busca_linear_n_ordenada(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # Retorna o índice se o elemento for encontrado
    return -1  # Retorna -1 se o elemento não estiver na lista

def busca_linear_ordenada(arr, alvo):
    for i, valor in enumerate(arr):
        if valor == alvo:
            return i  # Elemento encontrado, retorna o índice
        elif valor > alvo:
            return -1  # Elemento não está na lista, pois a lista está ordenada

    return -1  # Elemento não encontrado

def busca_binaria(arr, alvo):
    inf, sup = 0, len(arr) - 1

    while inf <= sup:
        meio = (inf + sup) // 2
        meio_val = arr[meio]

        if meio_val == alvo:
            return meio  # Elemento encontrado, retorna o índice
        elif meio_val < alvo:
            inf = meio + 1
        else:
            sup = meio - 1

    return -1  # Elemento não encontrado

def busca_binaria_recursiva(arr, alvo, inf, sup):
    if inf <= sup:
        meio = (inf + sup) // 2
        meio_val = arr[meio]

        if meio_val == alvo:
            return meio  # Elemento encontrado, retorna o índice
        elif meio_val < alvo:
            return busca_binaria_recursiva(arr, alvo, meio + 1, sup)
        else:
            return busca_binaria_recursiva(arr, alvo, inf, meio - 1)

    return -1  # Elemento não encontrado


lista_n_ordenada = [4, 2, 7, 1, 9, 5, 8]
elemento_n_ordenada = 5

lista_ordenada = [1, 2, 4, 5, 7, 8, 9]
elemento_ordenada = 7

lista_binaria = [1, 2, 4, 5, 7, 8, 9]
elemento_binaria = 5

resultado_busca_linear_n_ordenada = busca_linear_n_ordenada(lista_n_ordenada, elemento_n_ordenada)
resultado_busca_linear_ordenada = busca_linear_ordenada(lista_ordenada, elemento_ordenada)
resultado_busca_binaria = busca_binaria(lista_binaria, elemento_binaria)
resultado_busca_binaria_recursiva = busca_binaria_recursiva(lista_binaria, elemento_binaria, 0, len(lista_binaria) - 1)

print(f"Busca Linear Não Ordenada: Elemento {elemento_n_ordenada} encontrado no índice {resultado_busca_linear_n_ordenada}" if resultado_busca_linear_n_ordenada != -1 else f"Elemento {elemento_n_ordenada} não encontrado na lista não ordenada")

print(f"Busca Linear Ordenada: Elemento {elemento_ordenada} encontrado no índice {resultado_busca_linear_ordenada}" if resultado_busca_linear_ordenada != -1 else f"Elemento {elemento_ordenada} não encontrado na lista ordenada")

print(f"Busca Binária: Elemento {elemento_binaria} encontrado no índice {resultado_busca_binaria}" if resultado_busca_binaria != -1 else f"Elemento {elemento_binaria} não encontrado na lista para busca binária")

print(f"Busca Binária Recursiva: Elemento {elemento_binaria} encontrado no índice {resultado_busca_binaria_recursiva}" if resultado_busca_binaria_recursiva != -1 else f"Elemento {elemento_binaria} não encontrado na lista para busca binária recursiva")



def calcular_desconto_vale(nomes_produtos, valores_produtos, tipos_produtos):
    total = 0
    print("Extrato do Vale-Alimentação:")
    
    for nome, valor, tipo in zip(nomes_produtos, valores_produtos, tipos_produtos):
        if tipo == "ALIMENTICIO":
            total += valor
            print(f"{nome}: R${valor:.2f}")
    
    print(f"Total a ser descontado: R${total:.2f}")


nomes_produtos = ["Arroz", "Feijão", "Guardanapo", "Leite", "Ovo", "Pão", "Carne", "Cenoura", "Shampoo", "Sabonete"]
valores_produtos = [2.5, 3.0, 1.8, 2.2, 0.25, 1.0, 8.5, 0.8, 4.0, 1.2]
tipos_produtos = [
    "ALIMENTICIO", "ALIMENTICIO", "N_ALIMENTICIO", "ALIMENTICIO", "ALIMENTICIO",
    "ALIMENTICIO", "ALIMENTICIO", "ALIMENTICIO", "N_ALIMENTICIO", "N_ALIMENTICIO"
]

calcular_desconto_vale(nomes_produtos, valores_produtos, tipos_produtos)

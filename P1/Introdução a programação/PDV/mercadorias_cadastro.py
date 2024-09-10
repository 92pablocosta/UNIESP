mercadorias = {
    "item": [],
    "valor": [],# Dicionario e lista vazia precisam de , pra funcionar e tomar cuidado onde esta pondo dentro o codigo pois dependendo n funciona
    "estoque": []
}

# Adiciona o item
def adicionar_item():
    item = input("Digite o nome do item: ")
    valor = float(input(f"Digite o valor do item '{item}': "))#f string possibilita essas mencoes pq meio que viram strings/ palavras
    estoque = int(input(f"Digite o estoque do item '{item}': "))

    # Adiciona as informações nas listas com o append
    mercadorias["item"].append(item)
    mercadorias["valor"].append(valor)
    mercadorias["estoque"].append(estoque)

# Busca os itens
def buscar_item():
    item_busca = input("Digite o nome do item que deseja buscar: ")
    for i in range(len(mercadorias["item"])):
        if mercadorias["item"][i] == item_busca:
            print(f"Item: {mercadorias['item'][i]}, Valor: R${mercadorias['valor'][i]:.2f}, Estoque: {mercadorias['estoque'][i]}")
            break
    else:
        print(f"Item '{item_busca}' não encontrado.")

while True:
    print("[1] Adicionar item")
    print("[2] Buscar item")
    print("[3] Sair")
    opcao = input("Escolha um número de 1 a 3: ")
    
    if opcao == '1':
        adicionar_item()
    elif opcao == '2':
        buscar_item()
    elif opcao == '3':
        print("Tchau")
        break
    else:
        print("Invalido")
        
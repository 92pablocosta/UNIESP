import os

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade disponível: "))
    
    with open("produtos.txt", "a") as arquivo:
        arquivo.write(f"{nome},{preco},{quantidade}\n")

def mostrar_produtos():
    if not os.path.exists("produtos.txt"):
        print("Nenhum produto cadastrado.")
        return
    
    with open("produtos.txt", "r") as arquivo:
        print("Produtos disponíveis em estoque:")
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(",")
            print(f"Nome: {nome}, Preço: R${preco}, Quantidade disponível: {quantidade}")

def adicionar_ao_carrinho():
    if not os.path.exists("produtos.txt"):
        print("Nenhum produto cadastrado.")
        return
    
    carrinho = []
    while True:
        mostrar_produtos()
        escolha = input("Digite o nome do produto que deseja adicionar ao carrinho (ou 'sair' para finalizar): ")
        if escolha.lower() == "sair":
            break
        quantidade = int(input("Digite a quantidade desejada: "))
        carrinho.append((escolha, quantidade))
    
    with open("carrinho.txt", "a") as arquivo_carrinho:
        for item in carrinho:
            arquivo_carrinho.write(f"{item[0]},{item[1]}\n")

def main():
    while True:
        opcao = input("Deseja cadastrar um novo produto (c), mostrar produtos disponíveis (m) ou adicionar ao carrinho (a)? ")
        
        if opcao.lower() == "c":
            cadastrar_produto()
        elif opcao.lower() == "m":
            mostrar_produtos()
        elif opcao.lower() == "a":
            adicionar_ao_carrinho()
        else:
            print("Opção inválida.")
        
        continuar = input("Deseja continuar? (s/n) ")
        if continuar.lower() != "s":
            break

if __name__ == "__main__":
    main()
#importando as funções
from cadastro_cliente import *
from cadastro_vendedor import *


while True:
    # Tela inicial
    print("Bem vindo ao VENDEX, seu app preferido de vendas!")
    
    print('''Selecione uma das opções:

    [1] Login
    [2] Cadastrar
    [3] Sair
          
          ''')

    menu_inicial = input('Selecione a opção: ')
    

    if menu_inicial == '1':
        username = input('Usuário: ')
        password = input("Senha: ")
        login_vendedor(username, password)

    elif menu_inicial == '2':
          
          username = input('Novo nome de usuário: ')
          password = input('Nova senha: ')
          registro_vendedor(username, password)

    elif menu_inicial == '3':
        break

        
    else:
        print('Opção inválida, tente novamente')
    
    
    #Ambiente do vendedor
    print('''O que gostaria de fazer?
          
          
          [1] Cadastrar Cliente
          [2] Buscar/Adicionar Produto
          [3] Carrinho
          [4] Relatório de vendas
          
          ''')
    choice = input('Opção: ')
    
    if choice == '1':
        username = input('Nome de usuário: ')
        password = input('Senha: ')
        registro_cliente(username, password)
    
    elif choice == '2':
        print(''' [1] Adicionar novo produto
              [2] Buscar produto existente''')
        opcao_produto = input('Selecione: ')
        if opcao_produto == '1':
          adicionar_item()
        elif opcao_produto == '2':
            buscar_item()

    elif choice == '3':
        pass

#Escreva um código que exiba um menu para o usuário com duas opções (1 - continuar, 2 -
#sair). Exiba o menu até que o usuário digite 2. Caso o usuário informe outro valor diferente de
#1 e 2, retornar que o valor é inválido.


##########

print('''Olá! Bem vindo ao menu. Selecione uma das duas opções:
      
      1 - Continuar
      
      2 - sair
      ''')


while True:
    selecao = input("Continuar ou sair?")

    if selecao == "1":
        print("Continuar")

    elif selecao == "2":
        print("Saindo")
        break
    
    else:
        print("Opção inválida, tente novamente.")



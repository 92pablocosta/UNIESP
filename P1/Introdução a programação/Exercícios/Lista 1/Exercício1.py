<<<<<<< HEAD
# Lista 1 - Exercício 1

#Escreva um código que mostre um menu para o usuário com as operações matemáticas básicas 
#(soma, subtração, multiplicação e divisão).
#Peça para o usuário escolher uma operação e informar 2 valores. Faça a operação de acordo 
#com a escolha do usuário e exiba o resultado.

#########

op = input("Qual operação deseja realizar?  1 para Soma, 2 para Subtração, 3 para Multiplicação,  4 - Divisão: ")

     
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
subtração = num1 - num2
multiplicação = num1 * num2
divisão = num1 / num2

if op == '1': 
    print ("A soma dos numeros é: ", soma)

elif op == '2': 
    print ("Subtração: ", subtração)

elif op == '3': 
    print ("Multiplicação: ", multiplicação)

elif op == '4': 
    print ("Divisão: ", divisão)

else:
=======
# Lista 1 - Exercício 1

#Escreva um código que mostre um menu para o usuário com as operações matemáticas básicas 
#(soma, subtração, multiplicação e divisão).
#Peça para o usuário escolher uma operação e informar 2 valores. Faça a operação de acordo 
#com a escolha do usuário e exiba o resultado.

#########

op = input("Qual operação deseja realizar?  1 para Soma, 2 para Subtração, 3 para Multiplicação,  4 - Divisão: ")

     
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
subtração = num1 - num2
multiplicação = num1 * num2
divisão = num1 / num2

if op == '1': 
    print ("A soma dos numeros é: ", soma)

elif op == '2': 
    print ("Subtração: ", subtração)

elif op == '3': 
    print ("Multiplicação: ", multiplicação)

elif op == '4': 
    print ("Divisão: ", divisão)

else:
>>>>>>> master
    print("Opção inválida, tente novamente.")
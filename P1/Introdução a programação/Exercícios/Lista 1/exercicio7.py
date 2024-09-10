#Escreva um código que receba um valor inteiro e diga se ele é divisível por cinco.

##

num = int(input("Digite um número para saber se ele é divisível por 5: "))


if num % 5 ==0:
    print("O número",num,"é divisível por 5!")

else:
    print("O número",num,"não é divisível por 5.")
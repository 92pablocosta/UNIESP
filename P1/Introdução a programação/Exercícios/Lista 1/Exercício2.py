<<<<<<< HEAD
#Lista 1 - Exercício 2

#Escreva um código que receba 3 valores inteiro (a, b e c). Utilize
#esses valores para encontrar o valor de delta.
#Caso o valor de delta seja menor que zero, informar que a equação não possui raízes reais.
#Se for maior ou igual a zero, encontre e informe os valores de x1 e x2.
#Para raiz quadrada precisaremos importar a biblioteca “math” e usar o comando math.sqrt().

#####

import math

print("Vamos obter o valor de Delta usando a fórmula de Bhaskara! Para começar, digite os valor de a, b e c.")

a = float(input("Digite o valor de a: "))

b = float(input("Digite o valor de b: "))

c = float(input("Digite o valor de c: "))

delta = (b**2) - (4*a*c)

if a == 0:
    print ("Valor de a deve ser diferente de 0.")

elif a < 0:
    print ("Equação não possue raizes reais.")

else:
=======
#Lista 1 - Exercício 2

#Escreva um código que receba 3 valores inteiro (a, b e c). Utilize
#esses valores para encontrar o valor de delta.
#Caso o valor de delta seja menor que zero, informar que a equação não possui raízes reais.
#Se for maior ou igual a zero, encontre e informe os valores de x1 e x2.
#Para raiz quadrada precisaremos importar a biblioteca “math” e usar o comando math.sqrt().

#####

import math

print("Vamos obter o valor de Delta usando a fórmula de Bhaskara! Para começar, digite os valor de a, b e c.")

a = float(input("Digite o valor de a: "))

b = float(input("Digite o valor de b: "))

c = float(input("Digite o valor de c: "))

delta = (b**2) - (4*a*c)

if a == 0:
    print ("Valor de a deve ser diferente de 0.")

elif a < 0:
    print ("Equação não possue raizes reais.")

else:
>>>>>>> master
    print ("O valor de Delta é igual à: ", delta)
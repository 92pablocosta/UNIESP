# Lista 1 - Exercício 4

# Escreva um código que receba o valor do raio de uma circunferência e retorne a área desta
#circunferência.

#####

print("Digite o valor do Raio para calcularmos a área da circunferência.")
raio = int (input("Valor de r: "))

import math

C = 2 * math.pi * raio

print("O valor da área da circunferência é: ", C)
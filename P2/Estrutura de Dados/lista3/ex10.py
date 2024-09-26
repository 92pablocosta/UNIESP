# Escreva um programa que cria uma lista de números inteiros e remove todos os números repetidos,
# exibindo a lista resultante.

from random import randint

lista = [4, 2, 3, 2, 9, 7, 0, 12, 4, 8, 10, 10, 11, 11, 13, 3, 14, 8, 14, 3, 15, 12, 5, 12, 2, 12, 5, 9, 4, 6]
lista2 = []

for numero in lista:
    if numero not in lista2:
        lista2.append(numero)
lista2.sort()
lista.sort()
print(f'Lista original: {lista}')
print(f'Lista sem numeros repetidos: {lista2}')

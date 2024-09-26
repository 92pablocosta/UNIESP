# Escreva um programa que cria uma lista de números inteiros e exibe os números ímpares da lista.

from random import randint

lista = []
lista_impares = []

for i in range(10):
    n = randint(1, 50)
    if n % 2 != 0:
        lista_impares.append(n)
    lista.append(n)
print(f'Lista criada: {lista}')
print(f'Lista ìmpares: {lista_impares}')

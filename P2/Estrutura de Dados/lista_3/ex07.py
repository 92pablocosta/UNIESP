# Escreva um programa que cria uma lista de números inteiros e exibe os números pares da lista.

from random import randint
lista = []
numeros_pares = []
for i in range(10):
    n = randint(1, 50)
    if n % 2 == 0:
        numeros_pares.append(n)
    lista.append(n)
print(f'Lista criada: {lista}')
print(f'Números pares da lista: {numeros_pares}')

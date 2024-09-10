# Escreva um programa que cria uma lista de números inteiros e exibe o maior número da lista.

from random import randint
lista = []
for i in range(5):
    n = randint(0, 50)
    lista.append(n)

print(f'O maior número da lista é {max(lista)}')

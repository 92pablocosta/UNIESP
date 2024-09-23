# Escreva um programa que cria uma lista de números inteiros e exibe a soma de todos os números da lista.

from random import randint

lista = []

elementos = int(input("Quantos números gostaria de adicionar à lista?: "))

for i in range(elementos):
    n = randint(1, 50)
    lista.append(n)

print(f'Lista criada: {lista}')
print(f'Soma dos elementos da lista: {sum(lista)}')

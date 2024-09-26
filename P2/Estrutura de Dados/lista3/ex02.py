# Escreva um programa que cria uma lista de nomes e exibe o número total de nomes na lista.

from random import randint
lista_nomes = []
n = int(input('Quantos nomes gostaria de adicionar?: >'))

for i in range(n):
    nome = input("Digite um nome: ")
    lista_nomes.append(nome)
print(f'A lista digitada foi {lista_nomes}')
print(f'A lista contém {len(lista_nomes)} nomes.')

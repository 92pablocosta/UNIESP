# Escreva um programa que cria uma lista de números inteiros e exibe a média dos números da lista.

from random import randint

lista = []

while True:
    elementos = int(input('Quantos números gostaria de adicionar à lista? (Max. 15): '))
    if elementos > 15:
        print('Essa quantidade excede o número máximo de elementos na lista, tente novamente.')
    else:
        break

for i in range(elementos):
    n = randint(1, 50)
    lista.append(n)

media = sum(lista) / len(lista)

print(f'A lista criada foi: {lista}')
for j in range(len(lista)):
    if j == (elementos - 1):
        print(f'{lista[-1]} = {sum(lista)}')
    else:
        print(f'{lista[j]} + ', end='')

print(f'{sum(lista)} / {len(lista)} = {media:.2f}')
print(f'A média dos elementos da lista é: {media:.2f}')

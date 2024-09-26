# Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado 
# sem usar a função `max()`. 
# Em seguida, encontre o elemento mínimo sem usar a função `min()`.

lista = [45, 17, 36, 61, 82, 45, 87, 14, 58, 76, 94, 65, 75, 39, 73]
maior_elemento = 0
for numero in lista:
    if numero > maior_elemento:
        maior_elemento = numero
print(f'O maior número encontrado na lista foi {maior_elemento}')

# Escreva um programa que cria duas listas de números inteiros e exibe os números que estão presentes
# em ambas as listas.

lista1 = [20, 7, 6, 43, 32, 30, 23, 36, 28, 4]
lista2 = [41, 43, 4, 17, 44, 31, 2, 14, 20, 33]
numeros_iguais = []

for i in range(len(lista1)):
    n = lista1[i]
    for j in range(len(lista2)):
        if lista2[j] == n:
            numeros_iguais.append(n)

numeros_iguais.sort()
print(f'Números repetidos nas listas: {numeros_iguais}')

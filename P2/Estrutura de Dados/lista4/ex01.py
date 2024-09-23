# Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o
# algoritmo de seleção.

lista = [3, 1, 9, 8, 0, 5, 2, 8, 6, 0, 5, 1, 2, 8, 1]
print(lista)
n = len(lista)
for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            aux = lista[j]
            lista[j] = lista [j + 1]
            lista[j + 1] = aux
print(lista)

# Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro que
# serve como chave para realizar a ordenação crescente ou decrescente.

lista = [3, 1, 9, 8, 0, 5, 2, 8, 6, 0, 5, 1, 2, 8, 1]
n = len(lista)

print(f'A lista inserida é: {lista}')

opcao = int(input('Gostaria de mostrar a lista em ordem [1] crescente ou [2] decrescente:?'))

if opcao == 1:

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista [j + 1]
                lista[j + 1] = aux
    print(f'Lista em ordem CRESCENTE: {lista}')

elif opcao == 2:
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j] + 1:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    print('Lista em ordem DECRESCENTE: {lista}')
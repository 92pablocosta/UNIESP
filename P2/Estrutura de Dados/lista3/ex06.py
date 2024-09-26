# Escreva um programa que cria uma lista de strings e exibe a mais longa palavra da lista.
lista = ['maça', 'banana', 'grama', 'verde', 'otorrinolanringologista']
maior_palavra = max(lista, key=len).capitalize()
print(f'A lista de palavras digitadas é: {lista}')
print(f'A maior palavra da lista é: {maior_palavra}')

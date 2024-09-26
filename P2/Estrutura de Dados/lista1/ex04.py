# Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.

maior = menor = 0
c = 0
while True:
    n = int(input('Digite um número (0 para sair): '))
    if n == 0:
        break
    c += 1
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'Maior: {maior} - Menor {menor}')

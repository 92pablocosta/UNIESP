# Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até
# esse número.

pares = []
contador = 0

while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    if n % 2 == 0:
        pares.append(n)
        contador += 1
print(f'Você digitou {contador} números pares, sendo eles: {pares}')

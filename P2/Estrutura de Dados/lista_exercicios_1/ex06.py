# Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse
# número.

n = int(input('Digite um número para calcular o seu fatorial: '))
fatorial = 1
for c in range(1, n + 1):
    fatorial = fatorial * c
print(fatorial)

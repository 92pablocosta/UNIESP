# Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

n = int(input('Digite até que valor você quer ver a Sequência de Fibonacci: '))
f1 = 0
f2 = 1
print(f'Fibonacci: {f1}, {f2}', end='')
while True:
    termo = f1 + f2
    if termo > n:
        break
    print(f', {termo}', end='')
    f1 = f2
    f2 = termo

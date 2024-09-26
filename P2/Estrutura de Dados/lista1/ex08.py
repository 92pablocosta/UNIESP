# Faça um programa que determine se um número é primo ou não.

while True:
    n = int(input('Digite um número para saber se ele é Primo: '))
    if n == 0:
        break
    
    if n < 2:
        print(f'O número {n} NÃO É PRIMO.')
    elif n == 2 or n == 3:
        print(f'O número {n} É PRIMO.')
    elif n > 3:
        if n % 2 == 0 or n % 3 == 0:
            print(f'O número {n} NÃO É PRIMO.')
        else:
            print('O número É PRIMO')

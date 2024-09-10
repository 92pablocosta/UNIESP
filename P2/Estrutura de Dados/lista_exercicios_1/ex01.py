# Faça um programa que calcule a média de três números inseridos pelo usuário.

while True:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    n3 = int(input('Digite mais um: '))
    media = (n1 + n2 + n3) / 3

    print(f'VOcÊ digitou {n1}, {n2} e {n3}. A média é de {media:.2f}')

    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao != 'S':
        break
print('FIM DO PROGRAMA.')

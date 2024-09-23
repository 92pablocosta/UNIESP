# Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que
# começam com a letra 'A'.

nomes_a = []
while True:
    nome = input('Digite um nome (ou "sair" para encerrar): ').strip().lower()
    if nome == 'sair':
        break

    if nome[0] == 'a':
        nomes_a.append(nome)
print(f"Nomes com a letra 'A': {nomes_a}")

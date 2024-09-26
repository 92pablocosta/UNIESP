# Faça um programa que leia uma lista de números e retorne a média dos números pares.

lista = [1, 2, 4, 5, 8, 18, 20]
lista_pares = []
soma_pares = 0
for p in lista:
    if p % 2 == 0:
        soma_pares += p
        lista_pares.append(p)
print(f'Os valores pares da lista são: {lista_pares}')
print(f'A media dos valores digitados é {(soma_pares / len(lista_pares))}')

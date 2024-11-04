horas_sono = [[8, 6, 7, 8, 6],
              [5, 5, 6, 7, 8],
              [6, 7, 8, 6, 5],
              [7, 5, 9, 7, 4]]

soma_horas_sono = []
cont = 0

for i in range(len(horas_sono)):
    soma = 0
    for numero in horas_sono[i][cont]:
        soma += numero
        cont += 1
    soma_horas_sono.append(soma)

print(soma_horas_sono)

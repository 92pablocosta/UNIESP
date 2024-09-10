# Obtenha dados da altura e o gênero (Masculino ou Feminino) de 15 pessoas e apresente os seguintes resultados:
# - A maior e a menor altura do grupo;
# - A média de altura das pessoas do gênero Masculino;
# - O número de pessoas do gênero Feminino.

contador = maior_altura = menor_altura = mulheres = homens = 0
altura_total = 0

for i in range(0, 15):
    
    altura = float(input('Digite a sua altura: '))
    genero = input('Digite o seu gênero. [M/F]: ').strip().upper()[0]
    contador += 1
    if contador == 1:
        maior_altura = altura
        menor_altura = altura
        if genero == 'M':
            homens += 1
            altura_total += altura
        elif genero == 'F':
            mulheres += 1

    elif genero == 'M':
        homens += 1
        altura_total += altura
        if altura > maior_altura:
            maior_altura = altura
        elif altura < menor_altura:
            menor_altura = altura

    elif genero == 'F':
        mulheres += 1
        if altura > maior_altura:
            maior_altura = altura
        elif altura < menor_altura:
            menor_altura = altura
    
    if i < 15:
        print('Dados registrados com sucesso!\n')

print(f'A pessoa mais alta do grupo tem {maior_altura}m e a mais baixa tem {menor_altura}m')
print(f'A média de altura das pessoas do sexo masculino é de {(altura_total / homens):.2f}m.')
print(f'O grupo tem {mulheres} pessoas do sexo feminino.')

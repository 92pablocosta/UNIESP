# Escreva um programa que cria uma lista de palavras e exibe a quantidade de palavras que começam
# com a letra 'A'.

lista = []
palavras_a = 0
elementos = int(input("Quantas palavras gostaria de adicionar à lista? (Max. 15): "))
for i in range(elementos):
    palavra = input('Digite uma palavra: ').strip()
    lista.append(palavra)
    if palavra[0] in 'aA':
        palavras_a += 1
print(f'A lista de palavras digitadas foi: {lista}')
if palavras_a == 0:
    print('Não houveram palavras que começam com a letra A.')
elif palavras_a == 1:
    print(f'Apenas 1 palavra começa com a letra "A".')
else:
    print(f'{palavras_a} palavras começam com a letra A.')

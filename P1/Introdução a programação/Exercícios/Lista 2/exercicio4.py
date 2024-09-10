#Escreva um código que receba 6 valores do usuário, exiba a sua soma e a sua média. Fazer
#usando laços de repetição.


##########

soma = 0
contagem = 6

for i in range(contagem):
    valor = float(input(f"Digite o {i+1}º valor: "))
    soma += valor

media = soma / contagem

print(f"A soma dos valores é: {soma}")
print(f"A média dos valores é: {media}")


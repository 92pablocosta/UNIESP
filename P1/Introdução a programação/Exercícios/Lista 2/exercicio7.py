#Escreva um código que escreva a sequência Fibonacci até o valor informado pelo usuário.
#Ex.: Caso o usuário informe o valor 100, o resultado será:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

######


valor_final = int(input("Digite o número máximo da sequencia de Fibonacci: "))

a, b = 0, 1

resultado = a + b

fibo = resultado 

for i in range(valor_final):
    print(f"A sequência de fibonacci até o valor {valor_final} é")

#Escreva um código que receba um valor inteiro de 0 a 10. Exiba a tabuada de 0 a 10 do valor
#informado.

##########

tabuada = 11

while True:

    valor = int(input("Digite um valor de 0 a 10: "))

    if 0 <= valor <= 10:
        break
    else:
        print("O valor digitado é inválido, tente novamente.")

for i in range(tabuada):
    resultado = valor * i
    print(f"{valor} x {i} = {resultado}")


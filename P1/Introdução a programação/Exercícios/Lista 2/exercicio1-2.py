#Escreva um código que receba 2 valores do tipo inteiro, faça sua soma e informe se o
#resultado é par ou ímpar.

########### versão 2.0

def verificar_par_impar(soma):
    if soma % 2 == 0:
        return "par"
    else:
        return "ímpar"

def main():
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))

    soma = valor1 + valor2

    resultado = verificar_par_impar(soma)

    print(f"A soma dos valores é {soma} e o resultado é {resultado}.")

if __name__ == "__main__":
    main()

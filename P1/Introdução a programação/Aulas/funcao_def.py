horas = int(input("Horas trabalhadas pelo funcionário: "))

def calculaHoras(horas):
    if horas >40:
        extra = (horas - 40)
        horas_extras = ((extra * 33.30) * 1.25)
        horas_normais = ((horas - extra) * 33.30)
        total = (horas_normais + horas_extras)
        print("O valor a ser pago ao funcionário é de R$",total)

    else:
        horas_trabalhadas = (horas * 33.30)
        print(horas_trabalhadas)

calculaHoras (41)

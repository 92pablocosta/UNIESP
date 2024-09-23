# Lista 1 - Exercício 3

# Escreva um código que receba a sua idade e retorne o ano do seu nascimento

##############

from datetime import datetime

data_inicial = datetime.strptime('17/04/1992', '%d/%m/%Y').date()
data_final = datetime.strptime('04/04/2024', '%d/%m/%Y').date()
diferenca_entre_datas = data_final - data_inicial
mutiplicacao_data_valor = diferenca_entre_datas * 5.5
print(type(mutiplicacao_data_valor))
print(mutiplicacao_data_valor)


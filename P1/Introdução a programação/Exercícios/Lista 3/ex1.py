<<<<<<< HEAD
import funcoes

produto = input("Nome do produto: ")
valor = float(input("Valor: "))
peso = float(input("Peso: "))

valor_total = funcoes.compra(valor, peso)

print("Nome do produto: ", produto)
print("Valor do produto convertido: ", valor_total[0])
print("Valor do frente convertido: ", valor_total[1])
=======
import funcoes

produto = input("Nome do produto: ")
valor = float(input("Valor: "))
peso = float(input("Peso: "))

valor_total = funcoes.compra(valor, peso)

print("Nome do produto: ", produto)
print("Valor do produto convertido: ", valor_total[0])
print("Valor do frente convertido: ", valor_total[1])
>>>>>>> master
print("Valor total: ", valor_total[0], valor_total[1])
#Escreva uma lista com valores 1000, 1500, 1250 e 2500. Crie uma função que aplique 10% de imposto em cima do valor. Retorne uma lista com os novos valores

#Versão ChatGPT
def aplicar_imposto(valores):
    valores_com_imposto = []
    for valor in valores:
        novo_valor = valor * 1.1  # Subtrai 10% do valor total
        valores_com_imposto.append(novo_valor)
    return valores_com_imposto

# Lista de valores inicial
valores = [1000, 1500, 1250, 2500]

# Aplicar imposto aos valores
valores_com_imposto = aplicar_imposto(valores)

# Imprimir os novos valores
print("Valores com imposto aplicado:", valores_com_imposto)

#Versão sala de aula

valores = [1000, 1500, 1250, 2500]

def adicionar_imposto(valor):
    return valor * 1.1

valor_com_imposto = []
for valor in valores:
    valor_com_imposto.append(adicionar_imposto(valor))

print(valor_com_imposto)
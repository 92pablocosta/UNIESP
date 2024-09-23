#ex16-05

#Criar lista vazia

valores = []

for i in range(5):
    valor_usuario = int(input("Informe o valor: "))
    valores.append(valor_usuario)

def quadrado(valor):
    return valor * valor

lista_quadrado = list(map(quadrado, valores))

#ou

resultado = list(lista_quadrado)

print(lista_quadrado)

#Função MAP

#sintaxe: map(funcao, iteravel)

#codigo sem map

#Criar lista
valores = {1000, 1500, 1250, 2500}
#Criar função
def adicionar_imposto(valor):
    return valor * 1.1

#Com map

valor_com_imposto = list(map(adicionar_imposto, valores))

print(valor_com_imposto)

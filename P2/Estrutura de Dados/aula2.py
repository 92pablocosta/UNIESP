# Seu código aqui.
def ex1():
    vendas = [120, 85, 300, 45, 210, 95]
    limite = 100

    for produto in vendas:
        if produto < limite:
            vendas.remove(produto)
    print(min(vendas))

def ex2():
    loc = [150, 200, 250, 180, 220, 175]
    media = sum(loc) / len(loc)
    
    for linhas in loc:
        
        if linhas > media:
            loc.remove(linhas)
    
    print(f'A média de linhas de todos os programadores é {media:.2f}')
    print(f'{len(loc)} programadores fizeram acima da média de linhas.')
    print(f'O programador com mais linhas de código fez {max(loc)} linhas.')

ex2()
# A média de linhas de código escritas é de 195.83.
# Sua tarefa é encontrar o desenvolvedor com o maior número de linhas de código acima da média.
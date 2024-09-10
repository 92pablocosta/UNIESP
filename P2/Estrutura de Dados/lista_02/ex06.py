# Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
# método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def calcular_total(self):
        total = self.preco * self.quantidade
        return total
produto = Produto('Picolé', 3.99, 5)
print(f'Você comprou {produto.quantidade} unidades de {produto.nome}')
print(f'O valor total é de R${produto.calcular_total():.2f}')

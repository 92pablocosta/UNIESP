import numpy as np

class fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=object)

    def fila_vazia(self):
        return self.numero_elementos == 0

    def fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.fila_cheia():
            print('A fila está cheia')
            return
        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.fila_vazia():
            print('A fila já está vazia')
            return
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        else:
            self.numero_elementos -= 1
            return temp

    def primeiro(self):
        if self.fila_vazia():
            return -1
        else:
            return self.valores[self.inicio]

    def visualizar(self):
            if not self.fila_vazia():
                print("Itens da Fila:")
                for i in range(self.numero_elementos):
                  print(self.valores[i],end=' ')
            else:
                print("A pilha está vazia. Não há itens para visualizar.")

# Vamos simular um sistema de gerenciamento de pedidos para um restaurante.
# Os pedidos dos clientes são colocados em uma fila e processados na ordem em que foram feitos e
# de acordo com a cozinha. O primeiro dígido do código irá direcionar para a cozinha especializada
# Código 1 - Cozinha A, Código 2 - Cozinha B e Código 3 - Cozinha C.
# Use a classe de fila para gerenciar os pedidos e processá-los na ordem correta.

# Situação 1
# pedidos = ['1256','1856','2856','3452','2352','1878','3876']

# Responda as questões:
# Quantos pedidos estão pendentes nas Cozinhas A, B e C?
# Quais os próximos pedidos para cada cozinha?
# Quem são os últimos pedidos das cozinhas A, B e C?

# Situação 2
# pedidos = ['1256','1856','2856','3452','2352','1878','3876']

# Responda as questões:
# Quantos pedidos estão pendentes nas Cozinhas A, B e C?
# Quais os próximos pedidos para cada cozinha?
# Quem são os últimos pedidos das cozinhas A, B e C?

# A Cozinha B atendeu a 1 pedido, a Cozinha A atendeu dois pedidos.
# Responda novamente as questões:

# Quantos pedidos estão pendentes nas Cozinhas A, B e C?
# Quais os próximos pedidos para cada cozinha?
# Quem são os últimos pedidos das cozinhas A, B e C?

pedidos = ['1256','1856','2856','3452','2352','1878','3876']
cozinha_a = []
cozinha_b = []
cozinha_c = []

print(pedidos[0][0])
import numpy as np

class Listasequencial:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(self.valores[i], end=', ')

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if (valor==self.valores[i]):
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
        self.ultima_posicao -= 1

    def tamanho(self):
      return self.capacidade

    def maior_valor(self):
      pass

    def menor_valor(self):
      pass

    def valor_repetido(self):
      pass

    def organiza_lista(self):
      pass


    # Criando novos métodos para o objeto Listasequencial:

    # 1. Retornar o maior valor.
    # 2. Retornar o menor valor.
    # 3. Verificar se um valor se repete.
    # 4. Retornar quais os valores são pao maior valor.
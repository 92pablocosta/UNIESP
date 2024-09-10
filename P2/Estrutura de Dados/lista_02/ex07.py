# Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método
# chamado “detalhes” que retorna uma string com as informações do carro.
from time import sleep
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def detalhes(self):
        return f'Marca: {self.marca} Modelo: {self.modelo} Ano: {self.ano}'
    def acelerar(self):
        opcao = input('Gostaria de acelerar o carro? [s/n]\n>>').strip().upper()[0]
        if opcao == 'S':
            sleep(2)
            print('\nVRUUUUUUUUUUUUMMMMMMMMMMMMMM')
        else:
            print('\nVocê é chato, vou acelerar mesmo assim.\n')
            print('VRRRRRUUUUUUUMMMMMMMM RANDANDANDANDNADNAND\n')

corolla = Carro('Toyota', 'Corolla', 2021)
bmw = Carro('BMW', 'IX M60', 2024)
opcao = int(input('Gostaria de ver as informações de que carro? [1] Corolla [2] BMW: '))

if opcao == 1:
    print(corolla.detalhes())
elif opcao == 2:
    print(bmw.detalhes())
    sleep(2)
    bmw.acelerar()
else:
    print('Opção inválida. Tente novamente')

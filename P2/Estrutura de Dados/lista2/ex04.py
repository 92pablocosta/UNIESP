# Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente
# métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    def depositar(self):
        deposito = int(input('Quanto gostaria de depositar? R$'))
        novo_saldo = self.saldo + deposito
        print(f'O seu novo saldo é de {novo_saldo}')
    def sacar(self):
        saque = int(input(f'Olá {self.titular}!Quanto gostaria de sacar? R$'))
        novo_saldo = self.saldo - saque
        if novo_saldo < 0:
            print('Saldo indisponível, tente novamente.')
        else:
            print(f'Você sacou R${saque}. Seu novo saldo é de R${novo_saldo}')

while True:
    print('Olá! Bem vindo ao nosso Banco!')
    opcao = int(input('''O que gostaria de fazer hoje?
                      
                    [1] Saque
                    [2] Depósito
                    [3] Sair\nDigite sua opção: '''))
    if opcao == 1:
        conta = ContaBancaria(1000, 'Pablo')
        saque = conta.sacar()
        print(saque)
    elif opcao == 2:
        deposito = conta.depositar()
        print(deposito)
    elif opcao == 3:
        print('Obrigado pela preferência, volte sempre!')
        break
    else:
        print('Opção inválida, tente novamente.')

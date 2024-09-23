# Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um
# método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário
# do funcionário.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    def aumentar_salario_inflacao(self):
        inflacao = 1.1
        return self.salario * inflacao
funcionario = Funcionario('Pablo Costa', 19000, 'CEO')
print(f'O novo salário do funcionário {funcionario.nome} é de R${funcionario.aumentar_salario_inflacao()}')

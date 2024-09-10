# Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado
# “calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    def aluno_aprovado(self):
        if aluno.calcular_media() >= 7:
            print('O aluno está APROVADO.')
        elif aluno.calcular_media() < 4:
            print('O aluno está REPROVADO')
        else:
            print('O aluno tera que fazer PROVA FINAL.')
aluno = Aluno('Pablo', 4, 3)
print(f'A média do aluno {aluno.nome} é: {aluno.calcular_media()}')
aluno.aluno_aprovado()

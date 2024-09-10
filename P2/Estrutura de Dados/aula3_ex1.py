class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def calcular_media_aluno(self):
        self.media = float((self.nota1 + self.nota2) / 2)
        return self.calcular_media_aluno
    
    def mostra_resultados(self):
        print(f'Nome: {self.nome}')
        print(f'Nota 1: {self.nota1}')
        print(f'Nota 2: {self.nota2}')
        print(f'Média: {self.media}')



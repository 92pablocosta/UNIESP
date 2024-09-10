# Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. 
# Implemente um método chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def detalhes(self):
        return f'O Autor do livre {self.titulo} é {self.autor}.'
    
livro = Livro("'O vento Levou'", 'Margaret Mitchell')
info = livro.detalhes()
print(info)

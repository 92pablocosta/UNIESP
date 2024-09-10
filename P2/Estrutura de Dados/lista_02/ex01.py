# Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado
# “calcular_area” que retorna a área do círculo.


class Circulo: # Cria a classe
    
    def __init__(self, raio): # Construtor / Passagem de atributos
        self.raio = raio
    
    def calcular_area(self): # Método para calcular a área.
        pi = 3.14
        return pi * (self.raio ** 2)
    
circulo = Circulo(5) # Instanciando
area = circulo.calcular_area() # variavel 'area' recebe a instáncia + o método
print(area) 

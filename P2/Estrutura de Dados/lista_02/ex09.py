# Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um
# método chamado “calcular_perimetro” que retorna o perímetro do triângulo.

class Triangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    def calcular_area(self):
        return (self.base * self.altura) / 2
triangulo = Triangulo(10, 8)
print(f'A área do triângulo é {triangulo.calcular_area()}m²')

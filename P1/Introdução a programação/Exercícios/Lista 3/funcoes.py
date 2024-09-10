def compra(valor, peso):
    
    valor_convertido = (valor * 5.09)
    valor_peso = ((peso * 0.0199) * 5.09)
    return [valor_convertido, valor_peso]

#codigo gambiarra
def letra_numerog(letra):
    numero = ord(letra) - 96

def letra(letra):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h"]
    valor = (alfabeto.index(letra))
    return valor

def parouimpar(valor):
    if valor %2 ==0:
        for i in range(2, valor, 2):
            print(i)
        print("O valor é par")
    else:
            for i in range(1, valor, 2):
                print(i)
            print("O valor é impar.")
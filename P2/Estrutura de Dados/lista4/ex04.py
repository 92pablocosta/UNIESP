# Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número.
# Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.
def segundo_maior(lista):
    maior_numero = 0
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
            lista.remove(numero)
            lista.append(maior_numero)
    lista.pop()
    for num in lista:
        if num > maior_numero:
            maior_numero = num
            lista.remove(num)
            lista.append(maior_numero)
    return lista[-1]


lista = [45, 17, 36, 61, 82, 45, 88, 14, 58, 14, 94, 65, 75, 39, 73]
print(f'O segundo maior número na lista é {segundo_maior(lista)}.')

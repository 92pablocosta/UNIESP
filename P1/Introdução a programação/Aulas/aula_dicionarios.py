#Crie um dicionário chamado Alunos com os campos matrícula, nome, idade, sexo, curso

##############

alunos = {
    2024001: {'nome': 'Joãozinho', 'idade': 22, 'sexo': 'M', 'curso': 'SI'},
    2024002:{'nome': 'Toinho', 'idade': 40, 'sexo': 'M', 'curso': 'SI'},
    2024003:{'nome': 'Pedrinho', 'idade': 31, 'sexo': 'M', 'curso': 'SI'},
    2024004:{'nome': 'Zezinho', 'idade': 19, 'sexo': 'M', 'curso': 'SI'},
    2024005:{'nome': 'Mariazinha', 'idade': 33, 'sexo': 'F', 'curso': 'SI'}
}

#Modificar uma entrada
alunos[2024001]['Joãozinho'] = 'Coisinha'

#adicionar novo aluno
alunos.update({2024006: {'nome': 'kaka', 'idade': 22, 'sexo': 'M', 'curso': 'SI'}})
print(alunos)

novo = {
    2024008: {'nome': 'Dave', 'idade': 25, 'sexo': 'M', 'curso': 'SI'},
}

#apagando linha completa
alunos.pop(2024008)
#apaga o ultimo registro
alunos.popitem()
#apagando uma biblioteca completa
alunos.clear()

del alunos[2024005]['nome']

print(alunos)

for chave, valor in alunos.items():
    print(f"{2024003}: {'idade'}")
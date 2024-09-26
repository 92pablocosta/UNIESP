<<<<<<< HEAD
#pratica_slide3

#Escreva um código que possua 3 variáveis que recebam valores reais com
#uma casa decimal após a virgula, positivos e menores ou iguais a 10, faça
#a média dos três valores e, caso a média seja maior ou igual a 7,
#informar que o aluno está aprovado. Caso seja menor que 7 e maior ou
#igual a 4, informar que o aluno fará a prova final e, caso a nota seja
#menor que 4, informar que o aluno está reprovado.

###########

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 9:
    print("PARABÉNS! Você foi aprovado com uma média excelente!")
    print("Status: Aprovado. Média: ", media)

elif media >= 7:
    print("Você foi aprovado!")
    print("Média:", media)

elif media >= 4:
    print("Você não atingiu a média de aprovação e precisará fazer a prva final.")
    print("Status: Prova final. Média: ", media)

elif media < 4:
    print("Reprovado.")

=======
#pratica_slide3

#Escreva um código que possua 3 variáveis que recebam valores reais com
#uma casa decimal após a virgula, positivos e menores ou iguais a 10, faça
#a média dos três valores e, caso a média seja maior ou igual a 7,
#informar que o aluno está aprovado. Caso seja menor que 7 e maior ou
#igual a 4, informar que o aluno fará a prova final e, caso a nota seja
#menor que 4, informar que o aluno está reprovado.

###########

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 9:
    print("PARABÉNS! Você foi aprovado com uma média excelente!")
    print("Status: Aprovado. Média: ", media)

elif media >= 7:
    print("Você foi aprovado!")
    print("Média:", media)

elif media >= 4:
    print("Você não atingiu a média de aprovação e precisará fazer a prva final.")
    print("Status: Prova final. Média: ", media)

elif media < 4:
    print("Reprovado.")

>>>>>>> master

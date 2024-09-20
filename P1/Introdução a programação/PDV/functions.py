from datetime import datetime

#funções de exemplo
def salvar_historico(operacao, num1, num2, resultado):
    pass
    with open("historico_calculadora.txt", "a") as file:
        file.write(f"{datetime.now()} - {operacao} - {num1} e {num2} = {resultado}\n")


#funções que serão usadas



def historico_vendas(vendedor, cliente, checkout, relatorio): #Criação do arquivo de texto com todas as vendas realizadas.
    with open("registro_de_vendas.txt", "a") as file:
        file.write(f"{dt.now()} - {vendedor} - {cliente} - {checkout} - {relatorio}\n")


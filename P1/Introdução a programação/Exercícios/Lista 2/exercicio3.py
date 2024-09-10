#/Escreva um código que receba um valor de login e um valor de senha. Caso os valores
#estejam corretos, retornar ao usuário: “Você está logado”. Caso contrário, informar: “Login ou
#senha incorretos”.
#Defina um valor padrão para login e senha.

############

while True:

    user = "pablo"
    password = "123"
   
    input_user = input("Digite seu nome de usuário: ")
    
    input_password = input("Digite sua senha: ")

    if input_user == user and input_password == password:
        print("Você está logado.")
        break

    else:
        print("Senha ou login inválidos. Tente novamente.")

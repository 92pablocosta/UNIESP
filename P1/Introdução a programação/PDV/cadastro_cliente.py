
def registro_cliente(username, password):
    cliente = load_users()
    
    if username in cliente:
        print("Usuário já existe!")
    
    with open('cliente.txt', 'a') as file:
        file.write(f"{username},{password}\n")
    
    print("Usuário registrado com sucesso!")

def login_user(username, password):
    users = load_users()

    if username not in users:
        print("Usuário não encontrado!")
    
    if users[username] == password:
        print(f"Login bem-sucedido. Bem vindo {username}!")
    else:
        print("Senha incorreta!")

def load_users():

    users = {}
    
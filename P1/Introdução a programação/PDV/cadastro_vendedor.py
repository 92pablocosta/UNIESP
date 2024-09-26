<<<<<<< HEAD
def registro_vendedor(username, password):
    vendedor = load_users()
    
    if username in vendedor:
        print("Usuário já existe!")
    
    with open('vendedor.txt', 'a') as file:
        file.write(f"{username},{password}\n")
    
    print("Usuário registrado com sucesso!")

def login_vendedor(username, password):
    vendedor = load_users()
    
    if username not in vendedor:
        print("ERRO: Usuário não encontrado, tente novamente")
    
    if vendedor[username] == password:
        print(f"Login bem-sucedido. Bem vindo {username}!")
        
    else:
        print("Senha incorreta!")
        
    

def load_users():
    vendedor = {}
    try:
        with open('vendedor.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                vendedor[username] = password
    except FileNotFoundError:
        # O arquivo não existe ainda, retornamos um dicionário vazio
        pass
    
    return vendedor


    main()
=======
def registro_vendedor(username, password):
    vendedor = load_users()
    
    if username in vendedor:
        print("Usuário já existe!")
    
    with open('vendedor.txt', 'a') as file:
        file.write(f"{username},{password}\n")
    
    print("Usuário registrado com sucesso!")

def login_vendedor(username, password):
    vendedor = load_users()
    
    if username not in vendedor:
        print("ERRO: Usuário não encontrado, tente novamente")
    
    if vendedor[username] == password:
        print(f"Login bem-sucedido. Bem vindo {username}!")
        
    else:
        print("Senha incorreta!")
        
    

def load_users():
    vendedor = {}
    try:
        with open('vendedor.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                vendedor[username] = password
    except FileNotFoundError:
        # O arquivo não existe ainda, retornamos um dicionário vazio
        pass
    
    return vendedor


    main()
>>>>>>> master

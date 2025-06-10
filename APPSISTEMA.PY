def sistema_login():
    usuario_cadastrado = "admin"
    senha_cadastrada = "1234"

    print("Sistema de Login")

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

sistema_login()

def cadastro():
    usuarios = []

    while True:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        email = input("Email: ")

        usuario = {"nome": nome, "idade": idade, "email": email}
        usuarios.append(usuario)

        continuar = input("Deseja cadastrar outro? (s/n): ").lower()
        if continuar != "s":
            break

    print("\nUsuários cadastrados:")
    for u in usuarios:
        print(f"Nome: {u['nome']} - Idade: {u['idade']} - Email: {u['email']}")

cadastro()

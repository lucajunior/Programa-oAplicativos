def calculadora():
    print("Calculadora Simples")
    n1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    n2 = float(input("Digite o segundo número: "))

    if operador == "+":
        resultado = n1 + n2
    elif operador == "-":
        resultado = n1 - n2
    elif operador == "*":
        resultado = n1 * n2
    elif operador == "/":
        if n2 != 0:
            resultado = n1 / n2
        else:
            print("Erro: divisão por zero.")
            return
    else:
        print("Operador inválido.")
        return

    print(f"Resultado: {resultado}")

calculadora()

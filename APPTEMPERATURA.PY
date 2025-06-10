def conversor_temperatura():
    print("Conversor de Temperatura")
    temp = float(input("Digite a temperatura: "))
    escala = input("Converter para (C)elsius ou (F)ahrenheit? ").upper()

    if escala == "C":
        resultado = (temp - 32) * 5/9
        print(f"{temp}°F = {resultado:.2f}°C")
    elif escala == "F":
        resultado = (temp * 9/5) + 32
        print(f"{temp}°C = {resultado:.2f}°F")
    else:
        print("Opção inválida.")

conversor_temperatura()

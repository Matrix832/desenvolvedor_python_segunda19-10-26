nome = input("Informe seu nome: ").strip().title()
massa = float(input("Informe sua massa em kg: ").replace(",", "."))
altura = float(input("Informe sua altura em metros: ").replace(",", "."))

# Calcula o IMC
imc = massa / (altura ** 2)

print(f"{nome}, seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está no peso normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
elif imc < 35:
    print("Você está com obesidade grau 1.")
elif imc < 40:
    print("Você está com obesidade grau 2.")
else:
    print("Você está com obesidade grau 3.")
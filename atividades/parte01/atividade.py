import os

os.system("cls")

nome = input("Informe seu nome: ")
massa = float(input("Informe sua massa em kg: "))
altura = float(input("Informe sua altura em metros: "))

imc = massa / (altura * altura)

print(f"\n{nome}, seu IMC é {imc:.2f}")

if imc < 18.5:
    print("Você está magro.")
elif imc < 25:
    print("Você está no peso ideal.")
else:
    print("Você está gordo.")

    os.system("cls" if os.name == "nt" else "clear")
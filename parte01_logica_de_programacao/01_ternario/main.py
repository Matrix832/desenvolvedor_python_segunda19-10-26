# declaração de variaveis 

nome = input("Informe seu nome: ").strip().title()
idade = int(input("informe sua idade:")) 

print(f"{nome} {'e maior de idade' if idade >=18 else  'e menor de idade'}.")
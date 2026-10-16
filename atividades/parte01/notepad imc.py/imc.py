import os
os.system("cls")

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

while True:
    os.system("cls")
    print(f"Ola {nome}, filmes em cartaz:")
    print("Sala 1 - Divertida Mente 2 - 0 anos")
    print("Sala 2 - Deadpool - 18 anos")
    print("Sala 3 - Velozes e Furiosos - 14 anos")
    print("Sala 4 - Oppenheimer - 16 anos")
    print("0 - Sair")

    sala = int(input("\nEscolha a sala: "))

    if sala == 0:
        print("Tchau!")
        break

    if sala == 1:
        print("\nBom filme! Divertida Mente 2 liberado.")
        break

    elif sala == 2:
        if idade >= 18:
            print("\nBom filme! Deadpool liberado.")
            break
        else:
            print("\nVoce nao tem idade para esse filme!")
            input("Aperte ENTER para voltar...")

    elif sala == 3:
        if idade >= 14:
            print("\nBom filme! Velozes liberado.")
            break
        else:
            print("\nVoce nao tem idade para esse filme!")
            input("Aperte ENTER para voltar...")

    elif sala == 4:
        if idade >= 16:
            print("\nBom filme! Oppenheimer liberado.")
            break
        else:
            print("\nVoce nao tem idade para esse filme!")
            input("Aperte ENTER para voltar...")

    else:
        print("\nSala nao existe!")
        input("Aperte ENTER para voltar...")
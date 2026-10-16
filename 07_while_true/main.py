# importa biblioteca 
import os

os.system("cls" if os.name == "nt" else "clear")

#loop
while True: 
    aluno = input("Informe o nome do aluno:").strip().title()

    try: 
        nota = float(input("informe a nota de 0 a 10:").replace(",","."))

        if nota >= 0 and nota <= 10:
            print(f"Nota do {aluno}: {nota}")
            if nota >= 7:
                print(f"{aluno} foi aprovado.")
            elif nota >= 5:
                print(f"{aluno} está de recuperação.")
            else:
                print(f"{aluno} foi reprovado.")
        else:
            print("nota invalida.")
    
    except Exception as e: 
        print(f"Não foi possivel calcular a media. {e}")

    continuar = input("deseja inserir outra nota? 'sim' para prosseguir qualquer outro valor para encerrar: ").strip().lower()
    if continuar != "sim":
        break
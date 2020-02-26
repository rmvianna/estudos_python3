import random

def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************")

    pontuacao = 1000
    numero_maximo = 100
    total_tentativas = 0
    nivel = -1
    numero_secreto = random.randint(1, numero_maximo)

    print("Escolha o nível de dificuldade")
    print("(1) Fácil")
    print("(2) Médio")
    print("(3) Difícil")

    try:
        nivel = int(input("> "))
    except ValueError:
        print("Entrada inválida. Encerrando...")
        exit(-1)

    if (nivel >= 1 and nivel <= 3):
        if (nivel == 1):
            total_tentativas = 20
        elif (nivel == 2):
            total_tentativas = 10
        else:
            total_tentativas = 5

        for tentativa in range(total_tentativas):
            print(f"Tentativa {tentativa + 1} de {total_tentativas}") #Utilizando como se fosse printf
            #print("Tentativa {} de {}".format(tentativa + 1, total_tentativas)) #Utilizando funcao format da String

            try:
                chute = int(input(f"Digite um número entre 1 e {numero_maximo}: "))
            except ValueError:
                print("Você não digitou um número válido!")
                continue

            if (chute < 1 or chute > numero_maximo):
                print("Você não digitou um número válido!")
                continue

            if (chute < numero_secreto):
                print("Você errou! O seu chute foi menor que o número secreto")
                pontuacao -= (numero_secreto - chute)
            elif (chute > numero_secreto):
                print("Você errou! O seu chute foi maior que o número secreto")
                pontuacao -= (chute - numero_secreto)
            else:
                print(f"Você acertou! Sua pontuação final foi de {pontuacao} pontos utilizando {tentativa} tentativas!")
                break
    else:
        print("Nível de dificuldade inválido!")

    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()
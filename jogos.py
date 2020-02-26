import adivinhacao
import forca

print("*************")
print("*** JOGOS ***")
print("*************")

print("Escolha o jogo desejado")
print("(1) Forca")
print("(2) Adivinhação")

tipo_jogo = int(input("> "))

if (tipo_jogo == 1):
    forca.jogar()
elif (tipo_jogo == 2):
    adivinhacao.jogar()
else:
    print("Jogo inexistente!")

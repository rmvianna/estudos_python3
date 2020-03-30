import os
import random
import unicodedata

def jogar():
    categoria = carregar_categoria()

    palavra_secreta = carregar_palavra_secreta(categoria)

    palavra_descoberta = inicializar_palavra_descoberta(palavra_secreta)

    chutes = []
    total_tentativas = 7
    erros = 0

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        desenha_forca(erros)

        print()
        print(str(palavra_descoberta).strip('[]').replace(",", " ").replace("'", ""))
        print()

        chute = informar_chute(chutes)
        while (chute == None):
            chute = informar_chute(chutes)

        #Remove acentuação da palavra secreta para fins de comparação
        palavra = unicodedata.normalize('NFD', palavra_secreta).encode('ASCII', 'ignore').decode("UTF-8")

        if (chute in palavra):
            revelar_palavra_secreta(chute, palavra, palavra_secreta, palavra_descoberta)
        else:
            erros += 1

        enforcou = erros == total_tentativas
        acertou = "_" not in palavra_descoberta

    imprimir_fim_jogo(enforcou, palavra_secreta)
        

def carregar_categoria():
    print("**********************************")
    print("    Bem-vindo ao jogo da Forca!   ")
    print("Categorias disponíveis de palavras")
    print("(1) - Frutas")
    print("(2) - Paises")
    print("(3) - Animais")
    print("**********************************")

    categorias = {"1": "frutas", "2": "paises", "3": "animais"}

    tipo_categoria = input("Informe a categoria: ")
    
    while (tipo_categoria not in categorias):
        tipo_categoria = input("Categoria inválida! Digite novamente: ")

    cls()
    return categorias[tipo_categoria]

def carregar_palavra_secreta(categoria):
    palavra_secreta = ""

    with open(f"{categoria}.txt", "r", 1, "UTF-8") as base_palavras_secretas:
        linhas_arquivo = base_palavras_secretas.readlines()
        palavra_secreta = linhas_arquivo[random.randrange(0, len(linhas_arquivo))].upper().strip()

    return palavra_secreta

def inicializar_palavra_descoberta(palavra_secreta):
    palavra_descoberta = ["_"] * len(palavra_secreta)
    caracteres_nao_letras = (" ", "-")
    posicao = 0

    for letra in palavra_secreta:
        if (letra in caracteres_nao_letras):
            palavra_descoberta[posicao] = letra
        posicao += 1

    return palavra_descoberta

def informar_chute(chutes):
    chute = input("Digite uma letra: ").strip().upper()

    if (chute in chutes):
        print("Você já informou essa letra!")
        return None

    chutes.append(chute)
    cls()
    
    return chute

def revelar_palavra_secreta(chute, palavra, palavra_secreta, palavra_descoberta):
    posicao = -1

    for letra in palavra:
        posicao += 1
        if (letra == chute):
            palavra_descoberta[posicao] = palavra_secreta[posicao]    

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprimir_fim_jogo(enforcou, palavra_secreta):
    if (enforcou):
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    else:
        print(f"Parabéns, você acertou a palavra {palavra_secreta}!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    input()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

if (__name__ == "__main__"):
    jogar()

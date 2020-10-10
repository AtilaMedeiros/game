import random


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertada = inicializa_letras_acertadas(palavra_secreta)
    imprime_letras_acertada(letras_acertada)
    imprime_quantidade_tentativas(palavra_secreta)

    erros = 0

    while ("atila" != "camila"):

        chute = pede_chute()

        if (chute in palavra_secreta):

            marca_chute_correto(palavra_secreta, chute, letras_acertada)

        else:
            erros += 1
            imprime_progressao_erros(erros, palavra_secreta)
            desenha_forca(erros)

        # teste do while
        if (erros == len(palavra_secreta)):
            imprime_mensagem_perdeu(palavra_secreta)
            break

        if ("_" not in letras_acertada):
            imprime_mensagem_ganhou()
            break


def imprime_mensagem_abertura():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def imprime_letras_acertada(letras_acertada):
    print(f" \n \n Forca  = >  {letras_acertada} ")


def imprime_quantidade_tentativas(palavra_secreta):
    print(f"\n \n Você pode errar {len(palavra_secreta)} vezes.\n \n")


def pede_chute():
    return input("Qual letra? ").strip().upper()


def marca_chute_correto(palavra_secreta, chute, letras_acertada):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertada[index] = letra

        index += 1

    print(f" \n \n Forca  = >  {letras_acertada}  \n \n ")


def imprime_progressao_erros(erros, palavra_secreta):
    print(f"\n Total de erros {erros}/{len(palavra_secreta)} \n")


def imprime_mensagem_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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


def imprime_mensagem_ganhou():
    print("Parabéns, você ganhou!")
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


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
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


if (__name__ == "__main__"):
    jogar()

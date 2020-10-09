import random


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertada = inicializa_letras_acertadas(palavra_secreta)
    print(f"\n \n Você pode errar {len(palavra_secreta)} vezes.")
    print(f" \n \n Forca  = >  {letras_acertada}  \n \n ")

    erros = 0

    while ("atila" != "camila"):

        chute = pede_chute()

        if (chute in palavra_secreta):

            marca_chute_correto(palavra_secreta, chute, letras_acertada)

        else:
            erros += 1
            print(f"Total de erros {erros}/{len(palavra_secreta)}")

        # teste do while
        if (erros == len(palavra_secreta)):
            print("Você perdeu !!!")
            break

        if ("_" not in letras_acertada):
            print(f" \n \n Forca  = >  {letras_acertada}  \n \n ")
            print("Você ganhou!!!")
            break

    print("Fim do jogo")


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


def pede_chute():
    return input("Qual letra?").strip().upper()


def marca_chute_correto(palavra_secreta, chute, letras_acertada):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertada[index] = letra

        index += 1

    print(f" \n \n Forca  = >  {letras_acertada}  \n \n ")


if (__name__ == "__main__"):
    jogar()

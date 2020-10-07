
import forca
import adiviacao


def menu():

    print("***************************")
    print("Bem vindo ao menu dos jogos")
    print("***************************")

    print("1 - Adivinhação | 2 - Forca | 3 - Sair")
    jogo = 0

    while (jogo < 1 or jogo > 2):

        jogo = int(input("Digite o nomero do jogo: "))

        if (jogo == 1):
            print("Jogando Adivinhação \n")
            adiviacao.jogar()
        elif(jogo == 2):
            print("Jogando Forca \n")
            forca.jogar()
        elif(jogo == 3):
            break
        else:
            print("Digite uma das opções do menu")


if (__name__ == "__main__"):
    menu()

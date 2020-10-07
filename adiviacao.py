import random


def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("********************************* \n")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = int(1000)

    print(f"1 - Baixo | 2 - Médio | 3 - Difícil {numero_secreto}")

    while (total_de_tentativas <= 1 or total_de_tentativas >= 3):
        nivel = int(input('Digite o nível a dificuldade:'))

        if (nivel == 1):
            total_de_tentativas = 20
            print(
                f"Você tem {total_de_tentativas} tentativas e {pontos} pontos ")

            break

        elif (nivel == 2):
            total_de_tentativas = 10
            print(
                f"Você tem {total_de_tentativas} tentativas e {pontos} pontos ")
            break

        elif (nivel == 3):
            total_de_tentativas = 5
            print(
                f"Você tem {total_de_tentativas} tentativas e {pontos} pontos ")
            break

        else:
            print("Favor digite um número entre 1 e 3 ")
            continue

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))
        # print(f"Você digitou {chute}")

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if(chute == numero_secreto):
            print(f"Você acertou e tem {pontos} pontos")
            break
        else:
            if(chute > numero_secreto):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(chute < numero_secreto):
                print("Você errou! O seu chute foi menor do que o número secreto.")

            pontos_perdidos = abs(chute - numero_secreto)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()

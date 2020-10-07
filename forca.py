def jogar():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")

    palavra_chave = "banana"

    acertou = False
    enforcou = False

    while (not acertou and not enforcou):
        chute = input("Qual letra?")

        index = 0
        for letra in palavra_chave:
            if (chute == letra):
                print(f"Encontrei a letra {chute} na posição {index} ")

            index += 1


if (__name__ == "__main__"):
    jogar()

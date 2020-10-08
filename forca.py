def jogar():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")

    palavra_secreta = input("\n Digite a palavra secreta: ").strip().upper()

    conta_letras = len(palavra_secreta)
    letras_acertada = list(conta_letras * '_')
    erros = 0
    acertou = False
    enforcou = False

    print(f"\n \n Você pode errar {conta_letras} vezes.")
    print(f" \n \n Forca  = >  {letras_acertada}  \n \n ")

    while (not acertou and not enforcou):

        chute = input("Qual letra?").strip().upper()

        if (chute in palavra_secreta):

            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertada[index] = letra

                index += 1

            print(f" \n \n Forca  = >  {letras_acertada}  \n \n ")

        else:
            erros += 1
            print(f"Total de erros {erros}/{conta_letras}")

        # teste do while
        enforcou = erros == conta_letras
        acertou = "_" not in letras_acertada

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()

def jogar():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")

    palavra_secreta = input("\n Digite a palavra secreta: ").strip().upper()
    letras_acertada = ["_" for letra in palavra_secreta]

    erros = 0

    print(f"\n \n Você pode errar {len(palavra_secreta)} vezes.")
    print(f" \n \n Forca  = >  {letras_acertada}  \n \n ")

    while ("atila" != "camila"):

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


if (__name__ == "__main__"):
    jogar()

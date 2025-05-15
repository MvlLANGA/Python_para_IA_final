
while True:
    plvr1 = input("Digite uma palavra: ")
    plvr2 = input("Digite outra palavra: ")

    if len(plvr1) != len(plvr2):
        print("Essas palavras não tem a mesma quantidade de caracteres")

    else:
        print("Essas palavras são iguais")
        break
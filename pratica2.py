palavra = input("escolha uma palavra: ")

penultimo = len(palavra)-2
if palavra[penultimo] == palavra[1]:
    print("Os caracteres são iguais!!")
else:
    print("Os caracteres são diferentes")
        
#while
#Aprendendo a trabalhar com while
#importar biblioteca
from math import sqrt



n = 0

while True:
    numero = int(input("Coloque um numero: "))
    if numero == -1:
        print("Voce pausou a execução do programa")
        break
    print("Voce ainda não pausou")
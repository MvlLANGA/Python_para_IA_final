import random
tentativa = random.randint(1,100)

while True:
    num = int(input("Escolha um numero de 1 a 100: "))
    tentativa +=1

    if num < tentativa:
        print("O numero precisa ser maior")
        

    elif num > tentativa:
        print("O numero tem que ser menor")

    else:
        print("Parabens!!! Você acertou")
        break
    
   


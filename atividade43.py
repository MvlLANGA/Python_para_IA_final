ano = int(input("Digite um ano: "))
while True:
    ano += 1
    if (ano % 4 ==0 and ano % 100 !=0) or ano % 400 == 0:
        print(f"Proximo ano bissexto é {ano}")
        break
   

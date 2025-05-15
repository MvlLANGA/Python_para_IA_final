import random

saldo = 1500
print(f"Seu saldo atual é R${saldo}")

while True:
    saque = float(input("Qual o valor do Saque:R$ "))
    

    if saque % 10 != 0:
        print("Valor deve ser multiplo de 10.")


    elif saque > saldo:
        print("Valor de saque insulficiente")

    elif saque <= saldo:
        print("Valor Invalido")

    else:
        saldo -= saque
        print(f"Saque de R${saque} realizado com sucesso")
        print(f"Saldo restante: R${saldo}")
        break
        

        
    
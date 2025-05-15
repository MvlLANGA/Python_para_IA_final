import re

 
while True:
    senha = input("Qual a sua senha: ")
    temMaiuscula = re.search("[A-Z]", senha)
    temMinuscula = re.search("[a-z]", senha)
    temNumero = re.search("[0-9]", senha)
    if len(senha) < 8:
        print("Senha precisa ter 8 caracteres")

    elif temMaiuscula == None:
        print("1 letra maiuscula")

    elif temMinuscula == None:
        print("1 letra minuscula")

    elif temNumero == None:
        print("1 numero")
        
    else:
        print("Senha compativel")
        break
      
        
   



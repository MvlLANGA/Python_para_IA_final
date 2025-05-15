# Voce cria as variaveis
entrada = input("Solicite uma entrada: ")

# aqui se o texto for menor que 20 caracteres   
if len(entrada) < 20:
    caracteres = "*" * (20- len(entrada))
    resultado = caracteres + entrada
   

else:
# Usa esses : para fatiar os caracteres    
    resultado = entrada[:20]
    print(entrada)


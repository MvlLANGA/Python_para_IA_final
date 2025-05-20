numero =int(input("Qual o numero: "))
contador = 0

while contador < numero: # Esse primeiro While difine quantas linhas o elemento vai ter
    elemento = "" #Deixamos a variavel elemento vazio
    coluna = 0 # E deixamos a variavel coluna zerada
    while coluna< numero:#Para cada vez que repetir o primeiro while esse while repete 5x 

        if (coluna + contador) %2 == 0:
            elemento += "0"
             # Se a soma de coluna + contador dividido por 2 a sobra for igual a 0 ele vai 
        else:
            elemento += "1"
        coluna += 1
    contador += 1    
    print(elemento)

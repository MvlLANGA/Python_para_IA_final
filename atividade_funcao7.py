def triangulo(x):
    contador=0
    while contador < x:
        elemento = "#" * (contador +1) #Para fazer o resultado ao contrario faria (x - contador)
        print(elemento)
        contador +=1

triangulo(5)

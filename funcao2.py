def comprimentar(nome): # Voce chama uma funcao
    print(f"ola {nome}") # printa essa função
def comprimentar_mais(nome, vezes):#Chama outra função com um argumento nome e vezes
    while vezes > 0: #nesse While voce coloca que comprimentar tem que ser maior que 0
        comprimentar(nome) # comprimentar e chama o argumento nome
        vezes -=1 # cada vez que voce pedoir um  numero ele vai diminuindo 1 vez
comprimentar_mais("Maria", 5) # aqui vc faz a chamada da segunda função coloca o argumento nome e o argumnento vezes
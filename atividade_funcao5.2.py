def quadrado(texto, numero):
    #variavel que multplica a string pelo numero passado como parametros
    stringTotal = (texto *numero)
    #variavel que inicia em zero para ser usada como controle mais pra frente
    linha = 0
    while linha < numero: 
        coluna  = 0
        letras = ""

        while coluna < numero:
            posicao = linha * numero + coluna
            letras += stringTotal[posicao]
            coluna += 1
        print(letras)
        linha +=1
quadrado("jumanji",4)
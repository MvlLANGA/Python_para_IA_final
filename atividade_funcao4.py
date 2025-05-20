def mesaXadrez(tamanho):# Aqui vc cria a função com (Tamanho)

    linha = 0 # Aqui criamos uma variavel linha 
    while linha < tamanho: # A linha é menor que o tamanho
        coluna = 0 #cria uma variavel chamada coluna
        linha_texto = "" #cria
        while coluna < tamanho:# Nesse while 
            if (linha + coluna)% 2 ==0:
                linha_texto += "1"
            else:
                linha_texto += "0"
            coluna +=1
        print(linha_texto)
        linha +=1
mesaXadrez(10)
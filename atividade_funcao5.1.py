def quadradoString():
    texto = input("Digite algo: ") # Exemplo: "abc" (índices 0:a, 1:b, 2:c)
    tamanho = len(texto) # Tamanho = 3 (0,1,2)
    indice = 0 # Começa no índice 0
   
    while indice < tamanho: # Loop enquanto 0<3 | 1<3 | 2<3 | 3<3 (falso para o laço para aqui)
         print(texto[indice:] + texto[:indice]) # Concatena partes da string
         indice += 1 # Incrementa o índice: 0→1→2→3
       
quadradoString() # Chama a função para executa-lá
       
# """     Iteração  indice  texto[indice:]  texto[:indice]  Saída
#         1ª            0       "abc"           "" (vazio)      "abc" + "" = "abc"
#         2ª            1       "bc"            "a"             "bc" + "a" = "bca"
#         3ª            2       "c"             "ab"            "c" + "ab" = "cab" """
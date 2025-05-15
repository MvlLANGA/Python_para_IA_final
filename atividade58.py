string = input("Vamos usar uma string: ")

caracteres = 30
linha_borda = "*" * caracteres

espaco_total = caracteres - len(string)
espaco_esquerda = espaco_total //2
espaco_direita = espaco_total - espaco_esquerda-2

if len(string) % 2 == 0:
    linha_central = "*" + "" * espaco_esquerda + string + "" * espaco_direita + "*"
else:
    linha_central = "*" + string + "*"

print(linha_borda)
print(linha_central)
print(linha_borda)
    
def linha (tamanho, texto):
    if texto[0] == "":
        print("*"* texto)
    else:
        print(texto[0]*tamanho)

def caixa_hashtag(altura):
    contador =0
    while contador < altura:
        linha(10, "#")
        contador += 1

caixa_hashtag(6)

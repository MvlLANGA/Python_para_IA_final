def maior_numero(num1,num2,num3):
    if num1 > num2 > num3:
        print(num1)
    elif num1 < num2 > num3:
        print(num2)
    else:
        print(num3)

maior_numero(20, 50, 60)

# Ou Pode_se fazer desse jeito

#def maior_numero(a,b,c)
#   return max(a,b,c) # o max busca o maior numero 

#print(maior_numero(10,20,30))
#print(maio_numero(50,14,90))     
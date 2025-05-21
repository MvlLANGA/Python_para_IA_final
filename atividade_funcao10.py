def mesmo_caracter(str, num1, num2):
    if num1 < 0 or num2 < 0 or num1 >= len(str) or num2 >= len(str): # aqui voce compara os argumentoS
        return False # Retorna ele como falso
    
    else:
        if str[num1] != str[num2]:
            return False
        else:
            return True
    
print(mesmo_caracter("arara", 0, 4))
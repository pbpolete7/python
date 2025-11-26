def comptar_majuscules(cadena):
    comptador = 0
    for caracter in cadena:
        if caracter.isupper():   # isupper() comprova si el caràcter és majúscula
            comptador += 1
    return comptador
print(comptar_majuscules("Hola MON"))          # 4
print(comptar_majuscules("Python"))            # 1
print(comptar_majuscules("aAbBcC"))            # 3
print(comptar_majuscules("tot en minuscules")) # 0

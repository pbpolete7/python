def binari_a_enter(binari):
    resultat = 0
    pot = 0

    for digit in reversed(binari):
        if digit == '1':
            resultat += 2 ** pot
        pot += 1

    return resultat

# Exemples
print(binari_a_enter("1010"))   # 10
print(binari_a_enter("1111"))   # 15
print(binari_a_enter("100000")) # 32

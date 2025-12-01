# Programa que mostra els dígits parells d'un número

n = input("Introdueix un número: ")

print("Dígits parells:", end=" ")

for digit in n:
    if digit.isdigit():          # Comprovem que sigui un dígit
        if int(digit) % 2 == 0:  # Comprovem si és parell
            print(digit, end=" ")

print()  # Salt de línia final

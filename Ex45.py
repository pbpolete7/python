# Programa que suma els dígits d'un número i indica si la suma és parell o senar

n = input("Introdueix un número: ")

# Sumar els dígits
suma = 0
for digit in n:
    if digit.isdigit():        # per assegurar que només suma dígits
        suma += int(digit)

# Mostrar resultat
print(f"La suma dels dígits és: {suma}")

if suma % 2 == 0:
    print("La suma és parell.")
else:
    print("La suma és senar.")

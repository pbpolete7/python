# Programa que suma els quadrats dels números separats per 4 posicions

n = int(input("Introdueix un número menor de 100: "))

if n >= 100:
    print("❌ Has d'introduir un número menor de 100.")
else:
    suma = 0
    print("Càlcul:", end=" ")

    primer = True
    for x in range(n - 4, 0, -4):
        suma += x ** 2
        if primer:
            print(f"{x}^2", end="")
            primer = False
        else:
            print(f" + {x}^2", end="")

    print(f"\n\nLa suma dels quadrats és: {suma}")

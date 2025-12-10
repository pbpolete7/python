# Demanar els dos números a l'usuari
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))

# Determinar l'inici i el final correctes
inici = min(num1, num2)
final = max(num1, num2)

# Sumar tots els números entre inici i final
suma = 0
for i in range(inici, final + 1):
    suma += i

print(f"La suma dels números entre {inici} i {final} és: {suma}")

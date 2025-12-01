# Programa que imprimeix la taula de multiplicar d'un número (1 a 20)

while True:
    n = int(input("Introdueix un número entre 1 i 20: "))
    if 1 <= n <= 20:
        break
    print("❌ Error: el número ha d'estar entre 1 i 20.")

print(f"\nTaula de multiplicar del {n}:\n")

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

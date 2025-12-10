# Funció per comprovar si un número és primer
def es_primer(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Llista per guardar els nombres primers
primers = []

# Comprovar els números de 1 a 100
for i in range(1, 101):
    if es_primer(i):
        primers.append(i)

# Mostrar els nombres primers
print("Nombres primers entre 1 i 100:")
print(primers)

# Mostrar quants n’hi ha
print(f"Total de nombres primers: {len(primers)}")

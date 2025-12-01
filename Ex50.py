import random

def llista_20_elements():
    return [random.randint(1, 100) for _ in range(20)]
def hi_ha_duplicats(llista):
    return len(set(llista)) != len(llista)
# Generar la llista
llista = llista_20_elements()

print("Llista generada:")
print(llista)

# Comprovar si hi ha duplicats
if hi_ha_duplicats(llista):
    print("Hi ha elements duplicats.")
else:
    print("No hi ha elements duplicats.")

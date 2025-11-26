# Programa per calcular edats i mostrar taula

any_actual = int(input("Introdueix l'any actual: "))

noms = []
naixements = []
edats = []

# Llegim les dades de 4 persones
for i in range(4):
    nom = input(f"Introdueix el nom de la persona {i+1}: ")
    any_naixement = int(input(f"Introdueix l'any de naixement de {nom}: "))

    noms.append(nom)
    naixements.append(any_naixement)
    edats.append(any_actual - any_naixement)

# Imprimir la taula
print("\nNom\t\tData naixement\tAnys que farà aquest any")
for i in range(4):
    print(f"{noms[i]}\t\t{naixements[i]}\t\t{edats[i]}")

def nums_que_comencen_per(llista, lletra):
    comptador = 0
    lletra = lletra.lower()
    for nom in llista:
        if nom.lower().startswith(lletra):
            comptador += 1
    return comptador
# Demanem la lletra a l'usuari
lletra = input("Introdueix la lletra per comprovar: ")

# Llista de noms (pots canviar-la o demanar-la per teclat)
noms = ["Anna", "Joan", "albert", "Maria", "arnau", "Pere"]

# Comptem
resultat = nums_que_comencen_per(noms, lletra)

# Mostrem resultat
print(f"Hi ha {resultat} noms que comencen per '{lletra}'.")

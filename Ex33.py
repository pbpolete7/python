def nums_que_comencen_per(llista, lletra="a"):
    comptador = 0
    lletra = lletra.lower()   # per evitar problemes amb majúscules
    for nom in llista:
        if nom.lower().startswith(lletra):
            comptador += 1
    return comptador
noms = ["Anna", "Joan", "albert", "Maria", "arnau", "Pere"]
print(nums_que_comencen_per(noms, "a"))   # Retorna 3

def crear_llista_fitxer(nom_fitxer):
    llista = []
    with open(nom_fitxer, "r", encoding="utf-8") as f:
        for linia in f:
            paraules = linia.split()     # separa per espais i salts de línia
            llista.extend(paraules)      # afegeix les paraules a la llista
    return llista
"Hola món"
"Això és una prova"
llista = crear_llista_fitxer("text.txt")
print(llista)

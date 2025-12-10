def index_paraula(llista, paraula):
    """
    Retorna l'índex de 'paraula' dins de 'llista' ordenada.
    Si no hi és, retorna -1.
    """
    esquerra = 0
    dreta = len(llista) - 1

    while esquerra <= dreta:
        mig = (esquerra + dreta) // 2
        if llista[mig] == paraula:
            return mig
        elif llista[mig] < paraula:
            esquerra = mig + 1
        else:
            dreta = mig - 1

    return -1

# Exemple d'ús
paraules = ["apple", "banana", "cherry", "date", "fig"]
print(index_paraula(paraules, "cherry"))  # Sortida: 2
print(index_paraula(paraules, "orange"))  # Sortida: -1

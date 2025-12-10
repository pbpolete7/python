def coincidencies(llista):
    """
    Retorna el nombre d'elements on el valor coincideix amb el seu índex.
    """
    return sum(1 for idx, valor in enumerate(llista) if idx == valor)

# Exemple d'ús
llista = [0, 2, 3, 3, 4]
resultat = coincidencies(llista)
print(resultat)  # Sortida: 3

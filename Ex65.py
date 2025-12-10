def llista_a_diccionari(llista):
    """
    Retorna un diccionari amb els elements de la llista com a claus
    i els seus índexs com a valors.
    """
    return {valor: idx for idx, valor in enumerate(llista)}

# Exemple d'ús
llista = ['casa', 'cotxe', 'cadira', 'taula']
resultat = llista_a_diccionari(llista)
print(resultat)  # Sortida: {'casa': 0, 'cotxe': 1, 'cadira': 2, 'taula': 3}

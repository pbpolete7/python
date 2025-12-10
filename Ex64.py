def concatenar_llistes(llista1, llista2, connector):
    """
    Concatena dues llistes amb un connector entre els elements corresponents.
    """
    return [a + connector + b for a, b in zip(llista1, llista2)]

# Exemple d'ús
llista1 = ['sub', 'supra']
llista2 = ['campió', 'campiona']
connector = '-'

resultat = concatenar_llistes(llista1, llista2, connector)
print(resultat)  # Sortida: ['sub-campió', 'supra-campiona']

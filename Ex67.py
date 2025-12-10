def lletres_paraula(paraula):
    """
    Retorna una llista amb les lletres de la paraula donada.
    """
    return [lletra for lletra in paraula]

# Exemple d'ús
paraula = "institut"
resultat = lletres_paraula(paraula)
print(resultat)  # Sortida: ['i', 'n', 's', 't', 'i', 't', 'u', 't']

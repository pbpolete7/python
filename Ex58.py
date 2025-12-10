def elements_parells(llista):
    """
    Retorna els elements que estan en posicions parelles dins d'una llista.
    """
    return [llista[i] for i in range(len(llista)) if i % 2 == 0]

# Exemple de prova
paraules = ["apple", "banana", "cherry", "date", "fig", "grape"]
resultat = elements_parells(paraules)
print(resultat)  # Sortida: ['apple', 'cherry', 'fig']

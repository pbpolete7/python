def paraules_per_llletra(llista, lletra):
    """
    Retorna una llista amb les paraules que comencen per la lletra donada.
    """
    return list(filter(lambda paraula: paraula.startswith(lletra), llista))

# Exemple d'ús
paraules = ["maria", "manta", "peu", "mà"]
resultat = paraules_per_llletra(paraules, 'p')
print(resultat)  # Sortida: ['peu']

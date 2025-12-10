def elevar_a_potencia(n, potencia):
    """
    Retorna una llista amb els n primers números elevats a la potència donada.
    """
    return [i ** potencia for i in range(n)]

# Exemple d'ús: 10 primers nombres al quadrat
quadrats = elevar_a_potencia(10, 2)
print(quadrats)  # Sortida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Exemple d'ús: 10 primers nombres al cub
cubs = elevar_a_potencia(10, 3)
print(cubs)  # Sortida: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
